from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters

from .models import Metric
from .serializers import MetricSerializer


class MetricsViewSet(viewsets.ModelViewSet):
    # TODO add allowed methods

    def get_queryset(self):
        queryset = Metric.objects.all()

        group_by_str = self.request.query_params.get('group_by', None)
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)

        group_by_list = []
        if group_by_str:
            group_by_list = group_by_str.split(',')

        # Group_by filters
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

        # Dates filters
        if date_from and date_to:
            queryset = queryset.filter(date__range=[date_from, date_to])
        elif date_from:
            queryset = queryset.filter(date__gt=date_from)
        elif date_to:
            queryset = queryset.filter(date__lt=date_to)

        # TODO add serializer if there are no group_by params
        return queryset

    serializer_class = MetricSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # # TODO add date_to and date_from to filterset_fields
    filterset_fields = ['channel', 'country', 'os']
    ordering_fields = '__all__'
