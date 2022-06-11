from django.db import models


class ServiceArea(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    provider = models.ForeignKey('providers.Provider',
                                 on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    geo_json_polygon = models.JSONField(blank=True, null=True)

    class Meta:
        ordering = ['created']
