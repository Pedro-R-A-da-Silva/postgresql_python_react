from email.policy import default
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

from _crud.models import Atividade,Funcionario,Situação
from _crud.serializers import AtivividadeSerializer,FuncionarioSerializer,SituaçãoSerializer

# Create your views here.
@csrf_exempt
def atividade_Api(request,id=0):
    if request.method == 'GET':
        atividade = Atividade.objects.all()
        atividade_Serializer = AtivividadeSerializer(atividade,many=True)
        return JsonResponse(atividade_Serializer.data,safe=False)
    elif request.method == 'POST':
        funcionarios_data = JSONParser().parse(request)
        funcionarios_Serializer = FuncionarioSerializer(data = funcionarios_data)
        if funcionarios_Serializer.is_valid():
            funcionarios_Serializer.save()
            return JsonResponse("operação realizada com sucesso", safe=False)
        return JsonResponse("erro na operação", safe = False)
    elif request.method == 'PUT':
        funcionarios_data = JSONParser().parse(request)
        funcionario = Funcionario.objects.get(matricula = funcionarios_data['matricula'])
        funcionarios_Serializer = FuncionarioSerializer(funcionario ,data = funcionarios_data)
        if funcionarios_Serializer.is_valid():
            funcionarios_Serializer.save()
            return JsonResponse("operação realizada com sucesso", safe=False)
        return JsonResponse("erro na operação", safe = False)
    elif request.method == 'DELETE':
        funcionarios = Funcionario.objects.get(matricula=id)
        funcionarios.delete()
        return JsonResponse("deletado com sucesso")

@csrf_exempt
def funcionario_Api(request,id=0):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.all()
        funcionarios_Serializer = FuncionarioSerializer(funcionarios,many=True)
        return JsonResponse(funcionarios_Serializer.data,safe=False)
    elif request.method == 'POST':
        funcionarios_data = JSONParser().parse(request)
        funcionarios_Serializer = FuncionarioSerializer(data = funcionarios_data)
        if funcionarios_Serializer.is_valid():
            funcionarios_Serializer.save()
            return JsonResponse("operação realizada com sucesso", safe=False)
        return JsonResponse("erro na operação", safe = False)
    elif request.method == 'PUT':
        funcionarios_data = JSONParser().parse(request)
        funcionario = Funcionario.objects.get(matricula = funcionarios_data['matricula'])
        funcionarios_Serializer = FuncionarioSerializer(funcionario ,data = funcionarios_data)
        if funcionarios_Serializer.is_valid():
            funcionarios_Serializer.save()
            return JsonResponse("operação realizada com sucesso", safe=False)
        return JsonResponse("erro na operação", safe = False)
    elif request.method == 'DELETE':
        funcionarios = Funcionario.objects.get(matricula=id)
        funcionarios.delete()
        return JsonResponse("deletado com sucesso")

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name, safe=False)        

@csrf_exempt
def situação_Api(request,id=0):
    if request.method == 'GET':
        situaçao = Situação.objects.all()
        situaçao_Serializer = SituaçãoSerializer(situaçao,many=True)
        return JsonResponse(situaçao_Serializer.data,safe=False)
    elif request.method == 'POST':
        funcionarios_data = JSONParser().parse(request)
        funcionarios_Serializer = FuncionarioSerializer(data = funcionarios_data)
        if funcionarios_Serializer.is_valid():
            funcionarios_Serializer.save()
            return JsonResponse("operação realizada com sucesso", safe=False)
        return JsonResponse("erro na operação", safe = False)
    elif request.method == 'PUT':
        funcionarios_data = JSONParser().parse(request)
        funcionario = Funcionario.objects.get(matricula = funcionarios_data['matricula'])
        funcionarios_Serializer = FuncionarioSerializer(funcionario ,data = funcionarios_data)
        if funcionarios_Serializer.is_valid():
            funcionarios_Serializer.save()
            return JsonResponse("operação realizada com sucesso", safe=False)
        return JsonResponse("erro na operação", safe = False)
    elif request.method == 'DELETE':
        funcionarios = Funcionario.objects.get(matricula=id)
        funcionarios.delete()
        return JsonResponse("deletado com sucesso")