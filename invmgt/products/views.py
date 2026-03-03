from django.shortcuts import render
from .models import Product 
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .storage import data
from .storage import id_counter
from django.utils import timezone
import math
# from rest_framework import viewsets

# Create your views here.

# class ProductViewSet(viewsets.ModelViewSet):
    
#     serializer_class = ProductSerializer
def findproduct(pk):
    for item in data:
        if item['id']==pk:
            return item
        
@api_view(['GET'])
def get_product(request):
    page = max(int(request.GET.get('page',1)),1)
    size = max(int(request.GET.get('size',1)),1)

    total_items = len(data)
    total_pages = math.ceil(total_items/size)

    start = page*size - size 
    # page 2 size 4 : start = 
    end= start+size

    paginated_data = data[start:end]

    serializer = ProductSerializer(paginated_data, many=True)
    return Response({
        "total items": total_items,
        "total pages": total_pages,
        "current page": page,
        "page size": size,
        "data":serializer.data
        })

@api_view(['POST'])
def post_product(request):
    global id_counter
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        product = serializer.validated_data
        product['id']=id_counter
        id_counter+=1
        product['date_added']=timezone.now()

        data.append(product)

        return Response(product, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE' , 'PATCH'])
def get_productid(request, pk):
    item = findproduct(pk)
    if not item:
        return Response({"error" : "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'GET':
        return Response(ProductSerializer(item).data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            updated_data = serializer.validated_data
            updated_data["id"] = pk
            updated_data["date_added"] = item["date_added"]

            data.remove(item)
            data.append(updated_data)

            return Response(updated_data, status=status.HTTP_200_OK)
        
        # else:
        #     return raise() -> serializer handles the error on its own
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        data.remove(item)
        serializer = ProductSerializer(item)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT) #nothing to show
    
    # Now .items() is a dictionary method. It returns key–value pairs as tuples.
    elif request.method == 'PATCH':

        serializer = ProductSerializer(data = request.data, partial=True)
        if serializer.is_valid():
            updated_data = serializer.validated_data 
            for key,value in updated_data.items():
                item[key] = value

            return Response(ProductSerializer(item).data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response({"detail": "Method not found. Choose among - GET, POST, PUT, DELETE, PATCH"}, status=status.HTTP_400_BAD_REQUEST)