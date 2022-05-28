from django.shortcuts import render

# Create your views here.
from urllib import request
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class MassageViewSet(ModelViewSet):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer
   
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
 

class SimpleFilesViewSet(ModelViewSet):
    queryset = SimpleFiles.objects.all()
    serializer_class = SimpleFileSerializer