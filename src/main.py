import pickle
import traceback

from common import *

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'
def menu_eleitor():
    print("1-Novo Eleitor")
    print("2-Atualizar Eleitor")
    print("3-Novo CAndidato")
    print("4-Atualizar Candidato")
    print("5-Listar Candidatos")
    print("6-Listar Eleitor")
    print("7-Sair")
    op = int(input("Digite a opcao [1,2,3,4,5,6,7]: "))
    while op not in (1, 2, 3,4,5,6,7):
        op = int(input("Digite a opcao [1,2,3,4,5,6,7]: "))
    return op

def inserir_candidato(candidatos):
    numero = int(input("Numero do Candidato: "))
    if numero in candidatos:
        raise Exception("Numero já existente: ")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
    candidato = Candidato(nome, RG, CPF, numero,)
    candidatos[candidato.get_numero()] = candidato
def inserir_eleitor(eleitores):
    titulo = int(input("Digite o Títlulo: "))

    if titulo in eleitores:
        raise Exception("Titulo já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
    secao = input("Digite a secao: ")
    zona = input("Digite a zona: ")
    voto = int(input("Digite seu voto: "))

    with open(FILE_CANDIDATOS, 'wb') as arquivo2:
        pickle.dump(candidatos, arquivo2)

    print('Candidato gravado com sucesso!')
    print(candidatos)

    eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona,voto)
    eleitores[eleitor.get_titulo()] = eleitor

    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)

    print('Eleitor gravado com sucesso!')
    print(eleitor)

def atualizar_eleitor(eleitores):
    titulo = int(input('Digite o titulo do eleitor: '))

    if titulo in eleitores:
        eleitor = eleitores[titulo]
        print(eleitor)
        secao = input("Digite a nova secao: ")
        zona = input("Digite a nova zona: ")
        eleitor.secao = secao
        eleitor.zona = zona

        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(eleitores, arquivo)

        print('Atualizados dados do eleitor!')
        print(eleitor)
    else:
        raise Exception('Titulo inexistente')

def atualizar_candidato(candidatos):
    numero = int(input("Numero do Candidato: "))
    candidato = candidatos[numero]
    nome = input("Novo nome: ")
    candidato.nome = nome
    with open(FILE_CANDIDATOS, 'wb') as arquivo2:
        pickle.dump(candidatos, arquivo2)

    print('Candidato gravado com sucesso!')
    print(candidatos)

def listar_candidatos(candidatos):
    for i in candidatos.values():
        print(i)

def listar_eleitor(eleitores):
    for c in eleitores.values():
        print(c)

if __name__ == "__main__":
    eleitores = {} #dicionário a chave será o titulo
    try:
        print("Carregando arquivo de eleitores ...")

        with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum eleitor carregado!")
    candidatos = {}
    try:
        print("Carregando arquivo de candidatos ...")

        with open(FILE_CANDIDATOS, 'rb') as arquivo:
            candidatos = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum eleitor carregado!")

    opcao = 1
    while opcao in (1,2,3,4,5,6,7):
        try:
            opcao = menu_eleitor()

            if opcao == 1:
                inserir_eleitor(eleitores)

            elif opcao == 2:
                atualizar_eleitor(eleitores)

            elif opcao == 3:
                inserir_candidato(candidatos)

            elif opcao == 4:
                atualizar_candidato(candidatos)

            elif opcao == 5:
                listar_candidatos(candidatos)

            elif opcao == 6:
                listar_eleitor(eleitores)

            elif opcao == 7:
                print("Saindo!")
                break
        except Exception as e:
            traceback.print_exc()
            print(e)