from django.db import models
from django.utils.translation import gettext as _


class CSGOPriceBoost(models.Model):
    """
    СSGO Цена на буст
    """

    name = models.CharField(
        verbose_name=_("Наименование звания"), max_length=255
    )
    price = models.IntegerField(
        verbose_name=_("Цена")
    )
    order =  models.IntegerField(
        verbose_name=_("Порядковый номер звания")
    )

    class Meta:
        verbose_name = _("СSGO Цена на буст")
        verbose_name_plural = _("СSGO Цены на буст")
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} - {self.price} руб."


