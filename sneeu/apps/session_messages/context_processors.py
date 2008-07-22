from UserList import UserList


from helpers import SESSION_VALUE


class SessionMessages(UserList):
    def __init__(self, session):
        self.session = session
        self.data = self.session.get(SESSION_VALUE) or list()

    def __getitem__(self, idx):
        if SESSION_VALUE in self.session:
            del self.session[SESSION_VALUE]
        return self.data[idx]


def session_messages(request):
    return {'smessages': SessionMessages(request.session)}
