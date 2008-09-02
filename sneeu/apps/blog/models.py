import datetime

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
    keywords = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    published = models.BooleanField(default=True)
    allow_comments = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created', )

    def __unicode__(self):
        return self.headline

    def save(self, *args, **kwargs):
        self.updated = datetime.datetime.now()
        if not self.pk:
            self.created = self.updated
        super(Post, self).save(*args, **kwargs)
        cache.delete(self.get_absolute_url())
        cache.delete('/')

    @models.permalink
    def get_absolute_url(self):
        return 'post_detail', (), {'year': self.created.year,
            'month': self.created.month, 'slug': self.slug}

    @models.permalink
    def get_add_comment_url(self):
        return 'add_comment', (), {'year': self.created.year,
            'month': self.created.month, 'slug': self.slug}

    def _get_comments_open(self):
        expiry = self.created + datetime.timedelta(days=6 * 7)
        now = datetime.datetime.now()
        return self.allow_comments and expiry > now

    comments_open = property(_get_comments_open)


class PostComment(models.Model):
    post = models.ForeignKey(Post)
    created = models.DateTimeField(blank=True, null=True)
    author_name = models.CharField(max_length=30, verbose_name=u"Name")
    author_url = models.URLField(verbose_name=u"URL", blank=True, null=True)
    copy = models.TextField(verbose_name=u"Comment")

    class Meta:
        ordering = ('post', 'created')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created = datetime.datetime.now()
        super(PostComment, self).save(*args, **kwargs)
        cache.delete(self.post.get_absolute_url())
        cache.delete('/')

    def get_absolute_url(self):
        return u'%s#c%s' % (self.post.get_absolute_url(), self.pk)
