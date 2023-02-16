from django.contrib import admin
from django.urls import path, include


from .views import CreateCheckoutSessionView, ItemDetailView

urlpatterns = [
    path('buy/<int:id>', CreateCheckoutSessionView, name='buy'),
    path('item/<int:id>', ItemDetailView, name='item'),
]
