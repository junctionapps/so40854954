from __future__ import unicode_literals

from django.db import models


class CustomGroup(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True)
    is_active = models.BooleanField(null=False, default=True)
    description = models.CharField(max_length=512)

    def __str__(self):
        return unicode(self.name).encode('utf-8')


class CustomUser(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True, db_index=True)
    group = models.ForeignKey(CustomGroup, related_name='users')
    is_active = models.BooleanField(null=False, default=True)

    def __str__(self):
        return unicode(self.name).encode('utf-8')


class CustomSettings(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
    group = models.ForeignKey(CustomGroup, null=True, blank=True)
    user = models.ForeignKey(CustomUser, null=True, blank=True)

    def __str__(self):
        return unicode(self.name).encode('utf-8')
