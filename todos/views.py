from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Todo
from apis.serializers import TodoSerializer


# Create your views here.
def index(self):
    return HttpResponse("welcome on todo")
