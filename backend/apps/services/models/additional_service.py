from django.db import models
from django.utils.translation import gettext as _
from .game_enum import GameEnum


class AdditionalService(models.Model):
    """
    Дополнительная услуга
    """

    name = models.TextField(
        verbose_name=_("Описание услуги")
    )
    fixed_price = models.IntegerField(
        verbose_name=_("Фиксированная стоимость"),
        blank=True,
        null=True
    )
    percent_price = models.IntegerField(
        verbose_name=_("Процентная стоимость"),
        help_text=_("Имеет приоритет"),
        blank=True,
        null=True
    )
    category = models.IntegerField(
        verbose_name=_("Категория услуги"),
        choices=GameEnum.choices,
    )

    class Meta:
        verbose_name = _("Дополнительная услуга")
        verbose_name_plural = _("Дополнительные услуги")

    def __str__(self):
        return f"{self.name}"


