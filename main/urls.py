"""main URL Configuration
"""
from django.contrib import admin
from django.urls import path

import tasks.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tasks.views.homepage),
    path('high/', tasks.views.tareas_urgentes),
    path('urgentes/', tasks.views.tareas_urgentes),
    path('low/', tasks.views.tareas_no_urgentes),
    path('no_urgentes/', tasks.views.tareas_no_urgentes),
    path('projects/', tasks.views.lista_proyectos),
]


