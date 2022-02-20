from django.urls import path

from .views import CommentSaveView

urlpatterns = [
    path("comment-save/", CommentSaveView.as_view(), name="comment-save"),
]
