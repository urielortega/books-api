from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

# Create your views here.
class BookViewSet(viewsets.ModelViewSet): # Se usa ModelViewSet para permitir acciones CRUD
    serializer_class = BookSerializer
    queryset = Book.objects.all() # Se indica que deseamos retornar todos los objetos Book