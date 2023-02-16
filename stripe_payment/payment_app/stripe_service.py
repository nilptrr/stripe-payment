import stripe
from .models import Item

API_KEY = 'sk_test_51MaGPSLi7UmMpAciemZZAalHC13fnQZPCNusK2q1Pw4Mm16t6TQecNpENe7gFnDgSxFOrvLXyF4AuOgLiO7yGUaT00uvyQ4kRv'
# TODO вынести API_KET в ENV

def create_chechout_session_id(item_id: int):
    item = Item.objects.get(pk=item_id)
    stripe.api_key = API_KEY
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
