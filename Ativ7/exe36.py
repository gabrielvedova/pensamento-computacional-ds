#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 36.Peça ao usuário para inserir seu nome e sobrenome com letras minúsculas. Mude a caixa para o título e junte-os. Imprima o resultado geral.

fname = input('Digite o seu nome: ').lower()
sname = input('Digite o seu sobrenome: ').lower()
fullname = fname + ' ' + sname
print('Seu nome é {}.'.format(fullname.title()))