from django.contrib import admin
from .models import Person

# Register your models here.

@admin.register(Person)
class PersonTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','num','hobby')