from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view

from .serializers import ClienteInicioSesionSerializer
from .serializers import ClienteRegistroSerializer


# Create your views here.
