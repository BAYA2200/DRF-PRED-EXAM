import generics as generics
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Category, Item, Order
from shop.permissions import CategoryPermission, ItemPermission, OrderPermission, OrderPermission2
from shop.serializers import CategorySerializers, ItemSerializers, OrderSerializers


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticatedOrReadOnly, CategoryPermission]
    authentication_classes = [TokenAuthentication, ]


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticatedOrReadOnly, CategoryPermission]
    authentication_classes = [TokenAuthentication, ]



class ItemListCreateAPIView(APIView):
    queryset = Item.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, CategoryPermission]
    authentication_classes = [TokenAuthentication, ]


    def get(self, request, pk):
        cat = get_object_or_404(Category, pk=pk)
        it = cat.item_set.all()
        serializers = ItemSerializers(it, many=True)
        return Response(serializers.data, status=status.HTTP_201_CREATED)

    def post(self, request, pk):
        cat = get_object_or_404(Category, pk=pk)
        serializer = ItemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(category=cat, profile=self.request.user.profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemRetrieveUpdateDestroyAPIView(APIView):
    queryset = Item.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, ItemPermission]
    authentication_classes = [TokenAuthentication, ]


    def get(self, request, category_id, pk):
        cat = get_object_or_404(Category, id=category_id)
        it = cat.item_set.get(pk=pk)
        serializers = ItemSerializers(it)
        return Response(serializers.data, status=status.HTTP_201_CREATED)

    def put(self, request, category_id, pk):
        cat = get_object_or_404(Category, id=category_id)
        it = cat.item_set.get(pk=pk)
        serializer = ItemSerializers(it, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id, pk):
        cat = get_object_or_404(Category, id=category_id)
        it = cat.item_set.get(pk=pk)
        it.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, OrderPermission]
    authentication_classes = [TokenAuthentication, ]


    def get_queryset(self):
        return self.queryset.filter(pk=self.kwargs['pk'])

    def perform_create(self, serializer):
        item_id = self.kwargs.get('pk')
        item = get_object_or_404(Item, id=item_id)

        # Устанавливаем item перед сохранением заказа
        serializer.save(item=item, profile=self.request.user.profile)


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, OrderPermission2]
    authentication_classes = [TokenAuthentication, ]

