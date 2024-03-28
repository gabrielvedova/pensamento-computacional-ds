#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 29.Escreva um programa para ler números inteiros digitados pelo usuário, depois somar todos eles e exibir o resultado da soma. Para encerrar o programa utilize um valor negativo.


soma = 0

while True:
    numero = int(input("Digite um número (negativo para encerrar): "))

    if numero < 0:
        break
    if numero >= 0:
        soma += numero
        print(f"A soma dos números positivos é: {soma}")
