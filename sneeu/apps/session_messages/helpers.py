SESSION_VALUE = 'smessages'


def add_message(request, message):
    request.session.setdefault(SESSION_VALUE, list()).append(message)
    request.session.modified = True
