from django.db import models
from django.utils.translation import gettext as _


class News(models.Model):
    """
    Модель новостей
    """

    picture = models.ImageField(
        verbose_name=_("Картинка"), blank=True, null=True
    )
    title = models.CharField(
        verbose_name=_("Заголовок"), max_length=255, null=True
    )
    description = models.TextField(
        verbose_name=_("Краткое описание"), blank=True, null=True
    )
    content =  models.TextField(
        verbose_name=_("Содержание новости"), blank=True, null=True
    )
    is_published = models.BooleanField(
        verbose_name=_("Опубликовано"), default=False
    )
    is_published_landing = models.BooleanField(
        verbose_name=_("Опубликовано на главной странице"),
        default=False,
    )
    category_news = models.ForeignKey(
        'content.CategoryNews',
        verbose_name=_("Категория новости"),
        related_name='news',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    date = models.DateTimeField(verbose_name=_("Дата новости"),blank=True,null=True)
    date_created = models.DateTimeField(verbose_name=_("Дата создания"), auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=_("Дата последнего обновления"),auto_now=True)

    class Meta:
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")
        ordering = ["-date"]

    def __str__(self):
        title = "Без заголовка" if self.title is None else self.title
        return (
            f"'{title}' "
            + f"(дата создания: {self.date_created}, "
            + f"дата последнего редактирования: {self.date_updated})"
        )


