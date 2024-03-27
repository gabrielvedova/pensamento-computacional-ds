#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 20.Escreva um programa para receber três notas. Depois calcule a média dessas notas e verifique se o estudante foi aprovado, reprovado ou está em recuperação.

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))

media = (n1 + n2 + n3) / 3

if media >= 6:
    print("Aprovado")
elif media < 4:
    print('Reprovado')
else:
    print("Recuperação")
