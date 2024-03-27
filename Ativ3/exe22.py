#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 22.Escreva um programa para construir duas listas: l1 e l2.


l1 = [1981, 1982, 1983]
l2 = []

l2.append('mds')
l2.append('acontece')
l2.append('fzr o q')
l2.append('n quero')

l1.sort()
l2.sort()
print(f"p1: {l1}\np2: {l2}")

while True:
    escolha_lista = input('Deseja add ou remover um item na lista: ')

    if escolha_lista == 'p1':
        add_remove = input('Deseja add ou remover um item na lista? ')
        if add_remove == 'add':
            add = int(input('Add um número aí: '))
            l1.append(add)
            l1.sort()
            print(l1)
            break
        elif add_remove == 'remover':
            remove = int(input('Digite o número que deseja remover: '))
            l1.remove(remove)
            l1.sort()
            print(l1)
            break
        else:
            print('Selecionou nenhuma opção meu amigo')
    elif escolha_lista == 'p2':
        add_remove = input('Deseja add ou remover um item na lista? ')
        if add_remove == 'add':
            add = input('Add o que quer aí: ')
            l2.append(add)
            l2.sort()
            print(l2)
            break
        elif add_remove == 'remover':
            remove = input('Digite o que deseja remover: ')
            l2.remove(remove)
            l2.sort()
            print(l2)
            break
        else:
            print('Selecionou nenhuma opção meu amigo')
    else:
        print('Digitou a lista errado meu nobre')
