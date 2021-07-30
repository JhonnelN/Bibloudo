from rest_framework.serializers import ModelSerializer
from .models import Libro, Semestre, Carrera



class LibrosSerializer(ModelSerializer):
  
  class Meta:
    model = Libro
    fields = '__all__'

class SemestreSerializer(ModelSerializer):
  
  class Meta:
    model = Semestre
    fields = '__all__'


class CarreraSerializer(ModelSerializer):
  
  class Meta:
    model = Carrera
    fields = '__all__'