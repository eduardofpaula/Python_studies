# %%

alturas = []
altura1 = int(input('altura 1: '))
altura2 = int(input('altura 2: '))
altura3 = int(input('altura 3: '))
altura4 = int(input('altura 4: '))

alturas.extend([altura1, altura2, altura3, altura4])

print(alturas)

somaAlturas = 0
for i in alturas:
    somaAlturas += i

print(somaAlturas)

# %%

# Faça um programa que receba uma quantidade indefinida de valores correspondentes a “saldo em conta”, mas quando o usuário apertar “enter” sem digitar valor algum, o programa para de receber valores, e exibe a soma te todos os valores digitados anteriormente

total = 0

while True:

    entrada = input('digite um valor, ou não digite nada para terminar: ')
    if entrada == '':
        break

    total += float(entrada)

print('soma total ', total)


# %%

# Entrada: 556
# Saída: 0:9:16


def conversor(number):
    # segundos é o resto da divisão de number por 60
    segundos = number % 60

    # subtrai os segundos de number
    number -= segundos

    # divide number por 60 para obter os minutos
    minutos = number / 60

    # minutos é o resto da divisão de number por 60
    minutos = minutos % 60

    # subtrai os minutos de number
    number -= minutos

    # divide number por 3600 para obter as horas
    horas = int(number / 3600)

    print(f'{horas}:{int(minutos)}:{segundos}')


conversor(445)

# %%
area = 3.14
perimetro = 2 * 3.14

print(f'area: {area} perimetro: {perimetro}')

# %%

a = 50
b = 45

print(f'soma: {a + b}')

# %%

a = 100
b = 5

z = a**b

print(f'potenciação de {a} por {b}: {z}')

# %%

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

frase1 = f'{nome}, você não pode dirigir nem beber'
frase2 = f'{nome}, bebida liberada! Só não vale dirigir'
frase3 = f'{nome}, beba com muita moderação'

if idade < 18:
    print(frase1)
elif idade >= 18 and idade <= 65:
    print(frase2)
else:
    print(frase3)

# %%

a = int(input('Digite um numero: '))

if a % 2 == 0:
    print(f'O numero {a} é par')
else:
    print(f'O numero {a} é ímpar')

# %%

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

informacoes = {'nome': nome, 'idade': idade}

print(
    f"Meu nome é {informacoes['nome']} e minha idade é {informacoes['idade']}"
)

# %%

nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))
nota4 = int(input('Nota 4: '))

maior = 0
menor = 0
media = (nota1 + nota2 + nota3 + nota4) / 4

if nota1 > nota2 and nota1 > nota3 and nota1 > nota4:
    maior = nota1
elif nota2 > nota1 and nota2 > nota3 and nota2 > nota4:
    maior = nota2
elif nota3 > nota1 and nota3 > nota2 and nota3 > nota4:
    maior = nota3
else:
    maior = nota4

if nota1 < nota2 and nota1 < nota3 and nota1 < nota4:
    menor = nota1
elif nota2 < nota1 and nota2 < nota3 and nota2 < nota4:
    menor = nota2
elif nota3 < nota1 and nota3 < nota2 and nota3 < nota4:
    menor = nota3
else:
    menor = nota4

print(f'Média: {media}\n' f'Menor: {menor}\n' f'Maior: {maior}')

# %%

lista = [120, 'Python', 120.01, 'asw', False, [10, 20]]

print(
    f'Elemento -1: {lista[-1]},\n'
    f'Primeiro elemento: {lista[0]},\n'
    f'Último caractere do segundo elemento: {lista[1][-1]}'
)

# %%

str1 = input('Digite frase 1: ')
str2 = input('Digite frase 2: ')

print(f'{str1 + str2}')

# %%

notas = []

for i in range(4):
    nota = int(input(f'Digite a nota {i + 1}: '))
    notas.append(nota)

media = sum(notas) / len(notas)

print(
    f'Maior nota: {max(notas)}\n'
    f'Menor nota: {min(notas)}\n'
    f'Média: {media}'
)

# %%

a = int(input('Digite um numero: '))

if a > 1:
    for i in range(2, a):
        if (a % i) == 0:
            print('Não é primo')
            break
    else:
        print('É primo')
else:
    print('Não é primo')


# %%


def fibonacci(n):
    seq = [0, 1]
    ultimo = 0
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
        ultimo = seq[-1]
    return print(f'A posição {n} corresponde ao número {ultimo}')


print(fibonacci(10))

# %%


def inverter(frase='Esta é a frase original'):

    invertido = ''
    for i in frase:
        invertido = frase[::-1]

    print(invertido)


inverter()

# %%


def inverter_palavras(frase):
    # Divide a frase em palavras, inverte cada palavra e junta novamente
    palavras_invertidas = [palavra[::-1] for palavra in frase.split()]
    print(palavras_invertidas)
    return ' '.join(palavras_invertidas)


# Exemplo de uso
frase_original = 'Esta é a frase original'
frase_invertida = inverter_palavras(frase_original)

print('Frase original:')
print(frase_original)

print('\nFrase invertida:')
print(frase_invertida)

# %%


def contagem():

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print('Buzz')


contagem()

# %%


def fatorial(n):

    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


print(fatorial(5))

# %%

lista = [123, 435, 987, 1984, 2, 19, 423, -178, 320]


for i in lista:
    maior = lista.index(max(lista), 0, len(lista))
    menor = lista.index(min(lista), 0, len(lista))

print(
    f'O maior valor está na posição {maior}\n'
    f'O menor valor está na posição {menor}'
)

# %%


def tabuada(n):

    for i in range(0, 10):
        print(f'{n} X {i + 1} = {n * (i + 1)}')


tabuada(5)

# %%


def verificarPalindromo(palavra):

    # Remove os espaços e converte para minúsculas
    palavra = palavra.replace(' ', '').lower()
    # Verifica se a palavra é igual à ela mesma invertida
    return palavra == palavra[::-1]


print(verificarPalindromo('Ame a ema'))
