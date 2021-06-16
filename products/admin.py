from django.contrib import admin

# Register your models here.
from modeltranslation.admin import TranslationAdmin

from products.forms import ColorModelForm
from products.models import CategoryModel, BrandModel, ProductTagModel, ProductModel, SizeModel, ColorModel, \
    ProductImageModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'created_at']
    search_fields = ['code']
    list_filter = ['created_at']
    form = ColorModelForm


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['created_at']


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'price', 'brand', 'category', 'discount']
    search_fields = ['title', 'price', 'discount', 'short_description']
    list_filter = ['created_at', 'brand', 'category']
    autocomplete_fields = ['category', 'tags', 'brand', 'colors', 'sizes']
    readonly_fields = ['real_price']
    inlines = [ProductImageStackedInline]
