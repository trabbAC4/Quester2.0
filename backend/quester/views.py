from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Quester

# Create your views here.
class QuesterView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Quester.objects.all()
