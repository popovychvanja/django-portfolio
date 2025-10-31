# portfolio/admin.py
from django.contrib import admin
from .models import Service, PortfolioItem, ContactMessage

admin.site.register(Service)
admin.site.register(PortfolioItem)
admin.site.register(ContactMessage)