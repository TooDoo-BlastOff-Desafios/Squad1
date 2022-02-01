from multiprocessing import managers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from transferencia.models import Transferencia
from transferencia.api import serializers

class TransferenciaAPIView(APIView):
    """
    API de transferências do banco
    """
    def get(self, request):
        depositos = Transferencia.objects.all()
        infos = serializers.TransferenciaSerializer(depositos, many=True)
        return Response(infos.data)

    def post(self, request):
        infos = serializers.TransferenciaSerializer(data=request.data)
        infos.is_valid(raise_exception=True)
        infos.save()
        return Response(infos.data, status=status.HTTP_201_CREATED)

