#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 7.Escreva um programa que solicita ao usuário a largura e o comprimento de um retângulo e calcule o perímetro e a área do retângulo, exibindo-os na tela.

largura = float(input("Me diga a largura do retângulo: "))
comprimento = float(input("Me diga a comprimento do retângulo: "))

area = largura*comprimento
perimetro = largura*2 + comprimento*2

print(f'Área: {area}\nPerímetro: {perimetro}')
