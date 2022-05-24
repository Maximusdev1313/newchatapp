from dataclasses import fields
from rest_framework import serializers
from .models import *


class MassageSerializer(serializers.ModelSerializer):
    answer = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Massage
        fields = ['id', 'category_name', 'name', 'massage', 'file', 'timestamp', 'answer']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user_name', 'comment', 'answers']