import friendfeed
import pprint

from django.http import HttpResponse

from models import Service, Log, Media


def update(request):
    FF_USERNAME = u'sneeu'

    ff = friendfeed.FriendFeed()
    n = 0
    for entry in ff.fetch_user_feed(FF_USERNAME)['entries']:
        service, __ = Service.objects.get_or_create(
            ff_id=entry['service']['id'],
            defaults={
                'name': entry['service']['name'],
                'icon': entry['service']['iconUrl'],
                'profile_url': entry['service']['profileUrl'],
            })
        if entry['media']:
            for entry_media in entry['media']:
                entry_comment = None
                for comment in entry['comments']:
                    if comment['user']['nickname'] == FF_USERNAME:
                        entry_comment = comment['body']

                log, __ = Log.objects.get_or_create(
                    link=entry_media['link'],
                    defaults={
                        'ff_id': entry['id'],
                        'service': service,
                        'title': entry_media['title'],
                        'comment': entry_comment,
                        'published': entry['published'],
                    })

                media, created = Media.objects.get_or_create(
                    url=entry_media['content'][0]['url'],
                    defaults={'log': log}
                    )
                if created:
                    n += 1
        else:
            entry_comment = None
            for comment in entry['comments']:
                if comment['user']['nickname'] == FF_USERNAME:
                    entry_comment = comment['body']

            log, created = Log.objects.get_or_create(
                link=entry['link'],
                defaults={
                    'ff_id': entry['id'],
                    'service': service,
                    'title': entry['title'],
                    'comment': entry_comment,
                    'published': entry['published'],
                })
            if created:
                n += 1

    return HttpResponse('%d' % n)
