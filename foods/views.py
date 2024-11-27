from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
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


# class FoodAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Food.objects.all()
#     serializer_class = FoodSerializer
#     permission_classes = [IsAdminOrReadOnly]

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class CommentAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
