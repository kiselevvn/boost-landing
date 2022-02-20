from apps.services.models import Comment
from django.forms import ModelForm


class CommentSaveForm(ModelForm):
    """
    Форма сохранения отзыва
    """

    class Meta:
        model = Comment
        fields = ["name", "text", "category"]
