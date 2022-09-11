from django.contrib import admin
from .models import Files
from home.models import ChangeControlLog


# Register your models here.
admin.site.register(Files)
admin.site.register(ChangeControlLog)
