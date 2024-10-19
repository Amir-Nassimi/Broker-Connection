from django.db import models

class MyData(models.Model):
    id = models.IntegerField(primary_key=True)
    data_field = models.CharField(max_length=500)
    created_at = models.DateTimeField()

    class Meta:
        ordering = ['created_at']
