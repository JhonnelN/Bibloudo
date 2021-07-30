from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import LibrosViewSet, SemestreViewSet

app_name = 'repisa'

router = SimpleRouter()
router.register('libros', LibrosViewSet, basename='libros')
router.register('semestres', SemestreViewSet, basename='Semestres')
router.register('carreras', SemestreViewSet, basename='Carreras')


urlpatterns = [
 path('', include(router.urls))
]
