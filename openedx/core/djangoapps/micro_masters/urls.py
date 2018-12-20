from django.conf.urls import url
from .views import (
    program_about, program_postpay_callback,
    show_program_receipt, program_buy,
    use_code, reset_code_redemption,
    prorgam_user_certificate,
    program_info, program_enroll,
    program_unenroll
)
# from .program_reindex import index_programs_information, reindex_specific_program

urlpatterns = [
    url(r'^(?P<program_id>[0-9]+)/$', program_about, name='program_about'),
    url(r'^(?P<program_id>[0-9]+)/info$', program_info, name='program_info'),
    url(r'^(?P<program_id>[0-9]+)/enroll$', program_enroll, name='program_enroll'),
    url(r'^unenroll/$', program_unenroll, name='program_unenroll'),
    url(r'^receipt/(?P<ordernum>[0-9]+)/$', show_program_receipt),
    url(r'^buy/(?P<program_id>[0-9]+)/$', program_buy, name='program_buy'),
    # response from payment gateway for programs
    url(r'^program_postpay_callback/$', program_postpay_callback),  # Both the ~accept and ~reject callback pages are handled here
    url(r'^use_code/$', use_code),
    url(r'^reset_code_redemption/$', reset_code_redemption),

    # for reindex all programs
    # url(r'^reindex-all-programs/$', index_programs_information, name='reindex-all-programs'),
    # reindex only given program
    # url(r'^reindex-program/(?P<pk>[0-9]+)/$', reindex_specific_program, name='reindex-program'),

    # user program certificate
    url(
        r'^certificates/(?P<certificate_uuid>[0-9a-f]{32})/$',
        prorgam_user_certificate,
        name='prorgam_user_certificate'
    ),
]
