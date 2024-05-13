#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 37.Peça ao usuário para digitar a primeira linha de uma canção infantil e exibir o comprimento da corda. Peça um número inicial e um número final e então tente exibir apenas aquela seção do texto (lembre-se que o Python inicia contando a partir de 0 e não 1).

text = input('Digite a primeira linha de uma canção preferida: ')

st_num = int(input('Número inicial: '))
en_num = int(input('Número final: '))
print(f'O tamanho da canção é {len(text)}. A seção recortada da canção é: {text[st_num:en_num]}')