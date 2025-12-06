from django.db import models

class LinkRed(models.Model):
    key = models.SlugField(max_length=50, unique=True, verbose_name="Nombre Clave")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    url = models.URLField(verbose_name="Enlace", blank=True, null=True)

    class Meta():
        verbose_name = "Red"
        verbose_name_plural = "Redes"

    def __str__(self):
        return self.name
