from django.core.management.base import BaseCommand
from extra_settings.models import Setting

import tqdm

class Command(BaseCommand):
    help = "init extra settings site"

    EXTRA_SETTINGS = [
        {},
        {}
    ]

    def handle(self, *args, **options):
        print("")
