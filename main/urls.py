"""main URL Configuration
"""
from django.contrib import admin
from django.urls import re_path, path, include

import tasks.views
import commons.views

urlpatterns = [
    path('', commons.views.homepage, name='homepage'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('lab/', tasks.views.lab),
    path('buscar/', tasks.views.buscar_tareas, name="buscar"),
    path('tareas/nueva/', tasks.views.create_task, name='create_task'),
    path('tareas/editar/<int:pk>/', tasks.views.edit_task, name='edit_task'),
    re_path(r'^tareas/(high|normal|low)/$', tasks.views.tareas_por_prioridad),
    path('low/', tasks.views.tareas_no_urgentes, name='tareas_no_urgentes'),
    path('nor/', tasks.views.tareas_no_urgentes, name='tareas_no_urgentes'),
    path('urgentes/', tasks.views.tareas_urgentes, name='urgentes'),
    path('task/<int:pk>/', tasks.views.detalle_tarea, name="detalle_tarea"),
    path('no_urgentes/', tasks.views.tareas_no_urgentes, name='no-urgentes'),
    path('projects/', tasks.views.lista_proyectos, name='proyectos'),
    path('projects/<int:pk>/', tasks.views.detalle_proyecto, name='detalle_proyecto'),
    path('projects/new/', tasks.views.crear_proyecto, name='crear_proyecto'),
    path(
        'projects/<slug:code>/',
        tasks.views.detalle_proyecto_code,
        name='proyecto_por_codigo' 
        ),
    path('admin/', admin.site.urls),
]
