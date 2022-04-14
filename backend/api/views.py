from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


@api_view(["GET", "POST"])
def api_home(request):
    instance = Product.objects.all().order_by("?").first()
    data = ProductSerializer(instance).data
    return Response(data)
