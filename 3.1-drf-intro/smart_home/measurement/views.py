# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import generics
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer



def CreateProject(request):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class UpdateProject(generics.UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementProject(generics.ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class ListProject(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class RetrieveProject(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer