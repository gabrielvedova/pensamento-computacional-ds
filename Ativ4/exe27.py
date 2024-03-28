#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 27.Escreva um programa que apresente uma sequência de números (1 até 10, por exemplo). Para isso, utilize a instrução while e instrução for.


while True:
    menor = int(input('Me diga um número: '))
    maior = int(input('Agora me diga um número bem maior que o anterior: '))

    if menor < maior:
        for i in range(menor-1, maior):
            i += 1
            print(i)
        print('______________________')

        while menor <= maior:
            menor += 1
            print(menor)
        break
    else:
        print('Errou a ordem né amigão')
