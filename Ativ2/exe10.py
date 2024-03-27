#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A
# 10.Escreva um programa para testar se idade é maior ou menor do que 18 anos.

from datetime import date

while True:

    try:
        idade = input("Insira sua data de nascimento(mm/yyyy): ")
        mes = int(idade[:2])
        ano = int(idade[3:])

        if mes > 12 or mes < 1 or ano < 0:
            print('Digitou errado meu irmão')
        else:
            if date.today().year - ano < 18:
                if date.today().year - ano < 0:
                    print('Nem nasceu meu nobre')
                else:
                    print('É de menor...')
                    break
            elif date.today().year - ano == 18:
                m_rest = date.today().month - mes

                if date.today().month - mes > 0:
                    print(f"Vc ainda é menor, mas falta {m_rest} mês(es)")
                break
            else:
                if date.today().year - ano <= 115:
                    print('Pode beber em paz')
                    break
                elif date.today().year - ano > 115:
                    print('Virou um ser onipresente é')
    except ValueError:
        print("Digitou a data errada meu amigo")
