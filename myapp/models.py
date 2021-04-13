from django.db import models


# Create your models here.


class st(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
