from rest_framework import serializers

from .models import Metric


class DynamicFieldsMetricSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs['context']['request'].query_params.get('group_by', None)
        super(DynamicFieldsMetricSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            fields = fields.split(',')
            default_fields = {'impressions_sum', 'clicks_sum', 'installs_sum', 'spend_sum', 'revenue_sum', 'cpi'}
            allowed = set(fields) | default_fields
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class MetricGroupBySerializer(DynamicFieldsMetricSerializer):
    impressions_sum = serializers.IntegerField()
    clicks_sum = serializers.IntegerField()
    installs_sum = serializers.IntegerField()
    spend_sum = serializers.FloatField()
    revenue_sum = serializers.FloatField()
    cpi = serializers.SerializerMethodField()

    def get_cpi(self, obj):
        return round(obj['spend_sum'] + obj['revenue_sum'] / obj['installs_sum'])

    class Meta:
        model = Metric
        fields = ('date', 'channel', 'country', 'os', 'impressions_sum',
                  'clicks_sum', 'installs_sum', 'spend_sum', 'revenue_sum', 'cpi')


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'
