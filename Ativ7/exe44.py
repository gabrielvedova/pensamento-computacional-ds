#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 44.Peça ao usuário para inserir uma nova senha. Peça-lhe para inseri-la novamente. Se as duas senhas corresponderem, exiba “Obrigado”. Se as letras estão corretos, mas no caso errado, exibir a mensagem “As senhas devem ser  iguais”, caso contrário exibirá a mensagem “Incorreto”.

senha1 = input("Digite uma nova senha:")

senha2 = input("Digite uma nova senha de novo:")

if senha1 == senha2:
   print("Obrigado!")
elif (senha1.isupper() and senha2.islower()) or (senha1.islower() and senha2.isupper()):
   print("As senhas devem ser iguais")
else:
   print("Incorreto!")