from django.core.management import BaseCommand
from payment_app.models import Item


class Command(BaseCommand):
    help = f'Добавление 5 единиц товара Item'

    def handle(self, *args, **kwargs):
        for i in range(1, 6):
            Item.objects.create(name=f'Item {i}',
                                description=f'Description {i}',
                                price=200+(i*i))
        self.stdout.write('Таблица Item успешно заполнена')
