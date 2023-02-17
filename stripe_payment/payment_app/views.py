from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .stripe_service import create_chechout_session_id


class CreateCheckoutSessionIdView(View):
    """Представление Session Id"""
    def get(self, request, *args, **kwargs):
        session_id = create_chechout_session_id(kwargs['id'])
        return JsonResponse({
            'id': session_id
        })


class ItemDetailView(View):
    """Детальное представление Item"""
    
