from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics

# Create your views here.

class ModelListView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class = PostSerializer

    
