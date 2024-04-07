#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 41.Qual será o resultado do seguinte código abaixo?
# OBS.: estou copiando os códigos para mostrar os resultados como vai ser

x = True
y = True
z = False

if not x or y:
    print(1)
elif not x or (not y and z):
    print(2)
elif (not x or y) or (y and x):
    print(3)
else:
    print(4)


"""
Resposta:
    O programa irá executar 1, pois a condição boleana é
    se não verdadeiro ou verdadeiro(not x or y)
"""
