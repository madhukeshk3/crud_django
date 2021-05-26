from ..serializer import ProductSerializer
from rest_framework.parsers import JSONParser
from ..models import Product


def get_particular_product(pk):
    return Product.objects.get(pk=pk)


def create_new_product(request):
    data = JSONParser().parse(request)
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return None


def update_product(request, pk):
    product = get_particular_product(pk)
    data = JSONParser().parse(request)
    serializer = ProductSerializer(product, data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return None
