from dataclasses import fields
from rest_framework import serializers
from .models import *


class MassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Massage
        fields ='__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'