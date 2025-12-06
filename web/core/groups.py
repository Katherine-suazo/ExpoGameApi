from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from novedades.models import Novedad

def get_or_create_groups():

    usuarios, created = Group.objects.get_or_create(name='Usuarios')
    if created:
        ct = ContentType.objects.get_for_model(Novedad)
        perms = Permission.objects.filter(content_type=ct, codename__startswith='view_')
        usuarios.permissions.set(perms)


    clientes, created = Group.objects.get_or_create(name='Clientes')
    if created:
        ct = ContentType.objects.get_for_model(Novedad)
        perms = Permission.objects.filter(content_type=ct)
        clientes.permissions.set(perms)

    return usuarios, clientes
