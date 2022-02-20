from apps.services.forms import CommentSaveForm
from apps.services.models import (
    AdditionalService,
    Comment,
    CSGOPriceBoost,
    DOTAPriceBoost,
    GameEnum,
)
from django.core import serializers
from django.views.generic import TemplateView
from django.views.generic.edit import FormView


class LandingView(FormView):
    """
    Лэндиннг сайта
    """

    form_class = CommentSaveForm
    template_name = "landing.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        """
        Контекст данных лэндинга
        """
        data = super().get_context_data(**kwargs)
        # CS: GO
        data["csgo_prices"] = CSGOPriceBoost.objects.all()
        data["csgo_prices_json"] = serializers.serialize(
            "json", CSGOPriceBoost.objects.all()
        )
        data["csgo_comments"] = Comment.objects.filter(
            is_published_landing=True, category=GameEnum.CSGO_CATEGORY
        )
        data["csgo_services"] = AdditionalService.objects.filter(
            category=GameEnum.CSGO_CATEGORY
        )
        # Dota 2
        data["dota_prices_json"] = serializers.serialize(
            "json", DOTAPriceBoost.objects.all()
        )
        data["dota_comments"] = Comment.objects.filter(
            is_published_landing=True, category=GameEnum.DOTA_CATEGORY
        )
        data["dota_services"] = AdditionalService.objects.filter(
            category=GameEnum.DOTA_CATEGORY
        )
        return data

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
