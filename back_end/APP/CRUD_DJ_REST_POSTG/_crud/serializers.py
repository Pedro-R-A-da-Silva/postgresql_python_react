from rest_framework import serializers
from _crud.models import Atividade,Funcionario,Situação

class AtivividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = ('sede','lotaçao','cargo')

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('matricula','nome','ativo','setor','foto')

class SituaçãoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situação
        fields = ('operacional','motivo')