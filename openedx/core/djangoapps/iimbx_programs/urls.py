from django.conf.urls import url
from .views import program_about, program_enroll, program_unenroll, program_demo, course_detail, register_applicant

urlpatterns = [
    url(r'^(?P<id>[-\w]+)/about$', program_about, name='program_about'),
    url(r'^(?P<slug>[-\w]+)/enroll$', program_enroll, name='program_enroll'),
    url(r'^unenroll/$', program_unenroll, name='program_unenroll'),
    url(r'^demo/$', program_demo, name='program_demo'),
    # url(r'^(?P<slug>[-\w]+)/demo$', program_demo, name='program_demo'),
    url(r'^course_detail/$', course_detail, name='course_detail'),
    url(r'^add_applicant/$', register_applicant, name='register_applicant')
]
