from rest_framework import serializers
from .models import Category, Food, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=150)
    message = serializers.CharField()

