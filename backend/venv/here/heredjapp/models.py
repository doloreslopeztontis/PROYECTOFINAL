from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


class Alumno(models.Model):
    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, default='')
    apellido = models.CharField(max_length=20, blank=True, default='')
    libre = models.BooleanField(default=False)
    #libre: regular (false, 0) y libre (true, 1)
    cara = models.TextField()
    #link a la imagen de la cara

    #fkcurso
    #fkfaltas

    #class Meta:


CICLOS = [
    ('superior', 'Superior'),
    ('basico', 'Basico'),
    ]

AÑOS = [(i,i) for i in range(1, 11)]

ORIENTACIONES = [
    ('informatica', 'Informatica'),
    ('produccion', 'Produccion Musical'),
    ('gestion', 'Gestion'),
    ('construcciones', 'Construcciones'),
    ('quimica', 'Quimica'),
    ('electronica', 'Electronica'),
]

class Curso(models.Model):
    ciclo = models.CharField(max_length=20, choices=CICLOS)
    año = models.IntegerField(choices=AÑOS)
    letra = models.CharField(max_length=2)
    orientacion = models.CharField(max_length=20, choices=ORIENTACIONES)
    #fkcoordinador --> es un profesor con materia = coordinador

    #class Meta:


ROLES = [
    ('profesor', 'Profesor'),
    ('coordinador', 'Coordinador'),
]

class Profesor(models.Model):
    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, default='')
    apellido = models.CharField(max_length=20, blank=True, default='')
    rol = models.CharField(max_length=20, choices=ROLES)
    #list de materias o un multipleselect https://pypi.org/project/django-multiselectfield/
