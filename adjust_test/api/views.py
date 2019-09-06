from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters

from .models import Metric
from .serializers import MetricSerializer


class MetricsViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # TODO add date_to and date_from to filterset_fields
    filterset_fields = ['channel', 'country', 'os']
    ordering_fields = '__all__'
