"""tripps_treasures URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home_page.urls')),
    path('treasures/', include('treasures.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('user_account/', include('user_accounts.urls')),
    path('news_letter/', include('newsletter.urls')),
    path('banner/', include('banner.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'tripps_treasures.views.handler404'
