"""
URLs for EdxNotes.
"""
from django.conf.urls import url

from edxnotes import views

# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r"^$", views.edxnotes, name="edxnotes"),
    url(r"^notes/$", views.notes, name="notes"),
    url(r"^token/$", views.get_token, name="get_token"),
    url(r"^visibility/$", views.edxnotes_visibility, name="edxnotes_visibility"),
    url(r"^delete_user_data/$", views.gdpr_delete_all_notes_for_user, name="delete_user_data"),
]
