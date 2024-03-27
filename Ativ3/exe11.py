#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 11. Escreva um programa para verificar se o primeiro número ou o segundo número é maior, caso contrário eles são iguais.


num1, num2 = input("Digite dois números inteiros separados por um espaço cada um: ").split(" ")

num1, num2 = int(num1), int(num2)

if num1 < num2:
    print(f'{num1} é menor que {num2}')
elif num2 < num1:
    print(f'{num1} é maior que {num2}')
else:
    print('Os números são iguais')
