from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length = 50,verbose_name = "Nombre")
    created=models.DateTimeField(auto_now_add = True,verbose_name = "F.Creación")
    updated=models.DateTimeField(auto_now = True,verbose_name = "F.Edición")

    class Meta():
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name
    
class GameImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    title = models.CharField(max_length = 50, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion", blank=True)
    published = models.DateTimeField(default = now, verbose_name = "F.Solictud")
    image = models.ImageField(upload_to = "projects", null = True, blank = True, verbose_name = "Imagen")
    categories = models.ManyToManyField(Category, verbose_name="Categorias")
    created = models.DateTimeField(auto_now_add = True, verbose_name = "F.Creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "F.Edición")

    class Meta():
        verbose_name="GameImagen"
        verbose_name_plural="GameImagenes"

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    game = models.ForeignKey(GameImage, on_delete=models.CASCADE, verbose_name="Juego", related_name="comments")
    author_name = models.CharField(max_length=50, verbose_name="Autor")
    text = models.TextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True, verbose_name="F.Creación")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return f"Comentario de {self.author_name} en {self.game.title}"

