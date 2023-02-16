from django.contrib import admin
from django.urls import path, include


from .views import CreateCheckoutSessionView, ItemDetailView

urlpatterns = [
    path('buy/<int:id>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('item/<int:id>/', ItemDetailView.as_view(), name='item'),
]
