from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


@admin.register(Book)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'isbn')


# @admin.register(BookInstance)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # list_display = ('author', 'date_of_birth', 'date_of_death')
    # pass


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')


# admin.site.register(Author)
# admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
admin.site.register(BookInstance)
