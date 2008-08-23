from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=60)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    year = models.CharField(max_length=4)
    credit = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ('author', 'title', )

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'book_detail', (), {'book_slug': self.slug}


class Chapter(models.Model):
    book = models.ForeignKey(Book)
    chapter = models.IntegerField()
    copy = models.TextField()

    class Meta:
        ordering = ('book', 'chapter', )

    def __unicode__(self):
        return u'%s; Chapter %d' % (self.book, self.chapter, )

    @models.permalink
    def get_absolute_url(self):
        return 'chapter_detail', (), {'book_slug': self.book.slug,
            'chapter': self.chapter}
