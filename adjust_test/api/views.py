from rest_framework import viewsets

from .models import Metric
from .serializers import MetricSerializer


class MetricsViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all()[:5]
    serializer_class = MetricSerializer
