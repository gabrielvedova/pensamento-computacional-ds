#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 42.Peça ao usuário para digitar uma palavra em maiúscula. Se ele digitar em letras minúsculas, peça-lhe que tente novamente. Continue repetindo isso até que ele digite uma mensagem com letra maiúscula.

palavra = input("Digite uma palavra em maiúscula: ")

while palavra.islower():
   print("Por favor, tente outra vez!")
   palavra = input("Digite uma palavra em maiúscula: ")
print(palavra)