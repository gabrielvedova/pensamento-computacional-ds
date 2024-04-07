#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 40.Qual será o resultado do seguinte código abaixo?
# OBS.: estou copiando os códigos para mostrar os resultados como vai ser

x = int(input("Entre com um número entre 1-7: "))

if x == 7:
    print("Domingo")
elif x == 6:
    print("Segunda")
elif x == 5:
    print("Terça-feira")
elif x == 4:
    print("Quarta-feira")
elif x == 3:
    print("Quinta-feira")
elif x == 2:
    print("Sexta-feira")
elif x == 1:
    print("Sábado")
else:
    print("Entrada inválida")


"""
Resposta:
    O programa irá dizer o dia da semana de acordo com o número, só vai está
    diferentes no dia Domingo e Sábado, que estão com os números trocados.
"""
