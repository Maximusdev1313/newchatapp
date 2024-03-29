from dataclasses import fields
from msilib.schema import File
from unicodedata import category
from rest_framework import serializers
from .models import *



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user_name', 'comment', 'answers', 'timestamp']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file_field', 'title', 'files']

class MassageSerializer(serializers.ModelSerializer):
    # answer = serializers.StringRelatedField(many=True, read_only=True)
    answer = CommentSerializer(many=True, read_only=True)
    files = FileSerializer(many=True, read_only=True)
    class Meta:
        model = Massage
        fields = ['id',  'name', 'massage', 'files','timestamp', 'answer', 'category_name']

class SimpleFileSerializer(serializers.ModelSerializer):
    class Meta:
        model= SimpleFiles
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    category = MassageSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id','category_name', 'slug', 'icon','category']
