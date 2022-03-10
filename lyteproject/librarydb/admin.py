from django.contrib import admin
from .models import Author, Genre, Book, CustomerExtra, BorrowedBook
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date', 'genres']
    search_fields = ['title']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    search_fields = ['last_name', 'first_name']

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class CustomerExtraAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'branch')
    list_filter = ['enrollment', 'branch']


class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'borrowdate', 'expirydate')
    list_filter = ['enrollment', 'borrowdate', 'expirydate']



admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(CustomerExtra, CustomerExtraAdmin)
admin.site.register(BorrowedBook, BorrowedBookAdmin)