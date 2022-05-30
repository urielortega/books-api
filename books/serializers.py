from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book # Se usa el modelo Book creado en models.py ...
        fields = "__all__" # ...y se especifica el uso de todos sus atributos