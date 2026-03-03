from django.urls import path, include
from . import views
from rest_framework import routers

#Creating a router

# router = routers.DefaultRouter()
# Now we will register our product view set in this router so our view set is accessible by it with the urls
# router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', views.get_product, name="get_products"),
    path('create/', views.post_product, name="post_products"),
    path('<int:pk>/', views.get_productid, name ="get_productid")
]
