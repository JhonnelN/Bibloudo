from django.db.models import fields
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Carrera, Libro, Semestre
from .serializers import LibrosSerializer, SemestreSerializer, CarreraSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class LibrosViewSet(ModelViewSet):
  permission_classes = (IsAuthenticated,)
  serializer_class = LibrosSerializer
  queryset = Libro.objects.all()
  filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
  filterset_fields = ["autor", "materia"]


class SemestreViewSet(ModelViewSet):
  permission_classes = (IsAuthenticated,)
  serializer_class = SemestreSerializer
  queryset = Semestre.objects.all()

class CarreraViewSet(ModelViewSet):
  permission_classes = (IsAuthenticated,)
  serializer_class = CarreraSerializer
  queryset = Carrera.objects.all()

