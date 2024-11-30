from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodAPIViewSet, SendEmailAPIView

router = DefaultRouter()
router.register('foods', FoodAPIViewSet, basename='food')  

urlpatterns = [
    path('send-email/', SendEmailAPIView.as_view()), 
    path('', include(router.urls)),  
]
