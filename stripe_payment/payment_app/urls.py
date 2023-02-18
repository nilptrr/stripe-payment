from django.contrib import admin
from django.urls import path


from .views import CreateCheckoutSessionIdView, ItemDetailView, SuccessView, CancelView

urlpatterns = [
    path('buy/<int:pk>/', CreateCheckoutSessionIdView.as_view(), name='buy'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel')
]
