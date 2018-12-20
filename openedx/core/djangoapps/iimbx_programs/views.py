
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse

from edxmako.shortcuts import render_to_response
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from student.models import CourseEnrollment
from .models import Program, ProgramEnrollment
from courseware.courses import (
    get_permission_for_course_about,
    get_course_with_access,
    get_course_about_section
)
from django.core.cache import cache
from django.core.management import BaseCommand

from openedx.core.djangoapps.catalog.cache import (
    PROGRAM_CACHE_KEY_TPL,
    PROGRAM_UUIDS_CACHE_KEY,
    SITE_PROGRAM_UUIDS_CACHE_KEY_TPL
)
# from courseware.views.views import get_courses_info


def get_courses_and_enrollments(request, user, program):
    context = {}
    courses = []
    course_ids = []

    for course_obj in program.courses.select_related():
        overview = CourseOverview.get_from_id(course_obj.course_key)
        courses += [overview]
        course_ids += [str(course_obj.course_key)]
    # context = get_courses_info(request, course_ids)

    context['courses'] = courses
    return context


def program_about(request, id):
    # import pdb;
    # pdb.set_trace()
    user = request.user
    program = get_object_or_404(Program, id = id)
    context = get_courses_and_enrollments(request, user, program)
    user_is_enrolled = False
    if user.is_authenticated():
        user_is_enrolled = ProgramEnrollment.is_enrolled(user, program.id)
        if user_is_enrolled:
            user_is_enrolled = True

    context['program'] = program
    context['user_is_enrolled'] = user_is_enrolled

    return render_to_response('courseware/program_marketing.html', context)


@login_required
def program_enroll(request, slug):
    """
    Enroll the program without any restriction
    """
    user = request.user
    try:
        program = Program.objects.get(slug=slug)
    except Exception:
        raise Http404('Program not found!')

    ProgramEnrollment.enroll(user, program.id)
    dashboard = reverse('dashboard') + '?active=program'
    return HttpResponseRedirect(dashboard)


@login_required
def program_unenroll(request):
    """
    Unenroll the program
    """
    user = request.user
    program_id = request.POST.get('program_id', '')
    try:
        program = Program.objects.get(pk=program_id)
    except Exception:
        raise Http404('Program not found!')

    ProgramEnrollment.unenroll(user, program.id)
    return HttpResponse()



def program_demo(request):
    # user = request.user
    # program = get_object_or_404(Program, slug=slug)
    # context = get_courses_and_enrollments(request, user, program)
    # user_is_enrolled = False
    # if user.is_authenticated():
    #     user_is_enrolled = ProgramEnrollment.is_enrolled(user, program.id)
    #     if user_is_enrolled:
    #         user_is_enrolled = True

    # context['program'] = program
    # context['user_is_enrolled'] = user_is_enrolled

    return render_to_response('iimbx_programs/program_demo.html')


def course_detail(request):
    # user = request.user
    # program = get_object_or_404(Program, slug=slug)
    # context = get_courses_and_enrollments(request, user, program)
    # user_is_enrolled = False
    # if user.is_authenticated():
    #     user_is_enrolled = ProgramEnrollment.is_enrolled(user, program.id)
    #     if user_is_enrolled:
    #         user_is_enrolled = True

    # context['program'] = program
    # context['user_is_enrolled'] = user_is_enrolled

    return render_to_response('iimbx_programs/course_detail.html')

def register_applicant(request):
    from .forms import ProgramApplicantForm
    if request.method == 'POST':
        form = ProgramApplicantForm(request.POST)
        if form.is_valid():
            # applicant_form=form.save(commit=False)
            # applicant_form.username=request.POST['username']
            # applicant_form.first_name=request.POST['first_name']
            # applicant_form.last_name=request.POST['last_name']
            # applicant_form.degree=request.POST['degree']
            # applicant_form.expectation=request.POST['expectation']
            
            # applicant_form.save()
            form.save()
    

def programs_list(request):
    # import pdb;pdb.set_trace()
    # program_id=cache.get(PROGRAM_UUIDS_CACHE_KEY)
    # program_list = []
    # for uuid in program_id:
    #     program = cache.get(PROGRAM_CACHE_KEY_TPL.format(uuid=uuid))
    #     program_list.append({"uuid":program.get('uuid'),"title":program.get("title"),"type":program.get("type"),
    #         "banner_url": program.get('banner_image').get("small")})
    programs = Program.objects.all()
    return render_to_response("iimbx_programs/program_list.html",{"programs":programs})
