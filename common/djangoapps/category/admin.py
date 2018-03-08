"""Django admin interface for the course category models. """

from django.contrib import admin

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin for Course Subject.
    """
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)

