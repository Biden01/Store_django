from django.db import models

# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name