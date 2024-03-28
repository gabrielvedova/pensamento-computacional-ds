#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 23.Escreva um programa que leia o dia da semana e apresente uma mensagem informando se é um dia útil, se é um dia de fim de semana ou se é dia inválido.

while True:
    dia = [
        ['Sábado', 'Domingo'],
        ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
    ]

    qual_dia = input('Me dia em que dia da semana você está: ')

    if qual_dia in dia[0]:
        print('Final de semana')
        break
    elif qual_dia in dia[1]:
        print('Dia útil')
        break
    else:
        print('Dia inválido')
