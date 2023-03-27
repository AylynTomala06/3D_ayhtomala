from django.db import models

# Create your models here.
class usuarios(models.Model):
    id=models.BigAutoField(verbose_name='id', serialize=False, auto_created=True, primary_key=True )
    usuario= models.CharField(max_length=20)
    nombre= models.CharField(max_length=50)
    clave= models.CharField(max_length=15)
    class Meta:
        db_table='usuarios'
        ordering=['nombre']

class libros(models.Model):
    id=models.BigAutoField(verbose_name='id', serialize=False, auto_created=True, primary_key=True )
    titulo=models.CharField(max_length=45)
    autor=models.CharField(max_length=50)
    categoria=models.CharField(max_length=28)
    fecha_lanzamiento=models.DateField()
    class Meta:
        db_table= 'libros'
        ordering= ['id']
    def __str__(self):
        return self.titulo

class ulector(models.Model):
    id_lector=models.BigAutoField(verbose_name='id lector', serialize=False, auto_created=True, primary_key=True )
    cedula=models.IntegerField()
    nombre=models.CharField(max_length=30)
    telefono= models.IntegerField()
    observacion= models.CharField(max_length=255)
    class Meta:
        db_table='ulector'
        ordering=['id_lector']
    def __str__(self):
        return self.nombre

class alquiler (models.Model):
    id_alquiler = models.BigAutoField(verbose_name='id alquiler', serialize=False, auto_created=True, primary_key=True)
    id_ulector=models.ForeignKey(ulector, on_delete=models.CASCADE)
    id_libro=models.ForeignKey(libros, on_delete=models.CASCADE)
    fecha_salida=models.DateField()
    fecha_entrada=models.DateField()
    class Meta:
        db_table='alquiler'
        ordering= ['id_alquiler']
    def __int__(self):
        return self.id_libro
