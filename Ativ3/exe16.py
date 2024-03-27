#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 16.Escreva um programa que receba duas notas (uma nota para a prova1 e a outra para a prova2). Depois calcule a média aritmética simples dessas notas e verifique se o estudante é aprovado ou reprovado.


n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = (n1 + n2) / 2

if media < 6:
    print("Reprovado")
else:
    print("Aprovado")