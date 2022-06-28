from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_treasures, name='treasures'),
    path('<int:treasure_id>/', views.full_details, name='full_details'),
    path('add/', views.add_treasure, name='add_treasure'),
]
