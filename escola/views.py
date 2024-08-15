from django.http import JsonResponse
# Create your views here.
def estudantes(request):
    if request.method == 'GET':
            estudante = {
                'id':'2',
                'nome':'senai'
            }
    return JsonResponse(estudante)