from django.urls import path
from . import views

urlpatterns = [
    path('treasures/', views.all_treasures, name='treasures'),
]
