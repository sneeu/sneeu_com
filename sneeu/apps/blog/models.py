import datetime

from django.contrib import admin
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    headline = models.CharField(max_length=255)
    slug = models.SlugField()
    standfirst = models.CharField(max_length=255, blank=True, null=True)
    copy = models.TextField(blank=True, null=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __unicode__(self):
        return self.headline

    def save(self):
        self.updated = datetime.datetime.now()
        if not self.pk:
            self.created = self.updated
        super(Post, self).save()
        cache.delete(self.get_absolute_url())
        cache.delete('/')

    @models.permalink
    def get_absolute_url(self):
        return 'post_detail', (), {'year': self.created.year,
            'month': str(self.created.month).zfill(2), 'slug': self.slug, }


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('headline', )}


admin.site.register(Post, PostAdmin)
