from django.db import models
from django.utils.translation import gettext as _


class GameEnum(models.IntegerChoices):
    """
    Игры перечисление
    """

    DOTA_CATEGORY = 1, "Dota 2"
    CSGO_CATEGORY = 2, "CSGO"
