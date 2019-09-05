from django.db import models


class Metric(models.Model):
    date = models.DateField()
    channel = models.CharField(max_length=20)
    country = models.CharField(max_length=2)
    os = models.CharField(max_length=20)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()
