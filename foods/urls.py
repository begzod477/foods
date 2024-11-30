from django.urls import path, include
from .views import  FoodAPIViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('foods', FoodAPIViewSet, basename='food')
print(router.urls)


urlpatterns = [

    path('foods/', FoodAPIViewSet.as_view()),
    path('foods/<int:pk>/', FoodAPIViewSet.as_view(name='food-detail')),
    
    path('', include(router.urls))


    
]
