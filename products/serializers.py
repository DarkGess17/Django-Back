from rest_framework import serializers
from. models import Category, Product

class ProductSerializer(serializers.ModelSerializer):

    category_name =serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = ('id','name', 'image', 'category', 'category_name', 'description', 'calification', 'price')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')