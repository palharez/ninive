class Socio:

    def __init__(self):
        self._id = None
        self._nome = None
        self._rg = None
        self._nasc = None
        self._email = None
        self._associacao = None
        self._nome_pai = None
        self._nome_mae = None
        self._cidade = None
        self._bairro = None
        self._logradouro = None
        self._num = None
        self._tel_res = None
        self._cel_1 = None
        self._cel_2 = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def rg(self):
        return self._rg

    @rg.setter
    def rg(self, value):
        self._rg = value

    @property
    def nasc(self):
        return self._nasc

    @nasc.setter
    def nasc(self, value):
        self._nasc = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def associacao(self):
        return self._associacao

    @associacao.setter
    def associacao(self, value):
        self._associacao = value

    @property
    def nome_pai(self):
        return self._nome_pai

    @nome_pai.setter
    def nome_pai(self, value):
        self._nome_pai = value

    @property
    def nome_mae(self):
        return self._nome_mae

    @nome_mae.setter
    def nome_mae(self, value):
        self._nome_mae = value

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, value):
        self._cidade = value

    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, value):
        self._bairro = value

    @property
    def logradouro(self):
        return self._logradouro

    @logradouro.setter
    def logradouro(self, value):
        self._logradouro = value

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value

    @property
    def tel_res(self):
        return self._tel_res

    @tel_res.setter
    def tel_res(self, value):
        self._tel_res = value

    @property
    def cel_1(self):
        return self._cel_1

    @cel_1.setter
    def cel_1(self, value):
        self._cel_1 = value

    @property
    def cel_2(self):
        return self._cel_2

    @cel_2.setter
    def cel_2(self, value):
        self._cel_2 = value
