from rest_framework import serializers
from .models import Product

# create serializers here
# adding validations here
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Product
        fields = "__all__"
    
    def priceValidation(self,value):
        if value<=0:
            raise serializers.ValidationError("price greater than 0")
        return value
    
    def quantityValidation(self,value):
        if value<1:
            raise serializers.ValidationError("quantity greater than 0")
        return value