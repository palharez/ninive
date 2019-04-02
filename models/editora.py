class Editora:

    def __init__(self):
        self._id = None
        self._nome = None

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @id.setter
    def id(self, value):
        self._id = value

    @nome.setter
    def nome(self, value):
        self._nome = value


if __name__ == "__main__":
    a = Editora()
    a.id = 1
    print(a.id)
