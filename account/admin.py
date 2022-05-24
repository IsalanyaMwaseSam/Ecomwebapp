from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = 'SamTech Dashboard'
admin.site.register(Account)