from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ..repository import product_write_repo


@csrf_exempt
def product_creation(request):
    bo = product_write_repo.create_new_product(request)
    if bo is None:
        HttpResponse(status=400)
    return JsonResponse(bo, status=201)
