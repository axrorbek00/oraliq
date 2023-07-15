from config.urls import path
from .views import countr_view, poytaxt_view

urlpatterns = [
    path('', countr_view, name='conuntr'),
    path('poytaxt/<int:pk>/', poytaxt_view, name='poytaxt')
]
