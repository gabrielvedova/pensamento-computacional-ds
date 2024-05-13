#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 40.Peça ao usuário para inserir seu primeiro nome e, em seguida, exibir o comprimento de seu primeiro nome. Em seguida, pergunte o sobrenome e exiba a extensão do sobrenome. Junte o nome e o sobrenome com um espaço e exiba o resultado. Por fim, exiba o comprimento do nome completo (incluindo o espaço).
primeiro = input("Digite o seu primeiro nome: ")
print(len(primeiro))

final = input("Digite o seu sobrenome: ")
print(len(final))

nc = primeiro + ' ' + final
print(nc)
print(len(nc))