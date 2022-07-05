from django.urls import path
from . import views

urlpatterns = [
    path('', views.update_banner, name='update_banner'),
    path('', views.show_info, name='show_info'),
]
