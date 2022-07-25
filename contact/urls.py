from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('messages/', views.view_messages, name='view_messages'),
    path('delete/<int:message_id>/',
         views.delete_message,
         name='delete_message'),
]
