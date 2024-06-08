#!/usr/bin/python3

# Tarefa 1
# Problema: você precisa criar um vetor.
# Solução: use NumPy para criar um array unidimensional.
import panda as pd
import numpy as np
from scipy import sparse
vetor_horizontal = np.array([1, 2, 3])
vetor_vertical = np.array([[1], [2], [3]])

"""
A
principal estrutura de dados do NumPy é o array multidimensional. Um
vetor é apenas uma matriz com uma única dimensão. Para criar um vetor,
simplesmente criamos um array unidimensional. Assim como os vetores,
essas matrizes podem ser representadas horizontalmente (ou seja, linhas)
ou verticalmente (ou seja, colunas).
"""

print('Vetor linha:\n', vetor_horizontal)

print('Vetor coluna:\n', vetor_vertical)

# Tarefa 2
# Problema: você precisa criar uma matriz.
# Solução: use NumPy para criar um array bidimensional:

matriz = np.array([[1, 2],
                  [1, 2],
                  [1, 2]])

print(matriz)

# Tarefa3
# Problema: dado dados com poucos valores diferentes de zero, você deseja representá-los de forma eficiente

matriz = np.array([[0, 0],
                  [0, 1],
                  [3, 0]])

# Cria matriz de linha esparsa compactada
matriz_esparsa = sparse.csr_matrix(matriz)
print(matriz_esparsa)

# Tarefa 4
# Problema: você precisa selecionar um ou mais elementos em um vetor ou matriz
# Solução:Problema você precisa selecionar um ou mais elementos em um vetor ou matriz

vetor = np.array([1, 2, 3, 4, 5, 6])
# Create matrix
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Selecionar o terceiro elemento do vetor
print(vetor[2])
# Selecionar a segunda linha, segunda coluna
print(matriz[1,1])

# Tarefa 5
"""
Como a maioria das coisas em Python, os arrays NumPy são indexados em zero, o que significa que o índice do
primeiro elemento é 0, não 1. Com essa ressalva, NumPy oferece uma ampla variedade de métodos para
selecionar (ou seja, indexar e fatiar) elementos ou grupos de elementos em
matrizes:
"""

print('Selecione todos os elementos de um vetor:', vetor[:])
print('Selecione tudo até e incluindo o terceiro elemento: ', vetor[:3])
print('Selecione tudo após o terceiro elemento: ', vetor[3:])
print('Selecione o último elemento: ', vetor[-1])
print('Inverte o vetor: ', vetor[::-1])
print('Seleciona as duas primeiras linhas e todas as colunas de uma matriz: ', matriz[:2,:])
print('Seleciona todas as linhas e a segunda coluna: ', matrix[:,1:2])

# Tarefa 6
# Problema: você deseja descrever a forma, o tamanho e as dimensões de uma matriz.

matriz = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print('Visualiza o número de linhas e colunas: ', matriz.shape)
print('Visualiza o número de elementos (linhas * colunas):', matriz.size)
print(' Ver número de dimensões: ', matriz.ndim)

# Tarefa 7
"""
Definindo uma função
"""


def minha_funcao_etepd():
    print("Escola Técnica Estadual Porto Digital")
    print("Recife-Pernambuco-Brasil")


minha_funcao_etepd()

# Tarefa 8
"""
Função com argumentos posicionais
"""

"""
"""


def minha_fun1(a, b):
    c = a+b
    print('O valor de a: ', a)
    print('O valor de b:', b)
    print("O resultado: ", c )


print(minha_fun1(10, 20))

# tarefa 9
"""
Função com argumentos e valor de retorno
"""

"""
Uma
função com valor de retorno é como um pequeno departamento, para onde
vai algum material entra e o material recém-processado sai.
"""


def fun1(a, b):
    c = a+b
    return c


resultado = 20 + fun1(1, 12)
print(resultado)

# tarefa 10
"""
Função com argumento padrão
"""

"""
Também podemos definir o argumento padrão. Podemos definir o valor padrão no argumento. Se não 
especificarmos o argumento durante a chamada, a função assumirá o valor padrão. Veja o exemplo a seguir:
"""


def fun1(nome, habilidade, idade=30):
    print(nome, "\t", habilidade, idade)


print(" habilidade \t idade")
fun1("John", "python", 32)
fun1("Doe", "java")

# tarefa 11
"""
Função com argumentos de comprimento variável
"""

"""
Com a ajuda de um argumento de comprimento variável, podemos fornecer um número diferente de
argumentos
"""


def adicao(a,*args):
    print(type(args))
    c = a+sum(args)
    return c


print(adicao(10))
print(adicao(10,50,12,20,40))
print(adicao(10,20))


# tarefa 12


def fun1(**kwargs):
    print (type(kwargs))
    print (kwargs)


fun1(nome= "XYZ", idade = 30, habilidade= "Biologia")

# tarefa 13

dataframe = pd.read_csv('/content/sample_data/titanic.csv')

# Calcular estatísticas
print('Maximum:', dataframe['Age'].max())
print('Minimum:', dataframe['Age'].min())
print('Mean:', dataframe['Age'].mean())
print('Sum:', dataframe['Age'].sum())
print('Count:', dataframe['Age'].count())

# tarefa 14
dataframe["Age"].min()

# tarefa 15
dataframe["Age"].max()

# tarefa 16
passageiro = dataframe[dataframe["Sex"] == "male"]
passageiro

# tarefa 17
passageira = dataframe[dataframe["Sex"] == "female"]
passageira

# tarefa 16
dataframe.iloc[10]

# tarefa 17
dataframe.hist(column="Age")

# tarefa 18
dataframe.describe()

# tarefa 19
dataframe.info()

# tarefa 20
# Load library

# Criar um  DataFrame
data_a = {'id': ['1', '2', '3'],
          'primeiro': ['Alex', 'Amy', 'Allen'],
          'ultimo': ['Anderson', 'Ackerman', 'Ali']}
dataframe_a = pd.DataFrame(data_a, columns=['id', 'primeiro', 'ultimo'])

# Criar outro DataFrame
data_b = {'id': ['4', '5', '6'],
          'primeiro': ['Billy', 'Brian', 'Bran'],
          'ultimo': ['Bonder', 'Black', 'Balwner']}
dataframe_b = pd.DataFrame(data_b, columns=['id', 'primeiro', 'ultimo'])

# Concatenar DataFrames por linhas
pd.concat([dataframe_a, dataframe_b], axis=0)

# Concatenar DataFrames por colunas
print('oi', pd.concat([dataframe_a, dataframe_b], axis=1))
