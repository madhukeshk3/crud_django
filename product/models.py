from django.contrib.postgres.fields import ArrayField
from django.db import models
import enum


# Create your models here.

class PackagingType(enum.Enum):
    Tin = 'tin'
    Packet = 'packet'
    Sachet = 'sachet'

    @classmethod
    def get_choices(cls):
        choices = []
        for item in cls:
            choices.append(tuple((item.value, item.name)))
        return choices


class Product(models.Model):
    name = models.CharField(max_length=100)
    extra_name = ArrayField(models.CharField(max_length=100))
    weight_info = models.CharField(max_length=100)
    packaging_info = models.CharField(max_length=100)
    packaging_type = models.CharField(choices=PackagingType.get_choices(), max_length=100)
    expired_on = models.DateField(null=True)
    is_frozen = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # @staticmethod
    # def get_all_active_products():
    #     return Product.objects.all().filter(active=True)
    #
    # @staticmethod
    # def get_particular_product(pk):
    #     return Product.objects.get(pk=pk)
