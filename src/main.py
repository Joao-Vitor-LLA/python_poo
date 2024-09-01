import traceback
from func import *


if __name__ == "__main__":
    eleitores = {}
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
        print("Arquivo nao encontrado, nenhum candidato carregado!")

    opcao = 1
    while opcao in (1, 2, 3, 4, 5, 6, 7, 8,9,10):
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
                votar(eleitores, candidatos)

            elif opcao == 8:
                limpar_votos(candidatos, eleitores)

            elif opcao == 9:
                remover_arquivos()

            elif opcao == 10:
                print("Saindo!")
                break
        except Exception as e:
            traceback.print_exc()
            print(e)
