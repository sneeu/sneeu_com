import pprint
import StringIO

from django.http import HttpResponse
from django.shortcuts import render_to_response

import friendfeed

from models import Service, Log, Media


def update(request):
    FF_USERNAME = u'sneeu'

    ff = friendfeed.FriendFeed()
    data = ff.fetch_user_feed(FF_USERNAME)
    n = 0

    pp = pprint.PrettyPrinter(indent=4)

    for entry in data['entries']:
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

                for content in entry_media['content'] + entry_media['thumbnails']:
                    if content['width'] < 500:
                        media, created = Media.objects.get_or_create(
                            url=content['url'],
                            defaults={'log': log}
                            )
                        if created:
                            n += 1
                        break
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

    log = StringIO.StringIO()
    pprint.pprint(data, log)

    return render_to_response('tumble/update.html', {'log': log.getvalue(), 'updated': n})
