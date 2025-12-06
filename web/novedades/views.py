from django.shortcuts import render
from .models import Novedad

from django.core.paginator import Paginator


# def nov(request):
#     novedad = Novedad.objects.all()
#     return render(request, "nov/novedades.html", {'novedad': novedad})


def nov(request):
    noved = Paginator(Novedad.objects.all(), 2)
    nov_number = request.GET.get("page")
    novedad = noved.get_page(nov_number)

    return render(request, "nov/novedades.html", {'novedad': novedad}) # pasar la pagina al template
