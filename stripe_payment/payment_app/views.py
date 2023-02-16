from django.shortcuts import render
from django.views import View

from .models import Item


class CreateCheckoutSessionView(View):
    """Возвращает Checkout Session ID"""


class ItemDetailView():
    """Детальное представление Item"""
