from django.urls import path
from . import views

urlpatterns = [
    path('treasures/', views.all_treasures, name='treasures'),
    path('<int:treasure_id>/', views.full_details, name='full_details'),
]
