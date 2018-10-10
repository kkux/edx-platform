import logging

from celery.task import task  # pylint: disable=no-name-in-module, import-error
from django.conf import settings
from django.core import mail

from edxmako.shortcuts import render_to_string

log = logging.getLogger('edx.celery.task')


@task(bind=True)
def send_subcription_activation_mail(self, to_address, activation_code):
    """
    Subscription Activation mail.
    """
    subject = 'Activate your subscription.'
    from_address = settings.DEFAULT_FROM_EMAIL
    context = {'activation_code': activation_code}
    message_body = render_to_string('emails/subscription_activation_mail.txt', context)
    try:
        mail.send_mail(subject, message_body, from_address, [to_address], fail_silently=False)
        log.info('Subscription Activation Email has been sent to User {user_email}'.format(
            user_email=to_address
        ))
    except Exception:  # pylint: disable=bare-except
        log.exception(
            'Unable to send subscribtion activation email to user from "%s" to "%s"',
            from_address,
            to_address,
            exc_info=True
        )
        raise Exception
