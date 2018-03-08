"""
Implementation of the PayTabs credit card processor using the newer "Secure Acceptance API".
The previous Hosted Order Page API is being deprecated as of 9/14.

For now, we're keeping the older implementation in the code-base so we can
quickly roll-back by updating the configuration.  Eventually, we should replace
the original implementation with this version.

To enable this implementation, add the following Django settings:

    CC_PROCESSOR_NAME = "PayTabs"
    CC_PROCESSOR = {
        "PayTabs": {
            "WSDL_SERVICE_URL": "<wsdl service url given by KKUx>",
            "SERVICE_KEY": "<SERVICE_KEY given by KKUx>",
            "SECRET_KEY": "<secret key>",
            "RETURN_URL": "<return_url>",
            "MERCHANT_EMAIL": "<merchant_email>",
            "SITE_URL": "<site_url>** Site URL must match with profile site URL",
            "IP_MERCHANT": "<Public ip of MERCHANT>",
        }
    }
    Example:
    CC_PROCESSOR = {
        "PayTabs": {
            "WSDL_SERVICE_URL": "https://kkuservices.kku.edu.sa/MyKkuServices/MarketService.asmx?WSDL",
            "SECRET_KEY": "asdf",
            "MERCHANT_EMAIL": "<PayTabs merchant_email>"
        }
    }
"""

import hmac
import binascii
import re
import json
import uuid
import logging
from textwrap import dedent
from datetime import datetime
from collections import OrderedDict, defaultdict
from decimal import Decimal, InvalidOperation
from hashlib import sha256

from django.conf import settings
from django.utils.translation import ugettext as _, ugettext_noop
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from edxmako.shortcuts import render_to_string, render_to_response
from shoppingcart.models import Order
from shoppingcart.processors.exceptions import *
from shoppingcart.processors.helpers import get_processor_config
# from shoppingcart.views import verify_for_closed_enrollment
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from suds.client import Client

log = logging.getLogger(__name__)

# Translators: this text appears when an unfamiliar error code occurs during payment,
# for which we don't know a user-friendly message to display in advance.
DEFAULT_REASON = ugettext_noop("UNKNOWN REASON")


@csrf_exempt
@require_POST
@login_required
def create_invoice(request):
    """
    Create invoice at Paytabs end using KKUx wrapper.
    """
    user = request.user
    cart = Order.get_cart_for_user(user)
    # is_any_course_expired, expired_cart_items, expired_cart_item_names, valid_cart_item_tuples = \
    #     verify_for_closed_enrollment(user, cart)
    # if is_any_course_expired:
    #     for expired_item in expired_cart_items:
    #         Order.remove_cart_item_from_order(expired_item, request.user)
    #     cart.update_order_type()

    url_service = get_processor_config().get('WSDL_SERVICE_URL', '')
    secret_key = get_processor_config().get('SECRET_KEY', '')
    service_key = get_processor_config().get('SERVICE_KEY', '')
    site_url = get_processor_config().get('SITE_URL', '')
    merchant_email = get_processor_config().get('MERCHANT_EMAIL', '')
    ip_merchant = get_processor_config().get('IP_MERCHANT', '-')

    return_url = request.build_absolute_uri(
        reverse("shoppingcart.views.postpay_callback")
    )

    total_cost = cart.total_cost
    amount = "{0:0.2f}".format(total_cost)
    ip_customer = cart.ip_customer if cart.ip_customer else '-'
    ip_merchant = ip_merchant

    try:
        title = cart.orderitem_set.all().values()[0]['line_desc']
    except:
        title = 'Description not available'
    unit_price = ''
    quantity = ''
    products_per_title = ''
    for index, cart_item in enumerate(cart.orderitem_set.filter(status=cart.status)):
        if not index:
            quantity = str(cart_item.qty)
            unit_price = str(cart_item.unit_cost)
            products_per_title = cart_item.line_desc
        else:
            quantity += ' || ' + str(cart_item.qty)
            unit_price += ' || ' + str(cart_item.unit_cost)
            products_per_title += ' || ' + cart_item.line_desc
    # Paymnet gateway only allow 175 characters
    products_per_title = products_per_title[:175]
    if hasattr(user, 'profile'):
        full_name = cart.user.profile.name
        full_name = full_name.split(' ')
        first_name = cart.user.first_name if cart.user.first_name else full_name[0]
        last_name = cart.user.last_name
        mailing_address = cart.user.profile.mailing_address
        city = cart.user.profile.city
        country_code = cart.user.profile.country_code
        phone_number = cart.user.profile.phone_number
        postal_code = cart.user.profile.postalcode
    else:
        first_name = cart.user.first_name
        last_name = cart.user.last_name
        mailing_address = ''
        city = ''
        country_code = ''
        phone_number = ''
        postal_code = ''

    client = Client(url_service)
    # client.set_options(port='MarketServiceSoap12')
    client.set_options(port='MarketServiceSoap')
    response = client.service.CreateInvoice(
        merchant_email=merchant_email,
        secret_key=secret_key,
        amount=amount,
        site_url=site_url,
        title=title,
        unit_price=unit_price,
        quantity=quantity,
        products_per_title=products_per_title,
        return_url=return_url,
        cc_first_name=first_name,
        cc_last_name=last_name,
        cc_phone_number=country_code,
        phone_number=phone_number,
        billing_address=mailing_address,
        city=city,
        postal_code=postal_code,
        email=cart.user.email,
        ip_customer=ip_customer,
        ip_merchant=ip_merchant,
        address_shipping=mailing_address,
        city_shipping=city,
        postal_code_shipping=postal_code,
        other_charges='0.0',
        discount='0',
        reference_no=str(cart.id),
        KEY=service_key,
    )
    try:
        if not int(response.response_code) == 4012:
            error_html = _get_processor_exception_html(response)
            return render_to_response('shoppingcart/error.html', {'order': None,
                                                                  'error_html': error_html})
        else:
            request.session['p_id'] = str(response.p_id)
            return HttpResponseRedirect(str(response.payment_url))
    except:
        error_html = _get_processor_exception_html(response)
        return render_to_response('shoppingcart/error.html', {'order': None,
                                                              'error_html': error_html})


def process_postpay_callback(params):
    """
    Handle a response from the payment processor.

    Concrete implementations should:
        1) Verify the parameters and determine if the payment was successful.
        2) If successful, mark the order as purchased and call `purchased_callbacks` of the cart items.
        3) If unsuccessful, try to figure out why and generate a helpful error message.
        4) Return a dictionary of the form:
            {'success': bool, 'order': Order, 'error_html': str}

    Args:
        params (dict): Dictionary of parameters received from the payment processor.
        get payment_reference in params

    Keyword Args:
        Can be used to provide additional information to concrete implementations.

    Returns:
        dict

    """

    try:
        result = _payment_accepted(params)
        if result['accepted']:
            params = result.get('processor_reply')
            _record_purchase(params, result['order'])
            return {
                'success': True,
                'order': result['order'],
                'error_html': ''
            }
        else:
            _record_payment_info(params, result['order'])
            return {
                'success': False,
                'order': result['order'],
                'error_html': _get_processor_exception_html(params)
            }
    except:
        log.exception('error processing Paytabs postpay callback')
        # if we have the order and the id, log it
        log.info(json.dumps(params))
        return {
            'success': False,
            'order': None,  # due to exception we may not have the order
            'error_html': _get_processor_exception_html(params)
        }


def render_purchase_form_html(cart, callback_url=None, extra_data=None):
    """
    Renders the HTML of the hidden POST form that must be used to initiate a purchase with CyberSource

    Args:
        cart (Order): The order model representing items in the user's cart.

    Keyword Args:
        callback_url (unicode): The URL that CyberSource should POST to when the user
            completes a purchase.  If not provided, then CyberSource will use
            the URL provided by the administrator of the account
            (CyberSource config, not LMS config).

        extra_data (list): Additional data to include as merchant-defined data fields.

    Returns:
        unicode: The rendered HTML form.

    """
    return render_to_string('shoppingcart/pay_tabs_form.html', {
        'action': reverse('create_invoice'),
        # 'params': get_signed_purchase_params(
        #     cart, callback_url=callback_url, extra_data=extra_data
        # ),
    })


def _payment_accepted(params):
    """
    Check that CyberSource has accepted the payment.

    Args:
        params: payment reference number

    Returns:
        dictionary of the form:
        {
            'accepted': bool,
            'amnt_charged': int,
            'currency': string,
            'order': Order
        }

    Raises:
        Order not found: The order does not exist.
        Wrong amount or currency: The user did not pay the correct amount.

    """
    payment_support_email = configuration_helpers.get_value('payment_support_email', settings.PAYMENT_SUPPORT_EMAIL)
    url_service = get_processor_config().get('WSDL_SERVICE_URL', '')
    secret_key = get_processor_config().get('SECRET_KEY', '')
    service_key = get_processor_config().get('SERVICE_KEY', '')
    merchant_email = get_processor_config().get('MERCHANT_EMAIL', '')
    payment_reference = params.get('payment_reference', '')
    if not payment_reference:
        return HttpResponseRedirect(reverse("shoppingcart.views.show_cart"))

    client = Client(url_service)
    client.set_options(port='MarketServiceSoap')
    response = client.service.VerifyPayment(
        merchant_email=merchant_email,
        secret_key=secret_key,
        payment_reference=payment_reference,
        KEY=service_key
    )
    processor_reply = {}
    try:
        order_id = int(response.reference_no)
        response_code = int(response.response_code)
        currency = str(response.currency)
        auth_amount = Decimal(response.amount)
        pt_invoice_id = str(response.pt_invoice_id)
        transaction_id = str(response.transaction_id)
        result = str(response.result)
        processor_reply.update({
            'reference_no': str(order_id),
            'response_code': str(response_code),
            'currency': currency,
            'amount': str(auth_amount),
            'pt_invoice_id': pt_invoice_id,
            'transaction_id': transaction_id,
            'result': result,
        })
        try:
            order = Order.objects.get(id=order_id)
            if response_code == 100:
                if auth_amount == order.total_cost and currency.lower() == order.currency.lower():
                    return {
                        'accepted': True,
                        'amt_charged': auth_amount,
                        'currency': currency,
                        'order': order,
                        'processor_reply': processor_reply
                    }
                else:
                    # The user did not pay the correct amount.
                    # error_html = _format_error_html(
                    #     _(
                    #         u"Sorry! Our payment processor sent us back a corrupted message regarding your charge, so we are "
                    #         u"unable to validate that the message actually came from the payment processor. "
                    #         u"We apologize that we cannot verify whether the charge went through and take further action on your order. "
                    #         u"Your credit card may possibly have been charged. Contact us with payment-specific questions at {email}."
                    #     ).format(
                    #         email=payment_support_email
                    #     )
                    # )
                    return {
                        'accepted': False,
                        'amt_charged': 0,
                        'currency': '',
                        'order': None,
                        'processor_reply': processor_reply
                    }
        except Order.DoesNotExist:
            # Order not found
            # error_html = _format_error_html(
            #     _(
            #         u"Sorry! Our payment processor sent us back a payment confirmation that had inconsistent data! "
            #         u"We apologize that we cannot verify whether the charge went through and take further action on your order. "
            #         u"Your credit card may possibly have been charged.  Contact us with payment-specific questions at {email}."
            #     ).format(
            #         email=payment_support_email
            #     )
            # )
            return {
                'accepted': False,
                'amt_charged': 0,
                'currency': '',
                'order': None,
                'processor_reply': processor_reply
            }
    except:
        # No response from KKUx's SOAP
        return {
            'accepted': False,
            'amt_charged': 0,
            'currency': '',
            'order': None,
            'processor_reply': processor_reply
        }


def _record_purchase(params, order):
    """
    Record the purchase and run purchased_callbacks

    Args:
        params (dict): The parameters we received from CyberSource.
        order (Order): The order associated with this payment.

    Returns:
        None

    """
    # Usually, the credit card number will have the form "xxxxxxxx1234"
    # Parse the string to retrieve the digits.
    # If we can't find any digits, use placeholder values instead.
    ccnum_str = params.get('req_card_number', '')
    mm = re.search("\d", ccnum_str)
    if mm:
        ccnum = ccnum_str[mm.start():]
    else:
        ccnum = "####"

    if settings.FEATURES.get("LOG_POSTPAY_CALLBACKS"):
        log.info(
            "Order %d purchased with params: %s", order.id, json.dumps(params)
        )

    # Mark the order as purchased and store the billing information
    order.purchase(
        processor_reply_dump=json.dumps(params)
    )


def _record_payment_info(params, order):
    """
    Record the purchase and run purchased_callbacks

    Args:
        params (dict): The parameters we received from CyberSource.

    Returns:
        None
    """
    if order:
        if settings.FEATURES.get("LOG_POSTPAY_CALLBACKS"):
            log.info(
                "Order %d processed (but not completed) with params: %s", order.id, json.dumps(params)
            )
        order.processor_reply_dump = json.dumps(params)
        order.save()
    else:
        log.info(json.dumps(params))


def _get_processor_decline_html(params):
    """
    Return HTML indicating that the user's payment was declined.

    Args:
        params (dict): Parameters we received from CyberSource.

    Returns:
        unicode: The rendered HTML.

    """
    payment_support_email = configuration_helpers.get_value('payment_support_email', settings.PAYMENT_SUPPORT_EMAIL)
    return _format_error_html(
        _(
            "Sorry! Our payment processor did not accept your payment.  "
            "The decision they returned was {decision}, "
            "and the reason was {reason}.  "
            "You were not charged. Please try a different form of payment.  "
            "Contact us with payment-related questions at {email}."
        ).format(
            decision='<span class="decision">{decision}</span>'.format(decision=params['decision']),
            reason='<span class="reason">{reason_code}:{reason_msg}</span>'.format(
                reason_code=params['reason_code'],
                reason_msg=REASONCODE_MAP.get(params['reason_code'])
            ),
            email=payment_support_email
        )
    )


def _get_processor_exception_html(response):
    """
    Return HTML indicating that an error occurred.

    Args:
        response (PayTabs): PayTabs response using KKUx soap

    Returns:
        unicode: The rendered HTML.

    """
    payment_support_email = configuration_helpers.get_value('payment_support_email', settings.PAYMENT_SUPPORT_EMAIL)
    return _format_error_html(
        _(
            u"Sorry! Your payment could not be processed because an unexpected exception occurred. "
            u"Please contact us at {email} for assistance."
        ).format(email=payment_support_email)
    )


def _format_error_html(msg):
    """ Format an HTML error message """
    return u'<p class="error_msg">{msg}</p>'.format(msg=msg)

