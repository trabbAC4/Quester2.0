from http.client import HTTPResponse
from django.urls import path
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render



def register(request):
    return HttpResponse('This is the registration page')

def my_Login(request):
    return HttpResponse('This is the login Page')

def home(request):
    return HttpResponse('This is the homepage')