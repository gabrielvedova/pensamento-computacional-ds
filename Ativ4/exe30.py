#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 30.Escreva um programa simples para calcular a quantidade de vogais em uma frase digitada pelo usuário.

frase = input('Escreva o que quiser: ')

vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'â', 'ê', 'ô', 'ã', 'õ']
num = 0

for i in vogais:
    for j in frase:
        if j == i:
            num += 1

print(num)
