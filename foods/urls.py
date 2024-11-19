from django.urls import path
from .views import CategoryView, FoodView, OrderView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
    path('foods/', FoodView.as_view(), name='foods'),
    path('orders/', OrderView.as_view(), name='orders'),
]
