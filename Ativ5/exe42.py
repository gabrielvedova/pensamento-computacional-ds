#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 42.Qual será o resultado do seguinte código abaixo?
# OBS.: estou copiando os códigos para mostrar os resultados como vai ser

for p1 in range(4):
    print("Primeiro for: ", p1)

for p2 in range(4, 7):
    print("Segundo for: ", p2)

for p3 in range(14, 28, 4):
    print("Terceiro for: ", p3)

for p4 in range(24, 18, -3):
    print("Quarto for: ", p4)


"""
Resposta:
    O programa irá executar o seguinte comando no terminal:
        Primeiro for:  0
        Primeiro for:  1
        Primeiro for:  2
        Primeiro for:  3
        Segundo for:  4
        Segundo for:  5
        Segundo for:  6
        Terceiro for:  14
        Terceiro for:  18
        Terceiro for:  22
        Terceiro for:  26
        Quarto for:  24
        Quarto for:  21

    No p1 e p2, ele determina quais números ele quer dentro de um mínimo
    para o máximo.

    Já no p3 e p4, além de determinar quais são os número, ele determinou o
    padrão também, em vez de aumentar ou diminuir um por um, ele determinou se
    quer aumentar em 4 em 4 ou -3 po -3.

"""
