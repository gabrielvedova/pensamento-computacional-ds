#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 26.Escreva um programa que leia dois números inteiros e verifica se o primeiro número é divisível pelo segundo


num1 = int(input('Me diga o número aí meu nobre: '))
num2 = int(input('Agora me diz outro: '))

if num1 % num2 == 0:
    print(f'{num1} é divisível por {num2}')
else:
    print(f'{num1} não é divisível por {num2}')
