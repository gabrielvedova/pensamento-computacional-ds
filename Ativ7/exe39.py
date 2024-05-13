#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 39.Peça ao usuário para inserir seu primeiro nome. Se o comprimento do primeiro nome for menos de cinco caracteres, peça que digitar o sobrenome e juntem-os (sem espaço) e tente exibir o nome em maiúsculas. Se o comprimento do primeiro nome tiver cinco ou mais caracteres, exiba o primeiro nome em letras minúsculas.
fname = input('Digite o seu primeiro nome: ')

if len(fname) < 5:
   sname = input('Digite o seu sobrenome: ').lower()
   print(fname.upper()+sname.upper())
else:
   print(fname.lower())