from django.contrib import admin
from django.urls import path,include
from apiApp import urls as todo_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include(todo_urls))
]
