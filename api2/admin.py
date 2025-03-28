from django.contrib import admin
from .models import Student1

@admin.register(Student1)
class Student1Admin(admin.ModelAdmin):
    list_display=['id','name','city','roll']
