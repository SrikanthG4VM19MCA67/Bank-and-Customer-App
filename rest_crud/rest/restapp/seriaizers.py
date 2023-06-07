from .models import *
from rest_framework import serializers

class BankSerializers(serializers.ModelSerializer):
    class Meta:
        model=Bank
        fields='__all__'
        
class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'