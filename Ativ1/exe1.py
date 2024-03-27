#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 1.Escreva um programa que solicite ao usuário dois números e exiba a soma, subtração, multiplicação e divisão entre eles.

pergunta = input('Me diga os números os separando com um espaço: ')

# Separando os dados recebidos do input
n1, n2 = pergunta.split(' ')

# Convertendo os dados de str para int
num1 = int(n1)
num2 = int(n2)

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1*num2
divisao = num1 / num2

print(f'Resultados:\nAdição: {soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao}\nDivisão: {divisao}')
