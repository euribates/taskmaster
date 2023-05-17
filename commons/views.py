from django.shortcuts import render
from django.utils import timezone

from tasks.models import Task


def homepage(request):
    '''Página de inicio del proyecto.
    '''
    hoy = timezone.now().date()
    tareas = (
        Task.objects
        .filter(finished=False)
        .select_related('project')
    )
    return render(request, 'homepage.html', {
        'fecha': hoy,
        'tareas': tareas,
        'title': "Taskmater - Gestor de tareas",
        'subtitle': 'Página de inicio',
    })
