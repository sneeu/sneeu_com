import datetime

from django.db import models


class Service(models.Model):
    ff_id = models.CharField(max_length=36)
    name = models.CharField(max_length=36)
    icon = models.URLField(blank=True, null=True)
    profile_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ('name', )

    def __unicode__(self):
        return self.name


class Log(models.Model):
    ff_id = models.CharField(max_length=36)
    service = models.ForeignKey(Service)
    link = models.URLField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    published = models.DateTimeField()

    class Meta:
        ordering = ('-published', )

    def __unicode__(self):
        return self.title


class Media(models.Model):
    log = models.ForeignKey(Log)
    url = models.URLField()

    class Meta:
        ordering = ('log', 'url', )

    def __unicode__(self):
        return self.url
