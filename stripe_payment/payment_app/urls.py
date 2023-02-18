from django.contrib import admin
from django.urls import path, include


from .views import CreateCheckoutSessionIdView, ItemDetailView

urlpatterns = [
    path('buy/<int:pk>/', CreateCheckoutSessionIdView.as_view(), name='buy'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item'),
]
