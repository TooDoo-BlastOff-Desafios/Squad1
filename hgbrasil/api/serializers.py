from dataclasses import fields
from rest_framework import serializers
from hgbrasil import models

class HGBrasilSerializer(serializers.Serializer):
    moeda = serializers.JSONField()
    mercado = serializers.JSONField()
    bitcoin = serializers.JSONField()
        

