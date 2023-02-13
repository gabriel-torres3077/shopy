from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from shopy_api.models import Product, Order
from shopy_api.serializers import ProductSerializer, OrderSerializer
from django.http import Http404


# Create your views here.
class ProductViewSet(APIView):
    # Remova o comentário abaixo para utilizar autenticação na api
    #permission_classes = [permissions.IsAuthenticated]

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request):
        ordering = request.GET.get('order')
        if ordering is not None:
            products = Product.objects.all().order_by(f'-{ordering}')
        else:
            products = Product.objects.all()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            serializer.save()
            print(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        order = self.get_object(pk)
        serializer = ProductSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk=pk)
        serializer = ProductSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        order = self.get_object(pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderViewSet(APIView):
    # Remova o comentário abaixo para utilizar autenticação na api
    #permission_classes = [permissions.IsAuthenticated]

    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get(self, request):
        ordering = request.GET.get('order')
        if ordering is not None:
            orders = Order.objects.all().order_by(f'-{ordering}')
        else:
            orders = Order.objects.all()
        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # adiciona o valor de todos os items ao preço total do pedido
            for product in serializer.validated_data['products']:
                serializer.validated_data['total'] += product.price
            #  aplica o frete se o valor do pedido for menor que 250.00 reais
            if float(serializer.validated_data['total']) < 250.00:
                serializer.validated_data['freight'] = len(serializer.validated_data['products']) * 10
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            # adiciona o valor de todos os items ao preço total do pedido
            serializer.validated_data['total'] = 0
            for product in serializer.validated_data['products']:
                serializer.validated_data['total'] += product.price
            #  aplica o frete se o valor do pedido for menor que 250.00 reais
            if float(serializer.validated_data['total']) < 250.00:
                serializer.validated_data['freight'] = len(serializer.validated_data['products']) * 10
            

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        order = self.get_object(pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)