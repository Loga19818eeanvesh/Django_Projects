
from ast import Add
from csv import list_dialects
from django.contrib import admin

# Register your models here.

from .models import Book, Author, Address, Country

class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)
    prepopulated_fields = {'slug' : ('title',)}
    list_filter = ('rating', 'author')
    list_display = ('title', 'author', 'rating')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'postal_code', 'city')
    list_filter = ('city',)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', )
    list_filter = ('name',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Country,CountryAdmin)