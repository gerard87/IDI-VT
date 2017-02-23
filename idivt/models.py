from __future__ import unicode_literals

from django.db import models

class Line(models.Model):

    name = models.TextField()
    visibility = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.name

class Tower(models.Model):

    name = models.TextField()
    line = models.ForeignKey(Line)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    altitude = models.DecimalField(max_digits=20, decimal_places=15)


    def __unicode__(self):
        return u'%s' % self.name
