#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 57.Implemente uma função que verifique se um determinado nome de usuário contém apenas caracteres alfanuméricos.


def is_alphanumeric(username):
    return username.isalnum()


user_input = input("Digite um nome de usuário: ")

if is_alphanumeric(user_input):
    print(f"'{user_input}' é alfanúmerico.")
else:
    print(f"'{user_input}' não é alfanúmerico.")


# Output:
# Digite um nome de usuário: gabriel123
# 'gabriel123' é alfanúmerico.
