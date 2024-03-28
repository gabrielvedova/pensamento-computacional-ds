#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 25.Escreva um programa que leia a idade do usuário e apresente uma mensagem, informando se o usuário é uma criança, adolescente, adulto ou idoso.


while True:
    idade = int(input('Me diga tua idade aí pai: '))

    if idade < 12 and idade > -1:
        print('Criança = "Quero ser adulto logo!"')
        break
    elif idade > 11 and idade < 18:
        print('Adolescente = criança com liberdade')
        break
    elif idade > 17 and idade < 65:
        print('Adulto = "Quero voltar a ser criança..."')
        break
    elif idade > 65 and idade < 116:
        print('Pode descansar idoso, tá perto do fim mesmo...')
        break
    else:
        print('Quer mentir pra mim?')