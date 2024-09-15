from typing import List

class Quiz:

    __acertos : int
    __erros: int
    def __init__(self,  __acertos, __erros):
        self.__acertos = __acertos
        self.__erros = __erros

    def calcular_pontos(self):
        return self.__acertos - self.__erros

    def get_acertos(self):
        return self.__acertos

    def get_erros(self):
        return self.__erros

    def __str__(self):
        out = f'Acertos: {self.__acertos} Erros: {self.__erros} Pontos: {self.calcular_pontos()}'
        return out

class Quiz2A(Quiz):
    def __init__(self, __acertos, __erros):
        super().__init__(__acertos, __erros)

    def caucular_pontos(self):
        return self.get_acertos() - (4 * self.get_erros())

class Quiz3A(Quiz):
    def __init__(self, __acertos, __erros):
        super().__init__( __acertos, __erros)

    def caucular_pontos(self):
        return self.get_acertos() - (2 * self.get_erros())

class Aluno:
    __maticula : int
    __aluno : str
    __quizes : List[Quiz]

    def __init__(self,__matricula,__alulo,__quizes):
        self.__maticula = __matricula
        self.__aluno = __alulo
        self.__quizes = __quizes

    def __str__(self):
        out =f'Matricula: {self.__maticula} Aluno: {self.__aluno}'
        pt = 0
        for i in self.__quizes:
            pt += i.calcular_pontos()
        out += f'Pontos Totais = {pt}'
        return out

class Disciplina:
    __nome : str
    __professor : str
    __ano : int
    __semestre : int
    __alunos : List[Aluno] = []

    def __init__(self,nome : str,professor : str,ano : int,semestre : int):
        self.__nome = nome
        self.__professor = professor
        self.__ano = ano
        self.__semestre = semestre

    def add_aluno(self,a : Aluno):
        if a not in self.__alunos:
            self.__alunos.append(a)

        else:
            raise Exception("Aluno já existe")

    def __str__(self):
        out = f'Nome da disciplina {self.__nome}\n'
        out += f'Professor: {self.__professor}\n'
        out += f'{self.__ano}--{self.__semestre}\n'
        for aluno in self.__alunos:
            out += aluno.__str__()
        return out