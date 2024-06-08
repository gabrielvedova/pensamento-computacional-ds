#!/usr/bin/python3

# Tarefa 1.Use o método .read_csv() do pacote pandas e carregue o conjunto de dados em uma nova variável chamada df:

import pandas as pd
df = pd.read_csv('ames_iowa_housing.csv')

# Tarefa 2.Imprima o número de linhas e colunas do DataFrame usando a forma atributo da biblioteca pandas. Podemos ver que este conjunto de dados contém 1.460 linhas e 81 colunas diferentes.

print(df.shape)

# Tarefa3.Imprima os nomes das variáveis ​​contidas neste DataFrame usando as colunas atributo do pacote pandas:

print(df.columns)

# Tarefa 4.Imprima o tipo de cada variável contida neste DataFrame usando o atributo dtypes do pacote pandas:

print(df.dtypes)

# Tarefa 5.Exiba as linhas superiores do DataFrame usando o método head() do pandas:

print(df.head())

# Tarefa 6.Exiba as últimas cinco linhas do DataFrame usando o método tail() dos pandas:

print(df.tail())

# Tarefa 7.Agora, exiba 5 linhas amostradas aleatórias do DataFrame usando sample() método do pandas e passe para ele um 'random_state' de 8:

print(df.sample(5, random_state=8))

# Tarefa 8.Crie um novo DataFrame chamado obj_df apenas com as colunas que são de tipos numéricos usando o método select_dtypes do pacote pandas. Em seguida, passe o valor do objeto para o parâmetro include:

obj_df = df.select_dtypes(include='object')
print(obj_df)

# Tarefa 9.Usando o atributo columns do pandas, extraia a lista de colunas deste DataFrame, obj_df, atribua-a a uma nova variável chamada obj_cols e imprima seu conteúdo:

obj_cols = obj_df.columns
print(obj_cols)

# Tarefa 10.Crie uma função chamada description_object que usa um DataFrame do pandas e um nome de coluna como parâmetros de entrada. Então, dentro da função, imprima o nome da coluna fornecida, seu número de valores únicos usando a função nunique() e a lista de valores e suas ocorrências usando o método value_counts().


def describe_object(df, col_name):
    print(f"\nCOLUMN: {col_name}")
    print(f"{df[col_name].nunique()} different values")
    print(f"List of values:")
    print(df[col_name].value_counts\
                       (dropna=False, normalize=True))
    
# Tarefa 11.Teste esta função fornecendo o df DataFrame e a coluna 'MSZoning':


print(describe_object(df, 'MSZoning'))

# Tarefa 12.Crie um loop for que chamará a função criada para cada elemento da lista obj_cols:

for col_name in obj_cols:
    describe_object(df, col_name)

# Tarefa 13. Se quisermos saber qual é o maior valor contido no na coluna 'Quantidade', podemos usar o método .max():

print(df['Quantity'].max())

# Tarefa 14.Podemos ver que a quantidade máxima de um item vendido neste conjunto de dados é 80.995, o que parece extremamente alto para um negócio de varejo. Em um projeto real, esse tipo de valor inesperado terá que ser discutido e confirmado com o proprietário dos dados ou com as partes interessadas para ver se este é um valor genuíno ou incorreto. Agora, vamos fazer verificar o valor mais baixo para 'Quantidade' usando o método .min():

print(df['Quantity'].min())

# Tarefa 15.Podemos obter o valor médio de um recurso usando o método mean() do pandas:

print(df['Quantity'].mean())

# Tarefa 16.Podemos usar a mediana como outra medida de tendência central. A mediana é calculada dividindo a coluna em dois grupos de comprimentos iguais e obtendo o valor do ponto médio separando esses dois grupos. No pandas, você pode chamar o método median() para obter esse valor.

print(df['Quantity'].median())

# Tarefa 17.Também podemos avaliar o spread desta coluna (o quanto os pontos de dados variam em relação ao ponto central). Uma medida comum de spread é o desvio padrão. Quanto menor for esta medida, mais próximos os dados estarão da sua média. Por outro lado, se o o desvio padrão é alto, isso significa que há algumas observações que estão longe da média. Usaremos o método std() do pandas para calcular esta medida:

print(df['Quantity'].std())

# Tarefa 18.Na biblioteca pandas, existe um método que pode exibir a maioria dessas descrições estatísticas com uma única linha de código: description():

print(df.describe())

# Tarefa 19.Crie um novo DataFrame chamado num_df apenas com as colunas que são numéricas usando o método select_dtypes da biblioteca pandas e passe o valor 'number' para o parâmetro include:

num_df = df.select_dtypes(include='number')
print(num_df)

# Tarefa 20.Usando o atributo columns do pandas, extraia a lista de colunas deste DataFrame, num_df, atribua-a a uma nova variável chamada num_cols e imprima seu conteúdo.

num_cols = num_df.columns
print(num_cols)

# Tarefa 21.Crie uma função chamada description_numeric que usa um DataFrame do pandas e um nome de coluna como parâmetros de entrada. Em seguida, imprima o nome da coluna fornecida, seu valor máximo, mínimo, média, mediana e desvio padrão.


def describe_numeric(df, col_name):
    print(f"\nCOLUMN: {col_name}")
    print(f"Minimum: {df[col_name].min()}")
    print(f"Maximum: {df[col_name].max()}")
    print(f"Average: {df[col_name].mean()}")
    print(f"Standard Deviation: {df[col_name].std()}")
    print(f"Median: {df[col_name].median()}")

# Tarefa 22.Agora, teste esta função acima (describe_numeric) fornecendo o df DataFrame e a coluna PreçoVenda:

print(describe_numeric(df, 'SalePrice'))

# Tarefa 23.O preço de venda varia de 34.900 a 755.000 com média de 180.921. A mediana é ligeiramente inferior à média, o que nos indica que existem alguns valores discrepantes com preços de venda elevados. Crie um loop for que chamará a função criada acima para cada elemento da lista num_cols:

for col_name in num_cols:
    describe_numeric(df, col_name)
