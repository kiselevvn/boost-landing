from django.db import models
from django.utils.translation import gettext as _


class Service(models.Model):
    """
    Услуга
    """

    category_service = models.ForeignKey(
        "content.CategoryService",
        verbose_name=_("Категория услуги"),
        on_delete=models.CASCADE,
        related_name="services"
    )
    name = models.TextField(
        verbose_name=_("Услуга"),
    )
    is_published = models.BooleanField(
        verbose_name=_("Услуга опубликована"), default=False
    )

    class Meta:
        verbose_name = _("Услуга")
        verbose_name_plural = _("Услуги")

    def __str__(self):
        return f"{self.name}"
