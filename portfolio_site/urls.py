# portfolio_site/urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import home, contact_view, service_detail, portfolio_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact_view, name='contact'),
     path('services/<int:pk>/', service_detail, name='service_detail'),
    path('portfolio/<int:pk>/', portfolio_detail, name='portfolio_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)