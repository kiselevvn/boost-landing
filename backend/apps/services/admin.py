from django.contrib import admin
from .models import AdditionalService, CSGOPriceBoost, DOTAPriceBoost, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Новость в админке
    """

    list_display = (
        "name",
        "date_created",
        "is_published_landing",
    )
    list_filter = ("is_published_landing","category")


@admin.register(AdditionalService)
class AdditionalServiceAdmin(admin.ModelAdmin):
    """
    Регистрация дополнительных
    услуг в админке
    """

    list_display = (
        "name",
        "fixed_price",
        "percent_price",
    )
    list_filter = (
        "category",
    )


@admin.register(CSGOPriceBoost)
class CSGOPriceBoostAdmin(admin.ModelAdmin):
    """
    """

    list_display = (
        "name",
        "price",
        "order",
    )


@admin.register(DOTAPriceBoost)
class DOTAPriceBoostAdmin(admin.ModelAdmin):
    """
    """

    list_display = (
        "mmr",
        "price",
    )
