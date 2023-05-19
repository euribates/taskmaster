from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from django_countries.fields import CountryField


def hoy():
    return timezone.now().date()


class Project(models.Model):

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['code']

    name = models.CharField(max_length=250)
    code = models.SlugField(max_length=4, unique=True)
    description = models.TextField()
    country = CountryField(default='ES')
    start_date = models.DateField(default=hoy)
    end_date  = models.DateField()

    def __str__(self):
        return f'{self.code}: {self.description}'



class Task(models.Model):
    
    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['-orden', 'name']
    
    name = models.CharField(max_length=250)
    finished = models.BooleanField(default=False)
    orden = models.IntegerField(default=100)
    priority = models.CharField(
        max_length=1,
        choices=[
            ('H', 'Alta'),
            ('N', 'Normal'),
            ('L', 'Baja'),
        ],
        default='N',
    )
    color = models.CharField(
        max_length=6,
        choices=[
            ('blue', 'Azul Marino'),
            ('red', 'Rojo'),
            ('orange', 'Naranja'),
            ('green', 'Verde'),
        ],
        default='blue',
        )
    due_date = models.DateField(
        blank=True,
        null=True,
        default=None,
    )
    project = models.ForeignKey(
        Project,
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        )

    def __str__(self):
        return self.name

    def is_due(self) -> bool:
        if self.due_date is None:
            return False
        return self.due_date <= hoy()
