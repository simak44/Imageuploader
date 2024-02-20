from django.contrib import admin
from .models import myimage
# Register your models here.
@admin.register(myimage)
class imageadmin(admin.ModelAdmin):
    list_display =['id', 'photo', 'date']
    