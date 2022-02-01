from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from deposito.models import Deposito
from deposito.api import serializers

class DepositoAPIView(APIView):
    """
    API de depósitos do banco
    """
    def get(self, request):
        depositos = Deposito.objects.all()
        infos = serializers.DepositoSerializer(depositos, many=True)
        return Response(infos.data)

    def post(self, request):
        infos = serializers.DepositoSerializer(data=request.data)
        infos.is_valid(raise_exception=True)
        infos.save()
        return Response(infos.data, status=status.HTTP_201_CREATED)