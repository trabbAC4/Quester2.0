from http.client import HTTPResponse
from django.urls import path
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect 




def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'Register.html')

def my_Login(request):
    return render(request, 'Login.html')

