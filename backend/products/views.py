from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """ when used with post request, this view creates products """
    """ when used with get request, this view list the products """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)

        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content == None:
            content = title

        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'


class ProductListAPIView(generics.ListAPIView):
    "Not being used on the app"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
