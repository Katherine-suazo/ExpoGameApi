from django.shortcuts import render, redirect
from .services import get_data_from_api, post_data_from_api
from django.contrib.auth.models import User
from .forms import UsuarioRegisterForm, ClienteRegisterForm
from .groups import get_or_create_groups


def home(request):
    return render(request,"core/home.html")

def gallery(request):
    return render(request,"core/gallery.html") 

def quienes_somos(request):
    return render(request, "core/qsomos.html")


#---------------------------------------------------- LISTA API

def listview(request):
    if request.method == 'GET':
        api_url = "http://127.0.0.1:8282/todos/api"
        posts = get_data_from_api(api_url)    # es una query tipo de modelos que traemos, posts es un json
        return render(request, "core/lista.html", {'posts': posts})
    
    # if request.method == 'POST':
    #     api_url = "http://127.0.0.1:8282/todos/api"
    #     solicitud = {
    #         'nombre': 'Valheim',
    #         'año': 2021,
    #         'genero': 'Survival',
    #         'user': 1
    #     }
    #     posts = post_data_from_api(api_url, solicitud)  # es una query tipo de modelos que traemos, posts es un json
    #     return redirect('/lista')

# def enviarapi(request):
#     api_url = "http://127.0.0.1:8282/todos/api"
#     solicitud = {
#         'nombre': 'Battlefield 6',
#         'año': 2025,
#         'genero': 'Shooter',
#         'user': 1
#     }
#     posts = post_data_from_api(api_url, solicitud)  # es una query tipo de modelos que traemos, posts es un json
#     return render(request, "core/lista.html", {'posts': posts})


#---------------------------------------------------- REGISTRO USUARIO/CLIENTE

def register_usuario(request):
    if request.method == 'POST':
        form = UsuarioRegisterForm(request.POST)
        if form.is_valid():
            usuarios = get_or_create_groups()

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_staff = True
            user.save()

            user.groups.add(usuarios)

            return redirect('/admin/login/')
    else:
        form = UsuarioRegisterForm()

    return render(request, 'core/registrarUsuario.html', {'form': form})


def register_cliente(request):
    if request.method == 'POST':
        form = ClienteRegisterForm(request.POST)
        if form.is_valid():
            clientes = get_or_create_groups()

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_staff = True
            user.save()

            user.groups.add(clientes)

            return redirect('/admin/login/')
    else:
        form = ClienteRegisterForm()

    return render(request, 'core/registrarCliente.html', {'form': form})
