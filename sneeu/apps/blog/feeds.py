from django.contrib.syndication.feeds import Feed

from models import Post


class BlogFeed(Feed):
    title = "sneeu.com"
    link = '/blog/'
    description = ""
    author_name = "John Sutherland"
    author_email = "john@sneeu.com"
    author_link = 'http://sneeu.com/john/'

    def items(self):
        return Post.objects.all()[:10]

    def item_pubdate(self, item):
        return item.created


FEEDS = {
    'feed': BlogFeed,
}