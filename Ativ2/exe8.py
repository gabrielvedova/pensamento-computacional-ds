#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 8.Escreva um programa que solicita ao usuário a massa do objeto e velocidade. Calcule a energia cinética usando a fórmula  E = (mv²) / 2.

m = float(input("Digite a massa do objeto: "))
v = float(input("Digite a velocidade do objeto: "))

energy = (m*v**2) / 2

print(f"Energia Cinética = {energy}")
