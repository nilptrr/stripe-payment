import os
import stripe
from .models import Item
from config import settings


def create_chechout_session_id(item_id: int) -> int:
    """Возвращает Checkout Sesson ID по item_id"""
    item = Item.objects.get(pk=item_id)
    stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
    YOUR_DOMAIN = 'http://127.0.0.1:8000'
    checkout_session = stripe.checkout.Session.create(
        line_items=[{
        'price_data': {
            'currency': 'usd',
            'product_data': {
                'name': item.name,
            },
            'unit_amount': item.price,
        },
        'quantity': 1,
        }],
        mode='payment',
        success_url= settings.DOMAIN + '/success/',
        cancel_url= settings.DOMAIN + '/cancel/',
    )
    
    return checkout_session.id
