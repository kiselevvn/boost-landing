from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Crate a admin command"

    def handle(self, *args, **options):

        if len(get_user_model().objects.filter(username="admin")) == 1:
            self.stdout.write(
                self.style.SUCCESS("admin account already exists")
            )
            return

        user = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@admin.com",
            password="admin",
        )
        user.save()
