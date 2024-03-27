#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 15.Escreva um programa para receber duas notas, uma para a prova 1 e a outra para a prova 2. Então verifique se o estudante foi aprovado ou reprovado em cada uma delas.

while True:
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))

    if n1 > 10 or n1 < 0 or n2 > 10 or n2 < 0:
        print("Pelo menos uma das provas está com uma nota inexistente")
    elif n1 < 6 or n2 < 6:
        print('Foi reprovado em pelo menos uma das provas')
        break
    else:
        print("Aprovado")
        break
