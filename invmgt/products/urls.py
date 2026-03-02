from django.urls import path, include
from .views import ProductViewSet
from rest_framework import routers

#Creating a router

router = routers.DefaultRouter()
# Now we will register our product view set in this router so our view set is accessible by it with the urls
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
