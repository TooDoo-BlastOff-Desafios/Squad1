from rest_framework import views
import requests
from hgbrasil.api import serializers
from rest_framework.response import Response
from django.http import JsonResponse

def dados_banco():
    lista_moedas = []
    lista_mercado = []
    lista_bitcoin = []
    lista_completa = []
    dicio_completo = {}
    dicio = {}

    url = "https://api.hgbrasil.com/finance?key=95d8801e"
    requisicao = requests.get(url)

    dados = requisicao.json()

    lista_moedas.append(dados['results']['currencies'])
    lista_mercado.append(dados['results']['stocks'])
    lista_bitcoin.append(dados['results']['bitcoin'])

    dicio_completo = {
        'moeda': lista_moedas,
        'mercado': lista_mercado,
        'bitcoin': lista_bitcoin
    }

    lista_completa.append(dicio_completo)

    dicio['infos'] = lista_completa

    #dicio_completo['moeda'] = lista_moedas
    #dicio_completo['mercado'] = lista_mercado
    #dicio_completo['bitcoin'] = lista_bitcoin

    #return JsonResponse(dicio_completo)
    return dicio

class HGBrasilAPIView(views.APIView):
    def get(self, request):
        requisicao = dados_banco()
        infos = serializers.HGBrasilSerializer(requisicao['infos'], many=True).data

        return Response(infos)