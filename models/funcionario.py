class Funcioanrio:

    def __init__(self):
        self._matricula = None
        self._nome = None
        self._cargo = None

    @property
    def matricula(self):
        return self._matricula

    @property
    def nome(self):
        return self._nome

    @property
    def cargo(self):
        return self._cargo

    @matricula.setter
    def matricula(self, value):
        self._matricula = value

    @nome.setter
    def nome(self, value):
        self._nome = value

    @cargo.setter
    def cargo(self, value):
        self._cargo = value


if __name__ == "__main__":
    f = Funcioanrio()
    f.cargo = "TI"
    print(f.cargo)
