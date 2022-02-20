from apps.services.forms import CommentSaveForm
from django.views.generic.edit import FormView


class CommentSaveView(FormView):
    """
    Сохранение отзыва
    """

    http_method_names = ["post"]
    form_class = CommentSaveForm
    template_name = "apps/comment-save.html"
