from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import io
import random


from heredjapp.models import Materia, MATERIAS, DEPARTAMENTOS, Profesor
from heredjapp.serializers import MateriaSerializer, ProfesorSerializer



def index(request):
    return render(request,'index.html')

##materia
#listar
@api_view(['GET'])
def materia_list(request):

    if request.method == 'GET':
        materias = Materia.objects.all()
        serializer = MateriaSerializer(materias, many=True)
        return JsonResponse(serializer.data, safe=False)


#traer
@api_view(['GET', 'DELETE'])
def materia_detail(request, id):

    try:
        materia = Materia.objects.get(id=id)
    except Materia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MateriaSerializer(materia)
        return JsonResponse(serializer.data)


#insertar
@api_view(['POST'])
def materia_new(request):

    if request.method == 'POST':
        #data = JSONParser().parse(request.body)
        #serializer = MateriaSerializer(data=data)
        serializer = MateriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)


##profesor
#listar
@csrf_exempt
def profesor_list(request):

    profesores = Profesor.objects.all()
    serializer = ProfesorSerializer(profesores, many=True)
    return JsonResponse(serializer.data, safe=False)

#traer
@api_view(['GET'])
def profesor_detail(request, dni):

    if request.method == 'GET':
        try:
            profesor = Profesor.objects.get(pk=dni)
        except Profesor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProfesorSerializer(profesor)
        return JsonResponse(serializer.data)

#listar sus materias
def profesor_materias(request, dni):
    if request.method == 'GET':
        try:
            profesor = Profesor.objects.get(pk=dni)
        except Profesor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        materias = profesor.materias.all()
        #materias = profesor.materias_set.all()
        serializer = MateriaSerializer(materias, many=True)
        return JsonResponse(serializer.data, safe=False)

#:) xd

#insertar
@api_view(['POST'])
def profesor_new(request):

    if request.method == 'POST':
        data = JSONParser().parse(request.body)
        serializer = ProfesorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

#insertar materias
@api_view(['GET'])
def profesor_new_materia(request, dni):
    try:
        profesor = Profesor.objects.get(pk=dni)
    except Profesor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        materias = Materia.objects.all()
        materia = random.choice(materias)
        materia.profesor_set.create(profesor)

    serializer = ProfesorSerializer(profesor)
    return JsonResponse(serializer.data)
