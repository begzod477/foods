from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from .models import Category, Food, Comment
from .serializers import CategorySerializer, FoodSerializer, CommentSerializer

class CategoryAPIView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class FoodAPIView(GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CommentAPIView(GenericAPIView, CreateModelMixin, ListModelMixin, RetrieveModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

