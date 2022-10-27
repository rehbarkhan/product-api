from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
from products.models import Product
# Create your views here.


@api_view(['GET'])
def index(request,name):
    if request.method == "GET":
        all_product = Product.objects.filter(product__icontains=name)
        product_json = ProductSerializer(all_product,many=True)
        return Response(product_json.data)
    else:
        return Response({"error":"only get reqeust is allowed"})

@api_view(["POST"])
def search_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name',None)
        if product_name:
            all_product = Product.objects.filter(product__icontains=product_name)[:5]
            product_json = ProductSerializer(all_product,many=True)
            return Response(product_json.data)
    if request.method == 'GET':
        return Response({'msg':
        'get'})
    return Response({'error':"something wetn wrong"})

