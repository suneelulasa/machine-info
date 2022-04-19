import datetime

from django.db import models


# Create your models here.
class Blog(models.Model):
    companyName = models.CharField(max_length=50)
    # image = models.ImageField(upload_to='images')
    how_to_create = models.CharField(max_length=50)
    madein = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.companyName


class Meta:
    model = Blog
    fields = '__all__'
