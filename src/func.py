import pickle
from os import unlink
from common import *

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'

def menu_eleitor():
    print("1-Novo Eleitor")
    print("2-Atualizar Eleitor")
    print("3-Novo Candidato")
    print("4-Atualizar Candidato")
    print("5-Listar Candidatos")
    print("6-Listar Eleitor")
    print("7-Votar")
    print("8-Limpar votos")
    print("9-Remover arquivos")
    print("10-Sair")
    op = int(input("Digite a opcao [1,2,3,4,5,6,7,8,9,10]: "))
    while op not in (1, 2, 3, 4, 5, 6, 7, 8,9,10):
        op = int(input("Digite a opcao [1,2,3,4,5,6,7,8,9,10]: "))
    return op

def inserir_candidato(candidatos):
    numero = int(input("Numero do Candidato: "))
    if numero in candidatos:
        raise Exception("Numero já existente: ")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
    candidato = Candidato(nome, RG, CPF, numero)
    candidatos[candidato.get_numero()] = candidato

    with open(FILE_CANDIDATOS, 'wb') as arquivo2:
        pickle.dump(candidatos, arquivo2)

    print('Candidato gravado com sucesso!')
    print(candidatos)

def inserir_eleitor(eleitores):
    titulo = int(input("Digite o Título: "))

    if titulo in eleitores:
        raise Exception("Titulo já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
    secao = input("Digite a secao: ")
    zona = input("Digite a zona: ")

    eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona, voto=0)
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

def votar(eleitores, candidatos):
    titulo = int(input("Digite o título do eleitor: "))
    if titulo in eleitores:
        eleitor = eleitores[titulo]
        print(f"Eleitor encontrado: {eleitor.get_nome()}")
        if eleitor.get_voto() == 0:
            print("Numeros:")
            for numero in candidatos:
                print(numero)
            voto = int(input("Digite o número do candidato: "))
            if voto in candidatos:
                candidato = candidatos[voto]
                eleitor.votar(candidato)

                with open(FILE_ELEITORES, 'wb') as arquivo:
                    pickle.dump(eleitores, arquivo)

                with open(FILE_CANDIDATOS, 'wb') as arquivo2:
                    pickle.dump(candidatos, arquivo2)

                print(f"Voto registrado para {candidato.get_nome()}")
            else:
                print("Candidato não encontrado.")
        else:
            print("Já votou")
    else:
        print("Eleitor não encontrado.")

def limpar_votos(candidatos,eleitores):
    for titulo in eleitores:
        eleitor = eleitores[titulo]
        eleitor.voto = 0
        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(eleitores, arquivo)
    for numero in candidatos:
        candidato = candidatos[numero]
        candidato._votos = 0
        with open(FILE_CANDIDATOS, 'wb') as arquivo2:
            pickle.dump(candidatos, arquivo2)
    print("Votos zerados")

def remover_arquivos():
    try:
        unlink('eleitores.pkl')
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum eleitor carregado!")

    try:
        unlink('candidatos.pkl')
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum candidato carregado!")


