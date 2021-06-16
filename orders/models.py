from django.contrib.auth import get_user_model
from django.db import models

from products.models import ProductModel

UserModel = get_user_model()


class OrderModel(models.Model):
    user = models.ForeignKey(UserModel, related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel, related_name='orders')
    price = models.FloatField(null=True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    country = models.CharField(max_length=30)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postcode = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.user.profile)}'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
