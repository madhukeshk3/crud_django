from ..repository import product_read_repo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def product_retrieve():
    bo = product_read_repo.all_products()
    return JsonResponse(bo, safe=False, status=200)


def particular_product_retrieve(pk):
    bo = product_read_repo.particular_product(pk)
    return JsonResponse(bo, safe=False, status=200)
