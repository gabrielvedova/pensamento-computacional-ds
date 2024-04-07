#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 39.Qual será o resultado do seguinte código abaixo?
# OBS.: estou copiando os códigos para mostrar os resultados como vai ser

entrada_do_número = int(input("Digite um número inteiro: "))

if entrada_do_número > 0:
    print(entrada_do_número, "é um número positivo")
elif entrada_do_número < 0:
    print(entrada_do_número, "é um número negativo")
else:
    print("é zero")


"""
Resposta:
    Como estamos trabalhamos com input, existe 4 possibilidades como resposta
    no terminal:
        1. entrada_do_número é um número positivo
        2. entrada_do_número é um número negativo
        3. entrada_do_número é zero
        4. Traceback (most recent call last):
            File "/home/vedova/Área de Trabalho/ETE_PORTODIGITAL/
            pensamento-computacional-ds/Ativ5/exe39.py", line 8, in <module>
            entrada_do_número = int(input("Digite um número inteiro: "))
            ValueError: invalid literal for int() with base 10:

    Na 4 opção é diferente pois acontece quando colocamos qualquer dado que não
    seja inteiro, pois na variável entrada_do_número foi declarado que só
    aceita números inteiros.
"""
