from django.db import models
from django.utils.translation import gettext as _


class DOTAPriceBoost(models.Model):
    """
    Dota Цена на буст
    """

    mmr = models.IntegerField(verbose_name=_("Число рейтинга"))
    price = models.IntegerField(verbose_name=_("Цена 100 MMR"))

    class Meta:
        verbose_name = _("Dota Цена на буст")
        verbose_name_plural = _("Dota Цены на буст")
        ordering = ["mmr"]

    def __str__(self):
        return f"{self.mmr} - {self.price}"


