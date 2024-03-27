#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 18. Escreva um programa para ler três números inteiros. Depois some os três números e verifique se a soma é positiva, negativa ou igual a zero.


n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input('Terceiro número: '))

soma = n1 + n2 + n3

if soma > 0:
    print("A soma é positivo")
elif soma < 0:
    print("A soma é negativo")
else:
    print("A soma é igual a 0")
