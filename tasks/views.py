from django.shortcuts import render
from django.utils import timezone

from . import models

def homepage(request):
    hoy = timezone.now().date()
    tareas = models.Task.objects.all().filter(finished=False)
    return render(request, 'tasks/homepage.html', {
        'fecha': hoy,
        'tareas': tareas,
    })


def lista_proyectos(request):
    projects = models.Project.objects.all()
    return render(request, 'tasks/projects.html', {
        'projects': projects,
    })


def tareas_urgentes(request):
    tareas = (
        models.Task.objects
        .all()
        .filter(priority='H')
        .filter(finished=False)
        .order_by('orden', 'name')
    )
    return render(request, 'tasks/tareas_urgentes.html', {
        'tareas': tareas,
    })


def tareas_no_urgentes(request):
    tareas = (
        models.Task.objects
        .all()
        .filter(priority='L')
        .filter(finished=False)
        .order_by('orden', 'name')
    )
    return render(request, 'tasks/tareas_no_urgentes.html', {
        'tareas': tareas,
    })