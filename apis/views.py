from django.shortcuts import render
# from django.serializers import generics
from .serializers import TodoSerializer
from todos.models import Todo
import requests

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
