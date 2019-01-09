"""
Middleware that checks user standing for the purpose of keeping users with
disabled accounts from accessing the site.
"""
from django.conf import settings
from django.http import HttpResponseForbidden
from django.utils.translation import ugettext as _

from student.models import UserStanding,UserProfile
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


class UserStandingMiddleware(object):
    """
    Checks a user's standing on request. Returns a 403 if the user's
    status is 'disabled'.
    """
    def process_request(self, request):
        user = request.user
        try:
            user_account = UserStanding.objects.get(user=user.id)
            # because user is a unique field in UserStanding, there will either be
            # one or zero user_accounts associated with a UserStanding
        except UserStanding.DoesNotExist:
            pass
        else:
            if user_account.account_status == UserStanding.ACCOUNT_DISABLED:
                msg = _(
                    'Your account has been disabled. If you believe '
                    'this was done in error, please contact us at '
                    '{support_email}'
                ).format(
                    support_email=u'<a href="mailto:{address}?subject={subject_line}">{address}</a>'.format(
                        address=settings.DEFAULT_FEEDBACK_EMAIL,
                        subject_line=_('Disabled Account'),
                    ),
                )
                return HttpResponseForbidden(msg)



class UserDataMiddleware(object):
    # Added by Kava HD
    # Check User Details
    def process_request(self, request):
        user = request.user
        try:
            user_obj = UserProfile.objects.get(user=user.id)
            if user_obj.force_to_update == True:
                if request.path != '/account/settings' and request.path != '/api/user/v1/accounts/'+ str(user.username) and request.path != '/api/user/v1/preferences/'+str(user.username) and request.path !='/user_api/v1/preferences/time_zones/' and request.path !='/event' and request.path != '/user_api/v1/preferences/time_zones/?country_code='+ str(user_obj.country.code):
                    if not (user_obj.user.email and user_obj.name and user_obj.name_in_arabic and user_obj.gender and user_obj.country):
                        msg = _(
                            'Your account has been disabled. Please Update Your Details.'
                            '{support_link}'
                        ).format(
                            support_link=u'<a href="{address}">Click Here For Update Your Details</a>'.format(
                                address=reverse('account_settings'),
                            ),
                        )
                        return HttpResponseForbidden(msg)
        except UserProfile.DoesNotExist:
            pass
