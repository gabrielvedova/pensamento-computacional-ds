#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 12. Escreva um programa que solicita três números e verifique qual deles é o maior.


num1, num2, num3 = input("Digite 3 números inteiros separados por um espaço cada um: ").split(" ")
num1, num2, num3 = int(num1), int(num2), int(num3)

lista = [num1, num3, num2]
lista.sort()

print(f"O maior número é {lista[-1]}")
