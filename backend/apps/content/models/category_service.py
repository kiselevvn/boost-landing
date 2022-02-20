from django.db import models
from django.utils.translation import gettext as _


class CategoryService(
    models.Model,
):
    """
    Категория услуги
    """

    name = models.TextField(
        verbose_name=_("Категория услуги"),
    )
    is_published = models.BooleanField(
        verbose_name=_("Катеория услуг опубликована"), default=False
    )

    class Meta:
        verbose_name = _("Категория услуг")
        verbose_name_plural = _("Категории услуг")

    def __str__(self):
        return f"{self.name}"
