import re
from uuid import uuid4
from util.json_request import JsonResponse

from django.utils.translation import ugettext as _

from edxmako.shortcuts import render_to_response

from .models import Subscribers
from kkux.tasks import send_subcription_activation_mail

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

ALREADY_SUBCRIBED = _('You are already subscribed')
SUBSCRIPTION_MESSAGE = _('Please activate your subscription by clicking subcription link sent to your mail id.')
VALID_EMAIL = _('Please enter valid email address')
ERROR_MESSAGE = _('Sorry some error occurred.')


def subscribe(request):
    """
    Subscribes user to mailing list
    """
    email_id = request.POST.get('email_id')
    is_valid = re.search(EMAIL_REGEX, email_id)
    if is_valid:
        subscriber = Subscribers.get_subscriber(email_id)
        if subscriber:
            if subscriber.activated:
                return JsonResponse({'message': ALREADY_SUBCRIBED})
            send_subcription_activation_mail.delay(email_id, subscriber.activation_code)
            return JsonResponse({'message': SUBSCRIPTION_MESSAGE})
        activation_code = str(uuid4()).replace('-', '')
        sub = Subscribers.store_subscriber(email_id, activation_code)
        if sub:
            send_subcription_activation_mail.delay(email_id, sub.activation_code)
            return JsonResponse({'message': SUBSCRIPTION_MESSAGE})
        return JsonResponse({'message': ERROR_MESSAGE})
    return JsonResponse({'message': VALID_EMAIL})


def activate(request, activation_code):
    """
    Activate User subscription
    """
    sub = Subscribers.update_subscription(activation_code)
    context = dict()
    context['activated'] = sub.get('activated')
    return render_to_response('subscription_activation_status.html', context)

@staff_member_required
@login_required
def followup_update(request,update=None):
    
    from student.models import UserProfile
    user_obj_list=[]
    userprofile_obj = UserProfile.objects.all()
    for user_obj in userprofile_obj:
        if update == 'False':
            if not (user_obj.user.email and user_obj.name and user_obj.name_in_arabic and user_obj.gender and user_obj.country): 
                user_obj_list.append(user_obj)
        else:
            if (user_obj.user.email and user_obj.name and user_obj.name_in_arabic and user_obj.gender and user_obj.country): 
                user_obj_list.append(user_obj)
    page = request.GET.get('page', 1)
    paginator = Paginator(user_obj_list, 30)
    try:
        users_page = paginator.page(page)
    except PageNotAnInteger:
        users_page = paginator.page(1)
    except EmptyPage:
        users_page = paginator.page(paginator.num_pages)

   
    return render_to_response('followup_update.html', {'users_page':users_page,'update':update})
