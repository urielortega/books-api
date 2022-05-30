from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()

router.register('books', viewset=views.BookViewSet) # Se indica que se requieren las rutas necesarias para BookViewSet 

urlpatterns = [
    path('', include(router.urls)) # Se incluyen los urls del router en urlpatterns
]