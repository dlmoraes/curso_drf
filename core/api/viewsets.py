# coding = utf-8

from rest_framework.viewsets import ModelViewSet

from ..models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer