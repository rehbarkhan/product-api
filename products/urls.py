from django.urls import path
from products.views import index,search_product


urlpatterns = [
    path('product/<str:name>/',index,name='index'),
    path('search/',search_product,name='search')
]