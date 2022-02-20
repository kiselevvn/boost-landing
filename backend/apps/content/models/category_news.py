from django.db import models
from django.utils.translation import gettext as _


class CategoryNews(models.Model):
    """
    Модель категории новостей
    """

    name = models.CharField(
        verbose_name=_("Наименование"), max_length=255, null=True
    )
    description = models.TextField(
        verbose_name=_("Краткое описание"), blank=True, null=True
    )
    is_published = models.BooleanField(
        verbose_name=_("Категория опубликована"), default=False
    )
    date_created = models.DateTimeField(verbose_name=_("Дата создания"),auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=_("Дата последнего обновления"),auto_now=True)

    class Meta:
        verbose_name = _("Категория новостей")
        verbose_name_plural = _("Категории новостей")
        ordering = ["-date_created"]

    def __str__(self):
        name = "Категория без наименования" if self.name is None else self.name
        return f"{name}"


