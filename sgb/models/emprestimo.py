class Emprestimo:

    def __init__(self):
        self._retirada = None
        self._devolucao = None
        self._livro = None
        self._socio = None

    @property
    def retirada(self):
        return self._retirada

    @retirada.setter
    def retirada(self, value):
        self._retirada = value

    @property
    def devolucao(self):
        return self._devolucao

    @devolucao.setter
    def devolucao(self, value):
        self._devolucao = value

    @property
    def livro(self):
        return self._livro

    @livro.setter
    def livro(self, value):
        self._livro = value

    @property
    def socio(self):
        return self._socio

    @socio.setter
    def socio(self, value):
        self._socio = value
