from django.db import models
from django.contrib.auth.models import User


class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    año = models.IntegerField()
    genero = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)

    def __str__(self):
        return self.nombre
    
