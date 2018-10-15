from django.contrib import admin
from .models import Device, Client, Location
# Register your models here.

admin.site.register(Device)
admin.site.register(Location)
admin.site.register(Client)

