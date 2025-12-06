from django.urls import path
from .views import(TodoListApiView, )

urlpatterns = [
    path('api', TodoListApiView.as_view()),   # TodoListApiView es una clase, pero que convertimos en vista, asi en ves de llamar a cada def los llamamos a todos.
]