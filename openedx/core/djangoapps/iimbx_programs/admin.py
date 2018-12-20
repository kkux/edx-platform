from django.contrib import admin

from .models import Program, ProgramCategory
from .models import (
    Program, ProgramCategory,
    ProgramCertificateSignatories, ProgramEnrollment,
    ProgramFeature, ProgramReviewer, ProgramApplicant,ExpectedLearningItem
)


class ProgramCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    search_fields = ['name']

    class Meta:
        verbose_name = "Program Category"
        verbose_name_plural = "Program Category"

admin.site.register(ProgramCategory, ProgramCategoryAdmin)

class ProgramEnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'program', 'is_active']
    list_filter = ['is_active']
    search_fields = ['program__name', 'user__username']
    class Meta:
        verbose_name = "Program Enrollment"
        verbose_name_plural = "Program Enrollment"
admin.site.register(ProgramEnrollment, ProgramEnrollmentAdmin)


class ProgramCertificateSignatoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'institution', 'program']
    list_filter = ['program__name']
    search_fields = ['name', 'title', 'institution']
    class Meta:
        verbose_name = "Program Certificate Signatories"
        verbose_name_plural = "Program Certificate Signatories"
admin.site.register(ProgramCertificateSignatories, ProgramCertificateSignatoriesAdmin)

class ProgramReviewerAdmin(admin.TabularInline):
    model = ProgramReviewer

class ProgramFeatureAdmin(admin.TabularInline):
    model = ProgramFeature  

class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'program_category', 'short_description', 'fee']
    list_filter = ['program_category__name']
    search_fields = ['name', 'program_category__name']
    filter_horizontal = ('courses','expected_learning')
    inlines = [
        ProgramReviewerAdmin, 
        ProgramFeatureAdmin        
    ]

    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programs"
admin.site.register(Program, ProgramAdmin)
  
class ProgramApplicantAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email']
    search_fields = ['username']

    class Meta:
        verbose_name = "Program Applicant"
        verbose_name_plural = "Program Applicants"

admin.site.register(ProgramApplicant, ProgramApplicantAdmin)
admin.site.register(ExpectedLearningItem)