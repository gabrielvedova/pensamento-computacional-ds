#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 5.Escreva um programa que calcule o IMC de um indivíduo, utilizando a fórmula IMC = peso / altura².

peso = float(input('Me diga o seu peso: '))
altura = float(input('Me diga sua altura: '))

imc = peso / altura**2

if imc >= 17 and imc < 18.4:
    print(f'Magreza leve. IMC: {imc}')
elif imc >= 16 and imc < 16.9:
    print(f'Magreza moderada. IMC: {imc}')
elif imc < 16:
    print(f'Magreza grave. IMC: {imc}')
elif imc >= 18.5 and imc <= 24.9:
    print(f'Peso saudável. IMC: {imc}')
elif imc >= 25 and imc < 29.9:
    print(f'Sobrepeso. IMC: {imc}')
elif imc >= 30 and imc < 34.9:
    print(f'Obesidade grau 1. IMC: {imc}')
elif imc >= 35 and imc < 39.9:
    print(f'Obesidade severa. IMC: {imc}')
elif imc >= 40:
    print(f'Obesidade mórbida. IMC: {imc}')
