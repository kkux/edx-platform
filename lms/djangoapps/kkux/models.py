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


class Subscribers(TimeStampedModel):
    """
    Stores subscribers email address
    """
    email = models.EmailField(max_length=255)
    activation_code = models.CharField(max_length=512)
    activated = models.BooleanField(default=False)

    class Meta(object):
        app_label = "kkux"
        verbose_name = "Subscribers"
        verbose_name_plural = "Subscribers"

    @classmethod
    def store_subscriber(cls, email, activation_code):
        try:
            sub, _ = cls.objects.get_or_create(email=email)
            sub.activation_code = activation_code
            sub.save()
            return sub
        except Exception as error:
            return None

    @classmethod
    def get_subscriber(cls, email):
        try:
            return cls.objects.get(email=email)
        except cls.DoesNotExist:
            return None

    @classmethod
    def update_subscription(cls, activation_code):
        try:
            sub = cls.objects.get(activation_code=activation_code)
            if sub.activated:
                return {
                    'activated': False
                }
            sub.activated = True
            sub.save()
            return {
                'activated': True
            }
        except cls.DoesNotExist:
            return None
