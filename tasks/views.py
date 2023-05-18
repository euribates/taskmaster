from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone

from . import models
from . import forms


def lab(request):
    return render(request, 'tasks/lab.html', {
        "title": "Labs",
        })


def lista_proyectos(request):
    projects = models.Project.objects.all()
    return render(request, 'tasks/projects.html', {
        'projects': projects,
    })


def tareas_por_prioridad(request, prioridad):
    codigo_prioridad = prioridad[0].upper()
    tareas = (
        models.Task.objects
        .filter(priority=codigo_prioridad)
        .exclude(finished=True)
        .order_by('orden', 'name')
    )
    return render(request, 'tasks/listado_tareas.html', {
        'title': f"Tareas con prioridad {prioridad}",
        'tareas': tareas,
        'prioridad': prioridad,
    })


def tareas_urgentes(request):
    tareas = (
        models.Task.objects
        .filter(priority='H')
        .exclude(finished=True)
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


def detalle_proyecto(request, pk):
    project = models.Project.objects.get(pk=pk)
    tareas = project.task_set.all()
    return render(request, 'tasks/detalle_proyecto.html', {
        'project': project,
        'tareas': tareas,
    })

def detalle_proyecto_code(request, code):
    project = models.Project.objects.get(code=code)
    tareas = project.task_set.all()
    return render(request, 'tasks/detalle_proyecto.html', {
        'project': project,
        'tareas': tareas,
    })

def buscar_tareas(request):
    import logging
    logging.warning('buscar_tareas starts')

    tareas = []
    num_tareas = 0
    query = ''
    if request.method == 'POST':
        logging.warning('Entra en el post')
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            logging.error('is valid')
            query = form.cleaned_data['query']
            tareas = models.Task.objects.filter(name__icontains=query)
            num_tareas = tareas.count()
    else:
        form = forms.SearchForm()
    return render(request, 'tasks/buscar_tareas.html', {
        'form': form,
        'method': request.method,
        'tareas': tareas,
        'query': query,
        'num_tareas': num_tareas,
    })


def crear_proyecto(request):
    if request.method == 'POST':
        form = forms.ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/projects/')
    else:
        form = forms.ProjectForm()
    return render(request, 'tasks/crear_proyecto.html', {
        'form': form,
    })

from django.views.generic import DetailView


class DetalleTarea(DetailView):
    model = models.Task
    template_name = 'tasks/detalle_tarea.html'


detalle_tarea = DetalleTarea.as_view()
