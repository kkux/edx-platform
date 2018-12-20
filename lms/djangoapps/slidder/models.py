from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from openedx.core.djangoapps.xmodule_django.models import CourseKeyField



class indexslidder(models.Model):
	# course = CourseKeyField(db_index=True, primary_key=True, max_length=255)
	title_in_english =  models.CharField(max_length=300)
	title_in_arabic =  models.CharField(max_length=300)
	description_in_english = models.CharField(max_length=800)
	description_in_arabic = models.CharField(max_length=800)
	arabic_image = models.ImageField(upload_to="media")
	english_image = models.ImageField(upload_to="media")
	button_text_in_english = models.CharField(max_length=30)
	button_text_in_arabic = models.CharField(max_length=30)
	link = models.CharField(max_length=800,null=True,blank=True)

