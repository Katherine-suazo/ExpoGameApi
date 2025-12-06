from django.shortcuts import render, get_object_or_404
from .models import GameImage, Category

def callGallery(request):
    gi = GameImage.objects.all()
    return render(request, 'solicitud/galleryGame.html', {'gi': gi})

def callCategory(request, id_category):
    ctg = get_object_or_404(Category, id = id_category)
    gi = GameImage.objects.filter(categories=ctg)
    return render(request, "solicitud/categoria.html", {"ctg": ctg, "gi": gi})
