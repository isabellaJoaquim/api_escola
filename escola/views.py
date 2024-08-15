# from django.http import JsonResponse
# # Create your views here.
# def estudantes(request):
#     if request.method == 'GET':
#             estudante = {
#                 'id':'2',
#                 'nome':'senai'
#             }
#     return JsonResponse(estudante)

from rest_framework import viewsets, generics
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, Matricula, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = Matricula

class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer

