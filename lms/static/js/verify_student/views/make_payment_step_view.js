/**
 * View for the "make payment" step of the payment/verification flow.
 */
var edx = edx || {};

(function($, _, gettext, interpolate_text) {
    'use strict';

    edx.verify_student = edx.verify_student || {};

    edx.verify_student.MakePaymentStepView = edx.verify_student.StepView.extend({

        templateName: 'make_payment_step',
        btnClass: 'action-primary',

        initialize: function(obj) {
            _.extend(this, obj);
            if (this.templateContext().isABTesting) {
                this.templateName = 'make_payment_step_ab_testing';
                this.btnClass = 'action-primary-blue';
            }
        },

        defaultContext: function() {
            return {
                isActive: true,
                suggestedPrices: [],
                minPrice: 0,
                sku: '',
                currency: 'usd',
                upgrade: false,
                verificationDeadline: '',
                userTimezone: 'UTC',
                userLanguage: 'en-US',
                courseName: '',
                requirements: {},
                hasVisibleReqs: false,
                platformName: '',
                alreadyVerified: false,
                courseModeSlug: 'audit',
                verificationGoodUntil: '',
                isABTesting: false,
                userEmail: ''
            };
        },

        _getProductText: function(modeSlug, isUpgrade) {
            switch (modeSlug) {
            case 'professional':
                return gettext('Professional Education Verified Certificate');
            case 'no-id-professional':
                return gettext('Professional Education');
            default:
                if (isUpgrade) {
                    return gettext('Verified Certificate upgrade');
                } else {
                    return gettext('Verified Certificate');
                }
            }
        },

        _getPaymentButtonText: function(processorName) {
            if (processorName.toLowerCase().substr(0, 11) == 'cybersource') {
                return gettext('Checkout');
            } else if (processorName.toLowerCase() == 'paypal') {
                return gettext('Checkout with PayPal');
            } else {
                // This is mainly for testing as no other processors are supported right now.
                // Translators: 'processor' is the name of a third-party payment processing vendor (example: "PayPal")
                return interpolate_text(gettext('Checkout with {processor}'), {processor: processorName});
            }
        },

        _getPaymentButtonHtml: function(processorName) {
            var self = this;
            return _.template(
                '<button class="next <%- btnClass %> payment-button" id="<%- name %>" ><%- text %></button> '
            )({name: processorName, text: self._getPaymentButtonText(processorName), btnClass: this.btnClass});
        },

        postRender: function() {
            var templateContext = this.templateContext(),
                hasVisibleReqs = _.some(
                    templateContext.requirements,
                    function(isVisible) { return isVisible; }
                ),
                // This a hack to appease /lms/static/js/spec/verify_student/pay_and_verify_view_spec.js,
                // which does not load an actual template context.
                processors = templateContext.processors || [],
                self = this;

            // Track a virtual pageview, for easy funnel reconstruction.
            window.analytics.page('payment', this.templateName);

            // The contribution section is hidden by default
            // Display it if the user hasn't already selected an amount
            // or is upgrading.
            // In the short-term, we're also displaying this if there
            // are no requirements (e.g. the user already verified).
            // Otherwise, there's absolutely nothing to do on this page.
            // In the future, we'll likely skip directly to payment
            // from the track selection page if this happens.
            if (templateContext.upgrade || !templateContext.contributionAmount || !hasVisibleReqs) {
                $('.wrapper-task').removeClass('hidden').removeAttr('aria-hidden');
            }

            if (templateContext.suggestedPrices.length > 0) {
                // Enable the payment button once an amount is chosen
                $('input[name="contribution"]').on('click', _.bind(this.setPaymentEnabled, this));
            } else {
                // If there is only one payment option, then the user isn't shown
                // radio buttons, so we need to enable the radio button.
                this.setPaymentEnabled(true);
            }

            // render the name of the product being paid for
            $('div.payment-buttons span.product-name').append(
                self._getProductText(templateContext.courseModeSlug, templateContext.upgrade)
            );

            if (processors.length === 0) {
                // No payment processors are enabled at the moment, so show an error message
                this.errorModel.set({
                    errorTitle: gettext('All payment options are currently unavailable.'),
                    errorMsg: gettext('Try the transaction again in a few minutes.'),
                    shown: true
                });
            }
            else {
                // create a button for each payment processor
                _.each(processors.reverse(), function(processorName) {
                    $('div.payment-buttons').append(self._getPaymentButtonHtml(processorName));
                });
            }

            // Handle payment submission
            $('.payment-button').on('click', _.bind(this.createOrder, this));
            var paymentDetails = document.querySelector("#pay-and-verify-container");
            var phoneNumber = paymentDetails.dataset.userCountryCode + paymentDetails.dataset.userPhoneNumber;
            $("#phone").intlTelInput({
                nationalMode: false,
                separateDialCode: true,
                initialCountry: "auto",
                geoIpLookup: function(callback) {
                    $.get('https://ipinfo.io', function() {}, "jsonp").always(function(resp) {
                        var countryCode = (resp && resp.country) ? resp.country : "";
                        callback(countryCode);
                    });
                },
                utilsScript: $('input[name="country_utils"]').val(),
            });
            $("#phone").intlTelInput("setNumber", phoneNumber);

        },

        setPaymentEnabled: function(isEnabled) {
            if (_.isUndefined(isEnabled)) {
                isEnabled = true;
            }
            $('.payment-button')
                .toggleClass('is-disabled', !isEnabled)
                .prop('disabled', !isEnabled)
                .attr('aria-disabled', !isEnabled);
        },

        // This function invokes the create_order endpoint.  It will either create an order in
        // the lms' shoppingcart or a basket in Otto, depending on which backend the request course
        // mode is configured to use.  In either case, the checkout process will be triggered,
        // and the expected response will consist of an appropriate payment processor endpoint for
        // redirection, along with parameters to be passed along in the request.
        createOrder: function(event) {

            var is_valid_email = true;
            var cc_first_name = $('input[name="cc_first_name"]').val();
            var cc_last_name = $('input[name="cc_last_name"]').val();
            var country_code = '+'
            var billing_address = $('input[name="billing_address"]').val();
            var city = $('input[name="city"]').val();
            var postal_code = $('input[name="postal_code"]').val();

            var phone_number = $("#phone").intlTelInput("getNumber");
            country_code = country_code + $("#phone").intlTelInput("getSelectedCountryData").dialCode;
            phone_number = phone_number.replace(country_code, "");

            if (! cc_first_name){
                $('span#error_first_name').html('Please enter your first name');
                $('input[name="cc_first_name"]').addClass('error');
                is_valid_email = false;
            } else {
                $('input[name="cc_first_name"]').removeClass('error');
                $('span#error_first_name').html('');
            }
            if (! cc_last_name){
                $('span#error_last_name').html('Please enter your last name');
                $('input[name="cc_last_name"]').addClass('error');
                is_valid_email = false;
            } else {
                $('input[name="cc_last_name"]').removeClass('error');
                $('span#error_last_name').html('');
            }
            if (! phone_number){
                $('span#error_phone_number').html('Please enter phone number');
                $('input[name="phone_number"]').addClass('error');
                is_valid_email = false;
            } else {
                $('input[name="phone_number"]').removeClass('error');
                $('span#error_phone_number').html('');
            }
            if (! billing_address){
                $('span#error_billing_address').html('Please enter billing address');
                $('input[name="billing_address"]').addClass('error');
                is_valid_email = false;
            } else {
                $('input[name="billing_address"]').removeClass('error');
                $('span#error_billing_address').html('');
            }
            if (! city){
                $('span#error_city').html('Please enter city');
                $('input[name="city"]').addClass('error');
                is_valid_email = false;
            } else {
                $('input[name="city"]').removeClass('error');
                $('span#error_city').html('');
            }
            if (! postal_code){
                $('span#error_postal_code').html('Please enter postal code');
                $('input[name="postal_code"]').addClass('error');
                is_valid_email = false;
            } else {
                $('input[name="postal_code"]').removeClass('error');
                $('span#error_postal_code').html('');
            }
            if (!is_valid_email) {
                return false;
            }
            event.preventDefault();
            var paymentAmount = this.getPaymentAmount(),
                postData = {
                    'processor': event.target.id,
                    'contribution': paymentAmount,
                    'course_id': this.stepData.courseKey,
                    'sku': this.templateContext().sku,
                    'cc_first_name': cc_first_name,
                    'cc_last_name': cc_last_name,
                    'country_code': country_code,
                    'phone_number': phone_number,
                    'billing_address': billing_address,
                    'city': city,
                    'postal_code': postal_code
                };

            // Disable the payment button to prevent multiple submissions
            this.setPaymentEnabled(false);

            $(event.target).toggleClass('is-selected');

            // Create the order for the amount
            $.ajax({
                url: '/verify_student/create_order/',
                type: 'POST',
                headers: {
                    'X-CSRFToken': $.cookie('csrftoken')
                },
                data: postData,
                context: this,
                success: this.handleCreateOrderResponse,
                error: this.handleCreateOrderError
            });
        },

        handleCreateOrderResponse: function(paymentData) {
            // At this point, the basket has been created on the server,
            // and we've received signed payment parameters.
            // We need to dynamically construct a form using
            // these parameters, then submit it to the payment processor.
            // This will send the user to an externally-hosted page
            // where she can proceed with payment.
            if (paymentData.payment_processor_name == 'PayTabs') {
                window.location.href = paymentData.payment_page_url;
            } else{
                var form = $('#payment-processor-form');

                $('input', form).remove();

                form.attr('action', paymentData.payment_page_url);
                form.attr('method', 'POST');

                _.each(paymentData.payment_form_data, function(value, key) {
                    $('<input>').attr({
                        type: 'hidden',
                        name: key,
                        value: value
                    }).appendTo(form);
                });

                // Marketing needs a way to tell the difference between users
                // leaving for the payment processor and users dropping off on
                // this page. A virtual pageview can be used to do this.
                window.analytics.page('payment', 'payment_processor_step');

                this.submitForm(form);
            }
        },

        handleCreateOrderError: function(xhr) {
            var errorMsg = gettext('An error has occurred. Please try again.');

            if (xhr.status === 400) {
                errorMsg = xhr.responseText;
            }

            this.errorModel.set({
                errorTitle: gettext('Could not submit order'),
                errorMsg: errorMsg,
                shown: true
            });

            // Re-enable the button so the user can re-try
            this.setPaymentEnabled(true);

            $('.payment-button').toggleClass('is-selected', false);
        },

        getPaymentAmount: function() {
            var contributionInput = $('input[name="contribution"]:checked', this.el),
                amount = null;

            if (contributionInput.attr('id') === 'contribution-other') {
                amount = $('input[name="contribution-other-amt"]', this.el).val();
            } else {
                amount = contributionInput.val();
            }

            // If no suggested prices are available, then the user does not
            // get the option to select a price.  Default to the minimum.
            if (!amount) {
                amount = this.templateContext().minPrice;
            }

            return amount;
        },

        selectPaymentAmount: function(amount) {
            var amountFloat = parseFloat(amount),
                foundPrice,
                sel;

            // Check if we have a suggested price that matches the amount
            foundPrice = _.find(
                this.stepData.suggestedPrices,
                function(price) {
                    return parseFloat(price) === amountFloat;
                }
            );

            // If we've found an option for the price, select it.
            if (foundPrice) {
                sel = _.sprintf('input[name="contribution"][value="%s"]', foundPrice);
                $(sel).prop('checked', true);
            } else {
                // Otherwise, enter the value into the text box
                $('#contribution-other-amt', this.el).val(amount);
                $('#contribution-other', this.el).prop('checked', true);
            }

            // In either case, enable the payment button
            this.setPaymentEnabled();

            return amount;
        },

        // Stubbed out in tests
        submitForm: function(form) {
            form.submit();
        }

    });
})(jQuery, _, gettext, interpolate_text);

