#!/usr/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
base_gc = pd.read_csv('media2020.csv')

x = base_gc['Hora']
y1 = base_gc['21 a 30 km']
y2 = base_gc['31 a 40 km']
y3 = base_gc['41 a 50 km']
y4 = base_gc['51 a 60 km']
y5 = base_gc['61 a 70 km']
y6 = base_gc['71 a 80 km']
y7 = base_gc['81 a 90 km']
y8 = base_gc['Média Total']

plt.plot(x, y1, label="21 a 30km", linestyle='solid', color='r')
plt.plot(x, y2, label="31 a 40km", linestyle='solid', color='b')
plt.plot(x, y3, label="41 a 50km", linestyle='solid', color='orange')
plt.plot(x, y4, label="51 a 60km", linestyle='solid', color='y')
plt.plot(x, y5, label="61 a 70km", linestyle='solid', color='c')
plt.plot(x, y6, label="71 a 80km", linestyle='solid', color='m')
plt.plot(x, y7, label="81 a 90km", linestyle='solid', color='k')
plt.plot(x, y8, label="Média Total", linestyle='solid', color='g')

plt.ylabel('Quantidade de Veículos')
plt.xlabel('Hora')
plt.title('Gráfico de Veículos por Hora - 2020')
plt.legend()
plt.grid()
plt.show()
