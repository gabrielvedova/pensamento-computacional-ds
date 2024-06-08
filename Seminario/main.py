#!/usr/bin/python3

import pandas as pd

# 2019

#   lendo arquivo csv

data2019 = pd.read_csv('lombada_201906.csv', sep=';')

#   Filtrando por HORA

#       hora 06

hora2019_06 = data2019[data2019['hora'] == 6]

hora06_21a30km = round(hora2019_06['qtd_21a30km'].mean(), 2)
hora06_31a40km = round(hora2019_06['qtd_31a40km'].mean(), 2)
hora06_41a50km = round(hora2019_06['qtd_41a50km'].mean(), 2)
hora06_51a60km = round(hora2019_06['qtd_51a60km'].mean(), 2)
hora06_61a70km = round(hora2019_06['qtd_61a70km'].mean(), 2)
hora06_71a80km = round(hora2019_06['qtd_71a80km'].mean(), 2)
hora06_81a90km = round(hora2019_06['qtd_81a90km'].mean(), 2)

hora06_total = round((hora06_21a30km + hora06_31a40km + hora06_41a50km + hora06_51a60km + hora06_61a70km + hora06_71a80km + hora06_81a90km)/7, 2)

#       hora 07

hora2019_07 = data2019[data2019['hora'] == 7]

hora07_21a30km = round(hora2019_07['qtd_21a30km'].mean(), 2)
hora07_31a40km = round(hora2019_07['qtd_31a40km'].mean(), 2)
hora07_41a50km = round(hora2019_07['qtd_41a50km'].mean(), 2)
hora07_51a60km = round(hora2019_07['qtd_51a60km'].mean(), 2)
hora07_61a70km = round(hora2019_07['qtd_61a70km'].mean(), 2)
hora07_71a80km = round(hora2019_07['qtd_71a80km'].mean(), 2)
hora07_81a90km = round(hora2019_07['qtd_81a90km'].mean(), 2)

hora07_total = round((hora07_21a30km + hora07_31a40km + hora07_41a50km + hora07_51a60km + hora07_61a70km + hora07_71a80km + hora07_81a90km)/7, 2)

#       hora 08

hora2019_08 = data2019[data2019['hora'] == 8]

hora08_21a30km = round(hora2019_08['qtd_21a30km'].mean(), 2)
hora08_31a40km = round(hora2019_08['qtd_31a40km'].mean(), 2)
hora08_41a50km = round(hora2019_08['qtd_41a50km'].mean(), 2)
hora08_51a60km = round(hora2019_08['qtd_51a60km'].mean(), 2)
hora08_61a70km = round(hora2019_08['qtd_61a70km'].mean(), 2)
hora08_71a80km = round(hora2019_08['qtd_71a80km'].mean(), 2)
hora08_81a90km = round(hora2019_08['qtd_81a90km'].mean(), 2)

hora08_total = round((hora08_21a30km + hora08_31a40km + hora08_41a50km + hora08_51a60km + hora08_61a70km + hora08_71a80km + hora08_81a90km)/7, 2)

#       todas as horas

hora2019 = data2019[(data2019['hora'] >= 6) & (data2019['hora'] <= 8)]

hora2019_21a30km = round(hora2019['qtd_21a30km'].mean(), 2)
hora2019_31a40km = round(hora2019['qtd_31a40km'].mean(), 2)
hora2019_41a50km = round(hora2019['qtd_41a50km'].mean(), 2)
hora2019_51a60km = round(hora2019['qtd_51a60km'].mean(), 2)
hora2019_61a70km = round(hora2019['qtd_61a70km'].mean(), 2)
hora2019_71a80km = round(hora2019['qtd_71a80km'].mean(), 2)
hora2019_81a90km = round(hora2019['qtd_81a90km'].mean(), 2)

hora2019_total = round((hora2019_21a30km + hora2019_31a40km + hora2019_41a50km + hora2019_51a60km + hora2019_61a70km + hora2019_71a80km + hora2019_81a90km)/7, 2)


#   Criando uma tabela com os dados filtrados

data19 = [['06', hora06_21a30km, hora06_31a40km, hora06_41a50km, hora06_51a60km, hora06_61a70km, hora06_71a80km, hora06_81a90km, hora06_total],
          ['07', hora07_21a30km, hora07_31a40km, hora07_41a50km, hora07_51a60km, hora07_61a70km, hora07_71a80km, hora07_81a90km, hora07_total],
          ['08', hora08_21a30km, hora08_31a40km, hora08_41a50km, hora08_51a60km, hora08_61a70km, hora08_71a80km, hora08_81a90km, hora08_total],
          ['Total', hora2019_21a30km, hora2019_31a40km, hora2019_41a50km, hora2019_51a60km, hora2019_61a70km, hora2019_71a80km, hora2019_81a90km, hora2019_total]]

newData2019 = pd.DataFrame(data19, columns=['Hora', '21 a 30 km', '31 a 40 km', '41 a 50 km', '51 a 60 km', '61 a 70 km', '71 a 80 km', '81 a 90 km', 'Média Total'])

print(newData2019)

# 2020

#   lendo arquivo csv

data2020 = pd.read_csv('junholomb2020.csv', sep=';')

#   Filtrando por HORA

#       hora 06

hora2020_06 = data2020[data2020['hora'] == 6]

hora06_21a30km = round(hora2020_06['qtd_21a30km'].mean(), 2)
hora06_31a40km = round(hora2020_06['qtd_31a40km'].mean(), 2)
hora06_41a50km = round(hora2020_06['qtd_41a50km'].mean(), 2)
hora06_51a60km = round(hora2020_06['qtd_51a60km'].mean(), 2)
hora06_61a70km = round(hora2020_06['qtd_61a70km'].mean(), 2)
hora06_71a80km = round(hora2020_06['qtd_71a80km'].mean(), 2)
hora06_81a90km = round(hora2020_06['qtd_81a90km'].mean(), 2)

hora06_total = round((hora06_21a30km + hora06_31a40km + hora06_41a50km + hora06_51a60km + hora06_61a70km + hora06_71a80km + hora06_81a90km)/7, 2)

#       hora 07

hora2020_07 = data2020[data2020['hora'] == 7]

hora07_21a30km = round(hora2020_07['qtd_21a30km'].mean(), 2)
hora07_31a40km = round(hora2020_07['qtd_31a40km'].mean(), 2)
hora07_41a50km = round(hora2020_07['qtd_41a50km'].mean(), 2)
hora07_51a60km = round(hora2020_07['qtd_51a60km'].mean(), 2)
hora07_61a70km = round(hora2020_07['qtd_61a70km'].mean(), 2)
hora07_71a80km = round(hora2020_07['qtd_71a80km'].mean(), 2)
hora07_81a90km = round(hora2020_07['qtd_81a90km'].mean(), 2)

hora07_total = round((hora07_21a30km + hora07_31a40km + hora07_41a50km + hora07_51a60km + hora07_61a70km + hora07_71a80km + hora07_81a90km)/7, 2)

#       hora 08

hora2020_08 = data2020[data2020['hora'] == 8]

hora08_21a30km = round(hora2020_08['qtd_21a30km'].mean(), 2)
hora08_31a40km = round(hora2020_08['qtd_31a40km'].mean(), 2)
hora08_41a50km = round(hora2020_08['qtd_41a50km'].mean(), 2)
hora08_51a60km = round(hora2020_08['qtd_51a60km'].mean(), 2)
hora08_61a70km = round(hora2020_08['qtd_61a70km'].mean(), 2)
hora08_71a80km = round(hora2020_08['qtd_71a80km'].mean(), 2)
hora08_81a90km = round(hora2020_08['qtd_81a90km'].mean(), 2)

hora08_total = round((hora08_21a30km + hora08_31a40km + hora08_41a50km + hora08_51a60km + hora08_61a70km + hora08_71a80km + hora08_81a90km)/7, 2)

#       todas as horas

hora2020 = data2020[(data2020['hora'] >= 6) & (data2020['hora'] <= 8)]

hora2020_21a30km = round(hora2020['qtd_21a30km'].mean(), 2)
hora2020_31a40km = round(hora2020['qtd_31a40km'].mean(), 2)
hora2020_41a50km = round(hora2020['qtd_41a50km'].mean(), 2)
hora2020_51a60km = round(hora2020['qtd_51a60km'].mean(), 2)
hora2020_61a70km = round(hora2020['qtd_61a70km'].mean(), 2)
hora2020_71a80km = round(hora2020['qtd_71a80km'].mean(), 2)
hora2020_81a90km = round(hora2020['qtd_81a90km'].mean(), 2)

hora2020_total = round((hora2020_21a30km + hora2020_31a40km + hora2020_41a50km + hora2020_51a60km + hora2020_61a70km + hora2020_71a80km + hora2020_81a90km)/7, 2)


#   Criando uma tabela com os dados filtrados

data20 = [['06', hora06_21a30km, hora06_31a40km, hora06_41a50km, hora06_51a60km, hora06_61a70km, hora06_71a80km, hora06_81a90km, hora06_total],
          ['07', hora07_21a30km, hora07_31a40km, hora07_41a50km, hora07_51a60km, hora07_61a70km, hora07_71a80km, hora07_81a90km, hora07_total],
          ['08', hora08_21a30km, hora08_31a40km, hora08_41a50km, hora08_51a60km, hora08_61a70km, hora08_71a80km, hora08_81a90km, hora08_total],
          ['Total', hora2020_21a30km, hora2020_31a40km, hora2020_41a50km, hora2020_51a60km, hora2020_61a70km, hora2020_71a80km, hora2020_81a90km, hora2020_total]]

newData2020 = pd.DataFrame(data20, columns=['Hora', '21 a 30 km', '31 a 40 km', '41 a 50 km', '51 a 60 km', '61 a 70 km', '71 a 80 km', '81 a 90 km', 'Média Total'])

print(newData2020)

# Convertendo os dados para um arquivo csv

newData2019.to_csv('media2019.csv', index=False)
newData2020.to_csv('media2020.csv', index=False)
