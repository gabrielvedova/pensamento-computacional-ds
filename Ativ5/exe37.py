#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 37.Qual será o resultado do seguinte código abaixo?
# OBS.: estou copiando os códigos para mostrar os resultados como vai ser

x = 10

if x >= 10:
    x = x * 5
    y = x - 10
if x < 20:
    x = x * 2
    y = x + 10
print(x, y)


"""
Resposta:
    Irá ter a seguinte resposta no terminal:
        50 40
    Isso acontece porque existe dois if, então o interpretador python ele só
    irá ler a segunda condição, se a primeira for falsa, algo que não acontece
    no código fonte.
"""
