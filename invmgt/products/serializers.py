from rest_framework import serializers
from .models import Product

# create serializers here
# adding validations here
# class ProductSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model= Product
#         fields = "__all__"
    
#     def priceValidation(self,value):
#         if value<=0:
#             raise serializers.ValidationError("price greater than 0")
#         return value
    
#     def quantityValidation(self,value):
#         if value<1:
#             raise serializers.ValidationError("quantity greater than 0")
#         return value

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=100)
    # description = serializers.CharField(allow_blank=True)
    category = serializers.CharField(max_length=2)
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    brand = serializers.CharField(max_length=100)
    date_added = serializers.DateTimeField(read_only=True)


    def validate_price(self,value): # format is validate_<fieldname>
        if value<=0:
            raise serializers.ValidationError("price greater than 0")
        return value
    
    def validate_quantity(self,value):
        if value<1:
            raise serializers.ValidationError("quantity greater than 0")
        return value
    
    # cross-field validation
    def validate(self,value):
        if value["category"]=="LP" and value["price"]<100:
            raise serializers.ValidationError("Price for a laptop can't be below 100!")
        return value
