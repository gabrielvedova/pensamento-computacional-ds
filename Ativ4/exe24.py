#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 24.Escreva um programa que peça a altura (ex. 1.78) e o peso (80.5) do usuário e em seguida calcule o imc, informando também se está abaixo do peso, se está com peso normal, se está com sobrepeso, se está com obesidade ou se está com obesidade grave.

altura = float(input('Me diga sua altura: '))
peso = float(input('Me diga o seu peso: '))

imc = peso / altura**2

if imc < 18.6:
    print('Abaixo do peso')
elif imc > 18.5 and imc < 25:
    print('Peso ideal')
elif imc > 24.9 and imc < 30:
    print('Levemente acima do peso')
elif imc > 29.9 and imc < 35:
    print('Obesidade Grau I')
elif imc > 34.9 and imc < 40:
    print('Obesidade Grau II(severa)')
elif imc > 39.9:
    print('Obesidade Grau III(mórbida)')
else:
    print("How it's possible...")