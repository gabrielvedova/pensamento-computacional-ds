#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 28.Escreva um programa que imprima uma sequência de números (0 até 100, por exemplo).

while True:
    menor = int(input('Me diga um número: '))
    maior = int(input('Agora me diga um número bem maior que o anterior: '))

    if menor < maior:
        for i in range(menor-1, maior):
            i += 1
            print(i)
        break
    else:
        print('Errou a ordem né amigão')
