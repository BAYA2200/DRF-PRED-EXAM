from rest_framework import serializers, request

from account.models import Profile
from shop.models import Category, Item, Order


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ItemSerializers(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['profile']


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['profile', 'item']

