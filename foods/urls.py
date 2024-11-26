from django.urls import path
from .views import CategoryAPIView, FoodAPIView, CommentAPIView

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='foodtype-list'),
    path('foods/', FoodAPIView.as_view(), name='food-list'),
    path('comments/', CommentAPIView.as_view(), name='comment-list'),
    
]
