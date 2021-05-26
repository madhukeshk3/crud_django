from .views import home, particular
from django.urls import path

urlpatterns = [
    path('product/', home),
    path('product/<int:pk>/', particular)
]
