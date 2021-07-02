from django.db import models

# Lista de modelos creados:
# Autor
# Carrera
# Libro

#---------------------------------------------------------
class Autor(models.Model):
    # clave primaria
    id = models.AutoField(primary_key=True)
    # --------
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=200, blank=False, null=False)
    nacionalidad = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateField(
        "Fecha de creacion", auto_now=True, auto_now_add=False
    )
    # Metadatos
    class Meta:

        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

#---------------------------------------------------------
class Carrera(models.Model):
    # clave primaria
    id = models.AutoField(primary_key=True)
    # --------
    nombre = models.CharField(max_length=200, blank=False, null=False)
    # Metadatos
    class Meta:

        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
#---------------------------------------------------------
class Semestre(models.Model):
    # clave primaria
    id = models.AutoField(primary_key=True)
    # --------
    nombre = models.CharField(max_length=200, blank=False, null=False)
    # Metadatos
    class Meta:

        verbose_name = "Semestre"
        verbose_name_plural = "Semestres"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

#---------------------------------------------------------
class Libro(models.Model):
    def libros_path(self, filename):
        return 'libros/{0}/{1}_{2}.{3}'.format(
            self.carrera,
            self.titulo,
            self.Autor,
            filename.split('.')[-1]
        )
    # clave primaria
    id = models.AutoField(primary_key=True)
    # --------
    titulo = models.CharField(max_length=200, blank=False, null=False)
    fecha_publicacion = models.DateField(max_length=200, blank=True, null=True)
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera,  blank=True, null=True, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre,  blank=True, null=True, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(
        "Fecha de creacion", auto_now=True, auto_now_add=False
    )

    Libro =  models.FileField(default="", blank=False, null=False, upload_to=libros_path)
    # Metadatos
    class Meta:

        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo




