import re
from uuid import uuid4
from util.json_request import JsonResponse

from django.utils.translation import ugettext as _

from edxmako.shortcuts import render_to_response

from .models import Subscribers
from kkux.tasks import send_subcription_activation_mail
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from openedx.core.djangoapps.user_api.accounts.api import update_account_settings
from openedx.core.djangoapps.user_api.preferences.api import update_user_preferences
from django.core.validators import ValidationError, validate_email
from alphabet_detector import AlphabetDetector


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



def monshaat(request):
    try:
        from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
        courses = CourseOverview.objects.filter(course_category='monshaat')
    except Exception:
        courses = ''
    return render_to_response('monshaat.html', {'courses':courses})


def student_data(request):
    """
    Added by kava hd
    this function handle Account page student data and vallidate that data.
    save into student datebase.
    """
    old_email = request.user.email
    update_1 = {'gender':request.POST.get('gender'),
                'country': request.POST.get('country'),
                'level_of_education':request.POST.get('education'),
                'year_of_birth':request.POST.get('year'),
                'language_proficiencies':[{'code':request.POST.get('pre_language')}]
        }
     # {u'language_proficiencies': [{u'code': u'km'}]}
    ad = AlphabetDetector()
    if not ad.only_alphabet_chars(request.POST.get('name'), "LATIN"):
        return JsonResponse(status=401)
    update_1['name'] = request.POST.get('name')

    if not ad.only_alphabet_chars(request.POST.get('name_in_arabic'), 'ARABIC'):
        return JsonResponse(status=402) 
    update_1['name_in_arabic'] = request.POST.get('name_in_arabic')

    if request.POST.get('email') and old_email != request.POST.get('email'):
        if User.objects.filter(email=request.POST.get('email')).count() != 0:
            return JsonResponse(status=404)
        try:
            validate_email(request.POST.get('email'))
            update_1['email'] = request.POST.get('email')
        except ValidationError:
            response = JsonResponse(status=403)
            return response
        update_1['email'] = request.POST.get('email')
    # student_views.validate_new_email(existing_user, new_email)
    update_account_settings(request.user,update_1)
    update_2 = {'time_zone':request.POST.get('time_zone') if request.POST.get('time_zone') else None , 'pref-lang':request.POST.get('language') }
    if request.POST.get('time_zone'):
        update_2['time_zone'] = request.POST.get('time_zone')
    update_user_preferences(request.user,update_2)
    return JsonResponse(status=200)

