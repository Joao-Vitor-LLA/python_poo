class Pessoa:
    __nome : str
    __RG : str
    __CPF : str

    def __init__(self, nome, RG, CPF):
        self.__nome = nome
        self.__RG = RG
        self.__CPF = CPF

    def __str__(self):
        info = (f'Nome: {self.__nome}\n'
               f'RG: {self.__RG}\n'
               f'CPF: {self.__CPF}\n')
        return info

    def __repr__(self):
        return f"Pessoa(nome='{self.__nome}', RG='{self.__RG}', CPF='{self.__CPF}')"

class Eleitor(Pessoa):
    __titulo : int
    secao : int
    zona : int
    __voto : int

    def __init__(self, nome, RG, CPF, titulo, secao, zona, voto):
        super().__init__(nome, RG, CPF)
        self.__titulo = titulo
        self.secao = secao
        self.zona = zona
        self.__voto = voto

    def __str__(self):
        info = super().__str__()
        info += (f'Titulo: {self.__titulo}\n'
                 f'Seção: {self.secao}\n'
                 f'Zona: {self.zona}\n'
                 f'Voto: {self.__voto}\n')
        return info

    def __repr__(self):
        return f"Eleitor({super().__repr__()}, titulo='{self.__titulo}', secao='{self.secao}', zona='{self.zona}',voto='{self.__voto}'"

    def get_titulo(self):
        return self.__titulo
    def get_voto(self):
        return self.__voto

    def votar(self, candidato):
        if self.__voto == candidato.get_numero():
            candidato.incrementar_votos()

class Candidato(Pessoa):
    _numero: int
    _votos: int = 0

    def __init__(self, nome, RG, CPF, numero):
        super().__init__(nome, RG, CPF)
        self._numero = numero

    def __str__(self):
        info = super().__str__()
        info += (f'Numero: {self._numero}\n'
                 f'Votos: {self._votos}\n')
        return info

    def __repr__(self):
        return (f"Candidato({super().__repr__()}, "
                f"numero={self._numero}, votos={self._votos})")

    def get_numero(self):
        return self._numero

    def incrementar_votos(self):
        self._votos += 1

    def get_votos(self):
        return self._votos
