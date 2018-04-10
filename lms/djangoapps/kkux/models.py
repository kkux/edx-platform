from django.db import models

from model_utils.models import TimeStampedModel


class Language(TimeStampedModel):
    name = models.CharField(max_length=50, default='English')
    code = models.CharField(max_length=10, unique=True, default='en')

    class Meta:
        app_label = "kkux"
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.__unicode__()


class News(TimeStampedModel):
    """
    Store KKUx news details and news will be displayed on homepage.
    """
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, help_text="News title upto 30 characters")
    link = models.URLField(help_text="Link for the news")
    short_description = models.TextField(null=True, blank=True, help_text="Add description upto 100 characters")
    position = models.IntegerField(default=1, help_text="Position/order of the news")

    class Meta(object):
        app_label = "kkux"
        ordering = ['position']
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __unicode__(self):
        return self.title

    def __repr__(self):
        return self.__unicode__()
