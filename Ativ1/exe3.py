#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 3.Crie um programa que calcule e exiba a média aritmética de três notas informadas pelo usuário.

n2 = int(input('Me diga o sua média do 1° bimestre: '))
n3 = int(input('Me diga o sua média do 2° bimestre: '))
n1 = int(input('Me diga o sua média do 3° bimestre: '))

media = (n1 + n2 + n3)/3

if media < 6:
    print(f'Você está com {media} na média! Falta {6 - media} para passar de ano')
elif media >= 6:
    print(f'Você passou de ano com {media} pontos na média!')
