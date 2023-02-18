from django.views import View
from django.views.generic import DetailView
from django.http import JsonResponse
import os

from .models import Item
from .stripe_service import create_chechout_session_id


class CreateCheckoutSessionIdView(View):
    """Представление Session Id"""
    def get(self, request, *args, **kwargs):
        session_id = create_chechout_session_id(kwargs['pk'])
        return JsonResponse({
            'id': session_id
        })


class ItemDetailView(DetailView):
    """Детальное представление Item"""
    model = Item
    template_name = 'payment_app/checkout.html'
    context_object_name = 'item'
    
    def get_context_data(self, **kwargs):        
        context = super(ItemDetailView, self).get_context_data(**kwargs)

        STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
        context.update({
            'STRIPE_PUBLIC_KEY': STRIPE_PUBLIC_KEY
        })
        
        return context
