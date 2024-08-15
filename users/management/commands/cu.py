from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='finageeva.nina@mail.ru',
            first_name='user',
            last_name='user',
            is_superuser=False,
            is_staff=False,
            is_active=True

        )
        user.set_password('54321')
        user.save()
