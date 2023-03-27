from django.contrib import admin
# Register your models here.

from libreriaapp.models import libros
admin.site.register(libros)

from libreriaapp.models import ulector
admin.site.register(ulector)

from libreriaapp.models import alquiler
admin.site.register(alquiler)
