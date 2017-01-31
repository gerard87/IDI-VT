from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Line(models.Model):

    name = models.TextField()

    def __unicode__(self):
        return str(self.name)

class Tower(models.Model):

    name = models.TextField()
    line = models.ForeignKey(Line)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    altitude = models.DecimalField(max_digits=20, decimal_places=15)

    def __unicode__(self):
        return str(self.name)
