from autor import Autor
from editora import Editora


class Livro:

    def __init__(self):
        self._tombo = None
        self._titulo = None
        self._entrada = None
        self._etq = None
        self._ano = None
        self._v = None
        self._ex = None
        self._editora = None
        self._autor = None
        self._status = None
        self._nomeclatura = None
        self._status_disponiveis = [
            'EMPRESTADO', 'ESTANTE', 'EXTRAVIADO', 'RESERVADO', 'PERDIDO']
        self._nomeclatura_disponiveis = ['LIN', 'LBR', 'POE', 'LES']

    @property
    def tombo(self):
        return self._tombo

    @tombo.setter
    def tombo(self, value):
        self._tombo = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def entrada(self):
        return self._entrada

    @entrada.setter
    def entrada(self, value):
        self._entrada = value

    @property
    def etq(self):
        return self._etq

    @etq.setter
    def etq(self, value):
        self._etq = value

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, value):
        self._ano = value

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, value):
        self._v = value

    @property
    def ex(self):
        return self._ex

    @ex.setter
    def ex(self, value):
        self._ex = value

    @property
    def editora(self):
        return self._editora

    @editora.setter
    def editora(self, value):
        self._editora = value

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, value):
        self._autor = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value in self._status_disponiveis:
            self._status = value

    @property
    def nomenclatura(self):
        return self._nomenclatura

    @nomenclatura.setter
    def nomenclatura(self, value):
        if value in self._nomeclatura_disponiveis:
            self._nomenclatura = value


if __name__ == "__main__":
    autor = Autor()
    autor.nome = "Eduardo"

    editora = Editora()
    editora.nome = "Palhares"

    livro = Livro()
    livro.titulo = "Andrade"
    livro.editora = editora
    livro.autor = autor

    print(
        f"Autor: {livro.autor.nome}, Livro: {livro.titulo} e Editora: {livro.editora.nome}")
