from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from cliente.api import viewsets as vsc
from deposito.api import viewsets as vsd
from hgbrasil.api import viewsets as vsb
from transferencia.api import viewsets as vst

from cliente.views import ClienteAPIView
from deposito.views import DepositoAPIView
from hgbrasil.views import HGBrasilAPIView
from transferencia.views import TransferenciaAPIView

route = routers.DefaultRouter()
route.register(r'cadastrar_cliente', vsc.ClienteViewset, basename='cliente')
route.register(r'fazer_deposito', vsd.DepositoViewset, basename='deposito')
route.register(r'fazer_transferencia', vst.TransferenciaViewSet, basename='transferencia')
route.register(r'HGBrasil', vsb.HGBrasilViewset, basename='hgbrasil')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('listar_clientes/', ClienteAPIView.as_view(), name='clientes'),
    path('depositos/', DepositoAPIView.as_view(), name='depositos'),
    path('financeiro/', HGBrasilAPIView.as_view(), name='financeiro'),
    path('transferencia/', TransferenciaAPIView.as_view(), name='transferencia')
]
