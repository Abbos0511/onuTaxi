from rest_framework import serializers
from .models import *
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields='__all__'
class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Services
        fields='__all__'
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields='__all__'
class ComplaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Complaints
        fields='__all__'
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields='__all__'
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'