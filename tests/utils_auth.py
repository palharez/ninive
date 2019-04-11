class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, matricula=123456):
        self._client.post('/', data={'matricula': matricula})

    def logout(self):
        self._client.get('/auth/logout')