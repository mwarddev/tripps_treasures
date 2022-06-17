from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket_view, name='basket_view'),
    path('add/<int:treasure_id>/', views.add_to_basket, name='add_to_basket'),
]
