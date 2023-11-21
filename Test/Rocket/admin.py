from django.contrib import admin
from .models import *
# Register your models here.
class AR_display(admin.ModelAdmin):
    list_display=['name']
admin.site.register(AR,AR_display)
class Batch_display(admin.ModelAdmin):
    list_display=['Batch']
admin.site.register(Batch,Batch_display)
class Student_display(admin.ModelAdmin):
    list_display=['Student']
admin.site.register(Student,Student_display)