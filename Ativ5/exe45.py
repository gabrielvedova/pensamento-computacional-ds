#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 45.Qual será o resultado do seguinte código abaixo?
# OBS.: estou copiando os códigos para mostrar os resultados como vai ser


lista_palavras = ["Trabalho duro", "Paciência", "Esperança", "Sonhe grande"]
print(list(enumerate(lista_palavras)))

"""
Resposta:
    O programa irá executar o seguinte comando no terminal:
        [(0, 'Trabalho duro'), (1, 'Paciência'), (2, 'Esperança'), (3, 'Sonhe grande')]

    Isso acontece porque o enumarate mostra o número dos índices de cada item
    da lista, e o list serve só para juntar o número do índice com o valor
    em uma lista.
"""
