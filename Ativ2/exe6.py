#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 6.Escreva um programa que solicita ao usuário o raio do círculo e calcule essa área usando a fórmula A = π * raio²
from math import pi

raio = float(input("Digite o tamanho do raio: "))

area = pi * raio**2

print(f"A área do círculo é: {area}")
