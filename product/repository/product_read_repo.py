from ..models import Product
from ..serializer import ProductSerializer


def get_all_active_products():
    return Product.objects.all().filter(active=True)


def get_particular_product(pk):
    return Product.objects.get(pk=pk)


def all_products():
    products = get_all_active_products()
    data = ProductSerializer(products, many=True).data
    return data


def particular_product(pk):
    product = get_particular_product(pk)
    data = ProductSerializer(product).data
    return data
