class NotificationHidingMiddleware(object):
    def process_request(self, request):
        if not 'hide_rss' in request.session:
            request.session['hide_rss'] = True
        print request.session['hide_rss']

    def process_response(self, request, response):
        request.session['hide_rss'] = False
        print request.session['hide_rss']
        return response