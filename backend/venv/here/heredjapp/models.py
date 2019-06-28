from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinLengthValidator, MinValueValidator
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles



MATERIAS = [
    ('lengua', 'Lengua'),
    ('matematica', 'Matematica'),
    ('fuentes', 'Cultura Judia'),
    ('historiajudia', 'Historia Judia'),
    ('historia', 'Historia'),
    ('geografia', 'Geografia'),
    ('fisica', 'Fisica'),
    ('quimica', 'Quimica'),
    ('filosofia', 'Filosofia'),
    ('etica', 'Etica'),
    ('gimnasia', 'Educacion Fisica'),
    ('ingles', 'Ingles'),
]

DEPARTAMENTOS = [
    ('sociales', 'Sociales'),
    ('ingles', 'Ingles'),
    ('quimica', 'Quimica'),
    ('fisica', 'Fisica'),
    ('judia', 'Judia'),
    ('gimnasia', 'Educacion Fisica'),
    ('matematica', 'Matematica'),
    ('literatura', 'Literatura'),
]

class Materia(models.Model):
    materia = models.CharField(max_length=20, choices=MATERIAS)
    departamento = models.CharField(max_length=20, choices=DEPARTAMENTOS)

    def __str__(self):
        return '%s' % (self.materia)


ROLES = [
    ('profesor', 'Profesor'),
    ('coordinador', 'Coordinador'),
]

class Profesor(models.Model):
    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, default='')
    apellido = models.CharField(max_length=20, blank=True, default='')
    rol = models.CharField(max_length=20, choices=ROLES)
    materias = models.ManyToManyField(Materia)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)


CICLOS = [
    ('superior', 'Superior'),
    ('basico', 'Basico'),
    ]

ANIOS = [(i,i) for i in range(1, 11)]


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
    anio = models.IntegerField(choices=ANIOS)
    letra = models.CharField(max_length=2)
    orientacion = models.CharField(max_length=20, choices=ORIENTACIONES)
    coordinador = models.ForeignKey(Profesor, null=True, on_delete=models.SET_NULL) #un profesor con materia = coordinador

    def __str__(self):
        return '%s° %s %s' % (self.año, self.orientacion, self.letra)


class Alumno(models.Model):
    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    cara = models.TextField() #link a la imagen de la cara
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    libre = models.BooleanField(default=False)  #regular (false, 0) y libre (true, 1)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)


BLOQUES = [(i,i) for i in range(1, 7)]

class Bloque(models.Model):
    bloque = models.IntegerField(choices=BLOQUES)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return '%s° bloque' % (self.bloque)


class Clase(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    bloque = models.ForeignKey(Bloque, on_delete=models.PROTECT)
    dia = models.DateField(auto_now_add=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET(0))
    materia = models.ForeignKey(Materia, on_delete=models.SET(0))
    aula = models.IntegerField(validators=[MaxValueValidator(5730)])

    def __str__(self):
        return 'clase de %s de %s, con %s' % (self.materia, self.curso, self.profesor)


class Presentismo(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    time_stamp = models.TimeField(auto_now_add=True)
    presente = models.BooleanField(default=False)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)

    def __str__(self):
        if self.presente == True:
            return '%s presente' % (self.alumno)
        return '%s ausente' % (self.alumno)
