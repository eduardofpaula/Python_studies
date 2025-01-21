# %%

import random

numero = random.randint(0, 15)

print(numero)


def verificar_entrada():
    try:
        return int(input("Digite o numero secreto de 1 á 15: "))
    except ValueError as err:
        print(err)
        return "Digite uma entrada valida!"


def verifica_numero(n):

    n = verificar_entrada()

    while True:

        #  verifica se o numero é inteiro, se for imprime o numero e continua
        if type(n) == int:
            print(n)
            continue
        if 0 <= n <= 15:
            return n
        else:
            return "Digite um numero entre 0 e 15"


def verificar_sorte():

    sorte = random.randint(0, 15)

    while True:

        n = verificar_entrada()

        if n == sorte:
            print("Parabéns, você acertou!")
            break
        elif n < sorte:
            print("O numero secreto é maior!")
        elif n > sorte:
            print("O numero secreto é menor!")
        else:
            print("Digite um numero valido!")
            break


verificar_sorte()
