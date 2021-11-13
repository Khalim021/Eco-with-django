from datetime import datetime

import pytz
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


# Create your models here.


class CategoryModel(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class BrandModel(models.Model):
    title = models.CharField(max_length=75, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brand')


class ProductTagModel(models.Model):
    title = models.CharField(max_length=85, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('product tag')
        verbose_name_plural = _('product tags')


class SizeModel(models.Model):
    title = models.CharField(max_length=3, verbose_name=_('size'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _('sizes')


class ColorModel(models.Model):
    code = models.CharField(max_length=13, verbose_name=_('code'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class ProductModel(models.Model):
    title = models.CharField(max_length=512, verbose_name=_('title'))
    image = models.ImageField(upload_to='products', verbose_name=_('image'))
    price = models.FloatField(verbose_name=_('price'))
    real_price = models.FloatField(verbose_name=_('real_price', ), default=0)
    sizes = models.ManyToManyField(SizeModel, related_name='products')
    colors = models.ManyToManyField(ColorModel, related_name='products')
    wishlist = models.ManyToManyField(UserModel, related_name='wishlist')
    discount = models.PositiveIntegerField(default=0,
                                           validators=[
                                               MinValueValidator(0),
                                               MaxValueValidator(100)
                                           ], verbose_name=_('discount'))

    short_description = models.TextField(verbose_name=_('short_description'))
    long_description = RichTextUploadingField(verbose_name=_('long_description'))
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT,
                                 related_name='products', null=True, verbose_name=_('category'))

    brand = models.ForeignKey(BrandModel, on_delete=models.PROTECT,
                              related_name='products', null=True, verbose_name=_('brand'))

    tags = models.ManyToManyField(ProductTagModel, related_name='products', verbose_name=_('tags'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    @staticmethod
    def get_from_cart(request):
        cart = request.session.get('cart', [])
        return ProductModel.objects.filter(pk__in=cart)

    def is_discount(self):
        return self.discount != 0

    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return diff.days <= 5

    def get_related_products(self):
        return self.    category.products.exclude(pk=self.pk)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel,
                                related_name='images',
                                on_delete=models.CASCADE,
                                verbose_name=_('product')
                                )
    image = models.ImageField(upload_to='products', verbose_name=_('image'))

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _('product image')
        verbose_name_plural = _('product images')
