#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 9.Escreva um programa que solicita ao usuário o valor do raio de uma esfera. Calcule o volume da esfera utilizando a fórmula V = (4/3) * pi * raio³
from math import pi

raio = float(input("Digite o tamanho do raio: "))

volume = 4/3 * pi * raio**3

print(f"O volume da esfera é: {volume}")
