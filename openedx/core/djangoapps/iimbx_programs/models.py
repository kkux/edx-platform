from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.models import TimeStampedModel
from openedx.core.djangoapps.xmodule_django.models import CourseKeyField
# from student.models import CourseEnrollment
import student.models 
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from datetime import datetime
from pytz import UTC
from django.utils.translation import ugettext_noop




class Courses(TimeStampedModel):
    """
    Model for storing course id and name.
    """
    course_key = CourseKeyField(max_length=255)
    display_name = models.CharField(max_length=200)

    class Meta:
        app_label = 'iimbx_programs'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        unique_together = (('course_key', 'display_name'),)

    @classmethod
    def create_or_update_from_course_overview(cls, course_overview):
        title = course_overview.display_name
        course_key = course_overview.id
        try:
            course = cls.objects.get(course_key=course_key)
            course.display_name = title
            course.save()
        except cls.DoesNotExist:
            cls.objects.create(
                course_key=course_key,
                display_name=title
            )

    def __unicode__(self):
        return str(self.course_key)

    def __repr__(self):
        return self.__unicode__()


class ProgramCategory(TimeStampedModel):
    name = models.CharField(max_length=240, unique=True)
    position = models.IntegerField(help_text='Higher priority a smaller number')

    class Meta:
        app_label = 'iimbx_programs'
        verbose_name = 'Program Category'
        verbose_name_plural = 'Program Category'

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.__unicode__()


class ExpectedLearningItem(TimeStampedModel):
    """ ExpectedLearningItem model. """
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value



class Program(TimeStampedModel):
    name = models.CharField(max_length=240)
    slug = models.SlugField(
       max_length=200,
       unique=True,
       help_text="This is part of program URL, so no spaces or special characters are allowed"
    )
    program_category = models.ForeignKey(ProgramCategory, on_delete=models.CASCADE)
    short_description = models.TextField(
        max_length=150,
        help_text="Appears on the program mega menu. Limit to ~150 characters"
    )
    image = models.ImageField(upload_to="media")
    long_description = models.TextField(
        max_length=500,
        help_text="Appears on the program about page. Limit to ~500 characters"
    )
    courses = models.ManyToManyField(Courses)
    active = models.BooleanField(default=1)
    brochure = models.FileField(upload_to="media", null=True, blank=True)

    weeks_to_complete = models.PositiveSmallIntegerField(
        null=True, blank=True,
        help_text=_('Estimated number of weeks needed to complete a course run belonging to this program.'))

    start_date = models.DateField(default=None, null=True, blank=True)

    job_Outlook = models.TextField(
        blank=True, null=True, 
        help_text=_(
            u"Job Outlook"
        )
    )
    min_hours_effort_per_week = models.PositiveSmallIntegerField(null=True, blank=True)
    max_hours_effort_per_week = models.PositiveSmallIntegerField(null=True, blank=True)
    expected_learning = models.ManyToManyField(ExpectedLearningItem)
    fee = models.CharField(max_length=128)

    class Meta:
        app_label = 'iimbx_programs'
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.__unicode__()


class ProgramEnrollment(TimeStampedModel):
    """Storing Program Enrollment"""

    user = models.ForeignKey(User, related_name="user_iimbx",on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=0)

    class Meta:
        app_label = 'iimbx_programs'
        verbose_name = 'Program Enrollment'
        verbose_name_plural = 'Program Enrollment'

    @classmethod
    def is_enrolled(cls, user, program_id):
        if not user.is_authenticated():
            return False
        try:
            record = cls.objects.get(user=user, program__id=program_id)
            return record.is_active
        except cls.DoesNotExist:
            return False

    @classmethod
    def enroll(cls, user, program_id):
        try:
            program = Program.objects.get(pk=program_id)
        except:
            return False

        change_course_enrollment, _create = cls.objects.get_or_create(
            user=user,
            program=program
        )
        change_course_enrollment.is_active = True
        change_course_enrollment.save()

        for course in program.courses.select_related():
            CourseEnrollment.enroll(user, course.course_key)
        return True

    @classmethod
    def unenroll(cls, user, program_id):
        try:
            program = Program.objects.get(pk=program_id)
        except:
            return False

        for course in program.courses.select_related():
            CourseEnrollment.unenroll(user, course.course_key)
        change_course_enrollment = cls.objects.get(user=user, program=program)
        change_course_enrollment.is_active = False
        change_course_enrollment.save()

        return True


class ProgramCertificateSignatories(TimeStampedModel):
    """
    This table Certificate Signatories of programs
    """
    class Meta:
        app_label = 'iimbx_programs'
        verbose_name = 'Program Certificate Signatories'
        verbose_name_plural = 'Program Certificate Signatories'

    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=150,
        help_text='The name of this signatory as it should appear on certificates.'
    )
    title = models.CharField(
        max_length=100,
        help_text='Titles more than 100 characters may prevent students from printing their certificate on a single page.'
    )
    institution = models.TextField(
        max_length=150,
        help_text='The organization that this signatory belongs to, as it should appear on certificates.'
    )
    signature_image = models.ImageField()

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.__unicode__()

class ProgramReviewer(TimeStampedModel):
    """
    This table stores program reviewer's details and reviews content
    """
    program_page_content = models.ForeignKey(Program, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media", blank=True, null=True)
    name = models.CharField(max_length=150, blank=True)   
    review = models.TextField(
        blank=True, null=True, 
        help_text=_(
            u"Content in review_box"
        )
    )

class ProgramFeature(TimeStampedModel):
    """
    This table stores program's features
    """
    program_page_content = models.ForeignKey(Program, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media", blank=True, null=True)
    title = models.CharField(max_length=150, blank=True)   
    description = models.TextField(
        blank=True, null=True, 
        help_text=_(
            u"Content in program_feature"
        )
    )

class ProgramApplicant(TimeStampedModel):
    """
    This table stores applicant's information
    """
    username = models.CharField(_('username'), max_length=30, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        })
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    mobile = models.CharField(_('mobile number'), max_length=20, blank=True)
    this_year = datetime.now(UTC).year
    VALID_YEARS = range(this_year, this_year - 120, -1)
    year_of_birth = models.IntegerField(blank=True, null=True, db_index=True)
    GENDER_CHOICES = (
        ('m', ugettext_noop('Male')),
        ('f', ugettext_noop('Female')),
        # Translators: 'Other' refers to the student's gender
        ('o', ugettext_noop('Other/Prefer Not to Say'))
    )
    gender = models.CharField(
        blank=True, null=True, max_length=6, db_index=True, choices=GENDER_CHOICES
    )
    postal_address = models.TextField(blank=True, null=True)
    level_of_education = models.CharField(blank=True, max_length=128, db_index=True)
    discipline_or_stream = models.CharField(blank=True, max_length=128, db_index=True)
    degree = models.CharField(blank=True, max_length=128, db_index=True)
    percentage = models.CharField(blank=True, max_length=12, db_index=True)
    educational_institute = models.CharField(blank=True, max_length=128, db_index=True)
    referencer = models.TextField(blank=True, null=True)
    expectation = models.TextField(blank=True, null=True)

