from frota import *


def sim_carro(carro: Carro):
    print('1- Ligar motor')

    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro)


if __name__ == "__main__":
    print('Cadastre o carro 1')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, motor=False)

    print('Cadastre o carro 2')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, motor=False)
    '''
    Controlando 2 carro até ele atingir 10000 Km
    '''
    while carro1.odometro < 300 and carro2.odometro < 300:
        try:
            op_carro = 0
            while op_carro not in (1, 2):
                op_carro = int(input('Qual carro controlar 1 ou 2:'))
            if op_carro == 1:
                sim_carro(carro1)
            else:
                sim_carro(carro2)

        except Exception as e:
            print("Erro!")
            print(e)

    print(carro1)
    print(carro2)
