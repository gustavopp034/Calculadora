# Este é o primeiro programa de uma calculadora q sera melhor desenvolvida ao longo do tempo consertando erros e add ideias.
    # Bibliotecas
import math
from time import sleep
    # Variaveis
n1 = ''
n2 = ''
res = ''
op = '0'
nome = ''
per = 'S'
    # Inicio
print('\033[31m=-\033[m'*30)
print(' '*12,'Bem vindo a calculadora Max')
print('\033[31m=-\033[m'*30)
nome = input(str('Por favor digite seu nome: ')).upper()
print(f'Prazer, {nome}!')
sleep(1)
print('\033[33mVamos começar a calcular :-) \033[m')
sleep(1)
     # Corpo
while per == 'S':
  while op == '0':
    print ('*' * 20)
    print (' ' * 7, 'MENU')
    print ('*' * 20)
    print('Escolha uma das opções: ')
    print ('\033[31m[1] Adição\033[m')
    sleep (1)
    print ('\033[31m[2] Subtração\033[m')
    sleep (1)
    print ('\033[31m[3] Divisão\033[m')
    sleep (1)
    print ('\033[31m[4] Multiplicação\033[m')
    sleep (1)
    print('\033[31m[5] Mais opções\033[m')
    op = input(f'{nome} qual das opções você deseja? ')
    if op == '1':
            print('Você escolheu ADIÇÃO')
            n1 = float(input(f'{nome} digite o primeiro número:'))
            n2 = float(input(f'{n1} + '))
            res = n1 + n2
            sleep(2)
            print(f'\033[31mO resultado de {n1} + {n2} é igual a:\033[m')
            sleep(0.5)
            print(f'\033[32m>>>>{res}\033[m')
    elif op == '2':
            print('Você escolheu SUBTRAÇÃO')
            n1 = float(input(f'{nome} digite o primeiro número: '))
            n2 = float(input(f'{n1} - '))
            res = n1 - n2
            sleep(2)
            print(f'\033[31mO resultado de {n1} - {n2} é igual a:\033[m')
            sleep(0.5)
            print(f'\033[32m>>>>{res}\033[m')
    elif op == '3':
            print('Você escolheu DIVISÃO')
            n1 = float(input(f'{nome} digite o primeiro número: '))
            n2 = float(input(f'{n1} /  '))
            res = n1 / n2
            sleep(2)
            print(f'\033[31mO resultado de {n1} / {n2} é igual a:\033[m')
            sleep(0.5)
            print(f'\033[32m>>>>{res}\033[m')
    elif op == '4':
            print('Você escolheu MULTIPLICAÇÃO')
            n1 = float(input(f'{nome} digite o primeiro número: '))
            n2 = float(input(f'{n1} *  '))
            res = n1 * n2
            sleep(2)
            print(f'\033[31mO resultado de {n1} * {n2} é igual a:\033[m')
            sleep(0.5)
            print(f'\033[31m>>>>{res}\033[m')
    elif op == '5':
        print('\033[31m[6] Porcentagem\033[m')
        sleep(1)
        print('\033[31m[7] Raiz Quadrada\033[m')
        sleep(1)
        print('\033[31m[8] Equação de segundo grau\033[m')
        sleep(1)
        print('\033[31m[0] Voltar\033[m')
        op = input('Digite a opção desejada: ')
        if op == '6':
            n1 = float(input('Qual o número que você deseja saber a porcentagem: '))
            n2 = float(input('Qual a porcentagem: '))
            res = n1 * n2 / 100
            print(f'A porcentagem de {n1} é {res}')
        elif op == '7':
            n1 = float(input('Digite o número: '))
            res = math.sqrt(n1)
            print(f'A raiz quadrada de {n1} é {res}')
        elif op == '8':
            n1 = float(input('Digite o número da equação: '))
            res = n1 * n1
            print(f'{n1} elevado ao quadrado é {res}')
        else:
            print (f'Eii {nome} esta é uma \033[31mOPÇÃO INVÁLIDA\033[m')
            op = '0'
            sleep(1)
    else:
        print(f'Eii {nome} esta é uma \033[31mOPÇÃO INVÁLIDA\033[m')
        op = '0'
        sleep(1)
  per = str(input('Deseja fazer mais algum calculo? [S/N]')).upper()
print('Obrigado por usar nosso app!')
print('Versão 2.0')