from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import io


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
@csrf_exempt
def materia_detail(request, id):

    try:
        materia = Materia.objects.get(id=id)
    except Materia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MateriaSerializer(materia)
    return JsonResponse(serializer.data)

#insertar
@csrf_exempt
def materia_new(request, nombre, departamento):

    materia = Materia()

    try:
        materia.materia = nombre
    except nombre in MATERIAS == False:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        materia.departamento = departamento
    except departamento in DEPARTAMENTOS == False:
        return Response(status=status.HTTP_404_NOT_FOUND)

    materia.save()
    serializer = MateriaSerializer(materia)
    return JsonResponse(serializer.data)


##profesor
#listar
@csrf_exempt
def profesor_list(request):

    profesores = Profesor.objects.all()
    serializer = ProfesorSerializer(profesores, many=True)
    return JsonResponse(serializer.data, safe=False)

#insertar?
@api_view(['GET', 'POST'])
def profesor_new(request):

    #profesor = Profesor()
    #profesor.nombre = "vicente"
    #profesor.apellido = "viloni"
    #profesor.dni = 34567854
    #profesor.rol = "profesor"
    #profesor.save()

    #profesor.materias.add(Materia.objects.get(id=1))
    #profesor.materias.add(Materia.objects.get(id=2))

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProfesorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)
