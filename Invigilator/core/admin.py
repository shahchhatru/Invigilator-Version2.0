from django.contrib import admin
from .models import Invigilator
# Register your models here.

@admin.register(Invigilator)
class InvigilatorAdmin(admin.ModelAdmin):
    list_display=['staff_id','name','address','joined','department','position','qualification']
    
