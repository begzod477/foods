from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter  
from .models import Category, Food, Comment
from .serializers import CategorySerializer, FoodSerializer, CommentSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import throttling
from rest_framework.throttling import UserRateThrottle
from .serializers import FoodSerializer, EmailSerializer
from rest_framework.views import APIView
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from rest_framework.response import Response




class FoodAPIViewSet(ModelViewSet): 
    serializer_class = FoodSerializer
    thorttle_scope = 'food'
    throttle_classes = [UserRateThrottle] 


    def get_queryset(self):
        return Food.objects.all()
  
class SendEmailAPIView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = serializer.validated_data.get("subject")
        message = serializer.validated_data.get("message")

        for i in ['madrahimovq@gmail.com', 'shunchakiabdujabbor@gmail.com',
             'abdulvosid780@gmail.com',
             'karimovnurmuham1201mad@gmail.com']:
            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                [i]
            )

        return Response("Yuborildi!!!")














# class FoodDetailApiView(RetrieveUpdateAPIView):
#     queryset = Food.objects.all()
#     serializer_class = FoodSerializer

# class CommentAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAdminOrReadOnly]

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class CategoryAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsAdminOrReadOnly]

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)