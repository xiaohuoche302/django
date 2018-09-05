from django.contrib import admin
from .models import Person,BankCard,Class,Student,Author,Book
# Register your models here.

# admin.site.register(BankCard)
# admin.site.register(Person)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','bankcard')

@admin.register(BankCard)
class BankCardAdmin(admin.ModelAdmin):
    list_display = ('id','num','bank_name')

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id','class_name','boy_num','girl_num')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','gender','age','klass')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title')