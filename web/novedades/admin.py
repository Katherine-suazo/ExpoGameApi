from django.contrib import admin
from .models import Novedad

# Register your models here.

class ProjectAdmin(admin.ModelAdmin): # clase para personalizar el admin
    readonly_fields=('created','updated')

admin.site.register(Novedad, ProjectAdmin) # registrar el modelo en el admin con la clase personalizada
 