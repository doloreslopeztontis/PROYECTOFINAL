from rest_framework import serializers
from django.db import models
from heredjapp.models import Alumno, Curso, Profesor, Materia, Clase, Bloque, Presentismo


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = ('id', 'materia', 'departamento')


class ProfesorSerializer(serializers.ModelSerializer):
    materias = MateriaSerializer(read_only=False, many=True)

    class Meta:
        model = Profesor
        fields = ('dni', 'nombre', 'apellido', 'rol', 'materias')

    def create(self, validated_data):
        materias = validated_data.pop('materias')
        album = Profesor.objects.create(validated_data)

        for materia in materias:
            Materia.objects.create(materia)
        return album

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'ciclo', 'anio', 'letra', 'orientacion', 'coordinador')


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('dni', 'nombre', 'apellido', 'cara', 'curso', 'libre')


class BloqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloque
        fields = ('bloque', 'hora_inicio', 'hora_fin')


class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ('curso', 'bloque', 'dia', 'profesor', 'materia', 'aula')


class PresentismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentismo
        fields = ('alumno', 'time_stamp', 'falta', 'clase')