from django.contrib import admin
from .models import News, Language, Subscribers, Testimonial


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    search_fields = ['name', 'code']

admin.site.register(Language, LanguageAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'position']
    list_filter = ['language']
    search_fields = ['title']

admin.site.register(News, NewsAdmin)


class SubscribersAdmin(admin.ModelAdmin):
    list_display = ['email']
    list_filter = ['created', 'activated']
    search_fields = ['email']


admin.site.register(Subscribers, SubscribersAdmin)
admin.site.register(Testimonial)

