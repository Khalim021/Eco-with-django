from django.contrib import admin

# Register your models here.
from modeltranslation.admin import TranslationAdmin

from posts.models import AuthorModel, TagModel, PostModel, CommentModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'avatar']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(PostModel)
class PostModelAdmin(TranslationAdmin):
    list_display = ['title', 'content', 'author']
    search_fields = ['title', 'content', 'author']
    list_filter = ['created_at', 'tags', 'author']
    autocomplete_fields = ['author', 'tags']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'created_at']
    search_fields = ['name', 'email']
    list_filter = ['created_at']








