from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter  
from .models import Category, Food, Comment
from .serializers import CategorySerializer, FoodSerializer, CommentSerializer
from .permissions import IsAdminOrReadOnly

class CategoryAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class FoodAPIView(ListAPIView): 
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = [SearchFilter, OrderingFilter] 
    search_fields = ['name', 'description']  
    ordering_fields = ['price', 'name']  
    ordering = ['price']  

class FoodDetailApiView(RetrieveUpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class CommentAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
