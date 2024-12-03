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
from rest_framework.pagination import PageNumberPagination
from rest_framework.versioning import NamespaceVersioning
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100



class FoodThrottling(throttling.UserRateThrottle):
    scope = 'food'




class FoodAPIViewSet(ModelViewSet):
    serializer_class = FoodSerializer
    throttle_scope = 'food'
    pagination_class = CustomPagination
    versioning_class = NamespaceVersioning  

    def get_queryset(self):
        return Food.objects.all()

    @swagger_auto_schema(
        operation_description="Food list with pagination",
        responses={200: openapi.Response('Successful response', FoodSerializer(many=True))}
    )
    def list(self, request, *args, **kwargs):
   
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.get_paginated_response(self.serializer_class(page, many=True).data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
  



class SendEmailAPIView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = serializer.validated_data.get("subject")
        message = serializer.validated_data.get("message")

        for i in ['example12r@gmail.com',
             'abdulvosid780@gmail.com',
             'zokirovbegzod771@gmail.com']:
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