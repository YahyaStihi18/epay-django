from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Distributor)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Email)

