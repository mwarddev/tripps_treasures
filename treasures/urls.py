from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_treasures, name='treasures'),
    path('<int:treasure_id>/', views.full_details, name='full_details'),
    path('add/', views.add_treasure, name='add_treasure'),
    path('edit/<int:treasure_id>/', views.edit_treasure, name='edit_treasure'),
    path('delete/<int:treasure_id>/', views.delete_treasure, name='delete_treasure'),
]
