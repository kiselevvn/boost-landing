from django.db import models
from django.utils.translation import gettext as _


class QuestionAnswer(
    models.Model,
):
    """
    Модель секции Вопрос Ответ
    """

    question = models.TextField(verbose_name=_("Вопрос"))
    answer = models.TextField(verbose_name=_("Ответ"), blank=True, null=True)
    is_published_landing = models.BooleanField(
        verbose_name=_("Опубликовано на главной странице"),
        default=False,
    )
    date_created = models.DateTimeField(verbose_name=_("Дата создания"),auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=_("Дата последнего обновления"),auto_now=True)

    class Meta:
        verbose_name = _("Вопрос Ответ")
        verbose_name_plural = _("Вопросы и Ответы")
        ordering = ["-date_created"]

    def __str__(self):
        return (
            f"'{self.question}' "
            + f"(дата создания: {self.date_created}, "
            + f"дата последнего редактирования: {self.date_updated})"
        )
