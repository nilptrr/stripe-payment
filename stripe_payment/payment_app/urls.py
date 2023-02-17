from django.contrib import admin
from django.urls import path, include


from .views import CreateCheckoutSessionIdView, ItemDetailView

urlpatterns = [
    path('buy/<int:id>/', CreateCheckoutSessionIdView.as_view(), name='buy'),
    path('item/<int:id>/', ItemDetailView.as_view(), name='item'),
]
