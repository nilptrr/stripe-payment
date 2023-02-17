import os
import stripe
from .models import Item


def create_chechout_session_id(item_id: int) -> int:
    """Возвращает Checkout Sesson ID по item_id"""
    item = Item.objects.get(pk=item_id)
    stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
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
        success_url='http://localhost:4242/success',
        cancel_url='http://localhost:4242/cancel',        
    )
    
    return checkout_session.id
