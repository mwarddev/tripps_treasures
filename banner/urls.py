from django.urls import path
from . import views

urlpatterns = [
    path('', views.update_banner, name='update_banner'),
]
