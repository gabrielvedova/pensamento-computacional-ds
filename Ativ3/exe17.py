#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 17.Escreva um programa para ler três números inteiros. Depois some os três números e verifique se a soma é divisível por 5.


n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input('Terceiro número: '))

soma = n1 + n2 + n3

if soma % 5 == 0:
    print("A soma é divisível por 5")
else:
    print("A soma não é divisível por 5")
