from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ..repository import product_write_repo


@csrf_exempt
def data_update(request, pk):
    bo = product_write_repo.update_product(request, pk)
    if bo is None:
        return HttpResponse(400)
    return JsonResponse(bo, safe=False, status=201)
