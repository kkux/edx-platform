"""
Django models for course Category.
"""
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    """
    Model for storing course subject.
    """
    name = models.CharField(max_length=255, unique=True, verbose_name='Category Name')

    class Meta(object):
        app_label = "category"
        verbose_name = 'Course Category'
        verbose_name_plural = 'Course Category'

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.__unicode__()

