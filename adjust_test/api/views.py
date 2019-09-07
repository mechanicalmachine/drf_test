from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters

from .models import Metric
from .serializers import MetricSerializer


class MetricsViewSet(viewsets.ModelViewSet):
    # TODO add allowed methods
    # http://127.0.0.1:8000/api/metrics/?country=US&channel=adcolony&ordering=-spend&group_by=country,channel

    def get_queryset(self):
        queryset = Metric.objects.all()

        group_by_str = self.request.query_params.get('group_by', None)

        if not group_by_str:
            return queryset

        group_by_list = group_by_str.split(',')

        allowed_groups = {'date', 'channel', 'country', 'os'}
        if set(group_by_list) <= allowed_groups:
            queryset = queryset.values(
                *group_by_list
            ).annotate(
                impressions_sum=Sum('impressions'),
                clicks_sum=Sum('clicks'),
                installs_sum=Sum('installs'),
                spend_sum=Sum('spend'),
                revenue_sum=Sum('revenue')
            )

        return queryset

    serializer_class = MetricSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # # TODO add date_to and date_from to filterset_fields
    filterset_fields = ['date', 'channel', 'country', 'os']
    ordering_fields = '__all__'
