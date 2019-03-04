from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from openedx.core.djangoapps.xmodule_django.models import CourseKeyField
from django.conf import settings

class indexslidder(models.Model):
	# config = settings.VERIFY_STUDENT['SOFTWARE_SECURE']        
	# url=config['STORAGE_KWARGS']['custom_domain']+"/"+settings.AWS_STORAGE_BUCKET_NAME
        course = CourseKeyField(db_index=True, primary_key=True, max_length=255)
        title_in_english =  models.CharField(max_length=300)
        title_in_arabic =  models.CharField(max_length=300)
        description_in_english = models.CharField(max_length=800)
        description_in_arabic = models.CharField(max_length=800)
        arabic_image = models.ImageField()
        english_image = models.ImageField()
        button_text_in_english = models.CharField(max_length=30)
        button_text_in_arabic = models.CharField(max_length=30)
        link_arabic = models.CharField(max_length=800,null=True,blank=True)
        link_english = models.CharField(max_length=800,null=True,blank=True)

        def __unicode__(self):
                return self.title_in_english

