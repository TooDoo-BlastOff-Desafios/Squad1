from rest_framework import viewsets
from hgbrasil.api import serializers
from hgbrasil import models
from hgbrasil.views import dados_banco
from rest_framework.response import Response

class HGBrasilViewset(viewsets.ModelViewSet):
    serializer_class = serializers.HGBrasilSerializer
    queryset = models.HGBrasil.objects.all()
    