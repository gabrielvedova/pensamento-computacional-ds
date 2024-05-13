#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 41.Peça ao usuário para digitar sua matéria escolar favorita. Mostre-o com “-” após cada letra, por ex. E-s-p-a-n-h-o-l.
mat_escolar = input("Digite sua matéria escolar favorita: ")

for letra in mat_escolar:
   print(letra, end='-')