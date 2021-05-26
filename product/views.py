from django.views.decorators.csrf import csrf_exempt
from . import services


# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'GET':
        return services.product_retrieve.product_retrieve()
    elif request.method == 'POST':
        return services.product_creation.product_creation(request)


@csrf_exempt
def particular(request, pk=0):
    if request.method == 'GET':
        return services.product_retrieve.particular_product_retrieve(pk)
    elif request.method == 'PUT':
        return services.product_update.data_update(request, pk)
