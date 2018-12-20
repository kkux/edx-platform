from .models import ProgramApplicant
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.utils.translation import ugettext_noop

class ProgramApplicantForm(forms.ModelForm):
    # username = forms.CharField(label=_('username'), max_length=30,
    #     help_text=_('Required. 30 characters or fewer. Letters, digits and '
    #                 '@/./+/-/_ only.'),
    #     validators=[
    #         validators.RegexValidator(r'^[\w.@+-]+$',
    #                                   _('Enter a valid username. '
    #                                     'This value may contain only letters, numbers '
    #                                     'and @/./+/-/_ characters.'), 'invalid'),
    #     ],
    #     error_messages={
    #         'unique': "A user with that username already exists.",
    #     })
    # first_name = forms.CharField(label=_('first name'), max_length=30)
    # last_name = forms.CharField(label=_('last name'), max_length=30)
    # email = forms.EmailField(label=_('email address'), )
    # mobile = forms.CharField(label=_('mobile number'), max_length=20)
    # year_of_birth = forms.CharField(max_length=128)
    # # GENDER_CHOICES = (
    # #     ('m', ugettext_noop('Male')),
    # #     ('f', ugettext_noop('Female')),
    # #     # Translators: 'Other' refers to the student's gender
    # #     ('o', ugettext_noop('Other/Prefer Not to Say'))
    # # )
    # gender = forms.CharField(
    #      max_length=6
    # )
    # postal_address = forms.CharField(widget=forms.Textarea)
    # level_of_education = forms.CharField(max_length=128)
    # discipline_or_stream = forms.CharField(max_length=128)
    # degree = forms.CharField(max_length=128)
    # percentage = forms.CharField(max_length=12)
    # educational_institute = forms.CharField(max_length=128)
    # referencer = forms.CharField(widget=forms.Textarea)
    # expectation = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ProgramApplicant
        fields = '__all__'