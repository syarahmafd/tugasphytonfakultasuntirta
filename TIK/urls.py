from django.contrib import admin
from django.urls import path
from untirta.views import faperta, feb, fh, fisip, fk, fkip, ft, pascasarjana, untirta
urlpatterns = [
    path('admin/', admin.site.urls),
    path('faperta/', faperta),
    path('feb/', feb),
    path('fh/', fh),
    path('fisip/', fisip),
    path('fk/', fk),
    path('fkip/', fkip),
    path('ft/', ft),
    path('pascasarjana/', pascasarjana),
    path('untirta/', untirta),
]