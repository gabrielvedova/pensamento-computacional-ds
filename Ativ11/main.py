#!/usr/bin/python3
import pandas as pd
import altair as alt

# Tarefa 1
"""
Utilizar a base de dados de OnlineRetail. Nesse caso, não é necessário baixar a base. É
necessário apenas inserir o endereço dela.
"""

"""
Existem
muitos pacotes em Python para visualização de dados no mercado, como
matplotlib, seaborn ou bokeh, e comparado a eles, altair é relativamente
novo, mas sua comunidade de usuários está crescendo rapidamente graças à
sua sintaxe simples de API.
"""

"""
Vamos ver como podemos exibir um gráfico de barras passo a passo no conjunto de dados de varejo online.
Primeiro, importe os pacotes pandas e altair:
"""

"""
Em seguida, carregue os dados em um DataFrame do pandas:
"""

file_url = 'https://github.com/FabrizioBF/datasets/blob/main/OnlineRetail.xlsx?raw=true&#39;'
df = pd.read_excel(file_url)

# Tarefa 2
"""
Iremos mostrar aleatoriamente 5.000 linhas deste DataFrame usando o método sample()
(altair requer etapas adicionais para exibir um conjunto de dados maior):
"""

sample_df = df.sample(n=5000, random_state=8)
print(sample_df)

# Tarefa 3
"""
Agora instancie um objeto Chart do altair com o DataFrame do pandas como parâmetro de entrada:
"""

base = alt.Chart(sample_df)

"""
A seguir, chamamos o método mark_circle() para especificar o tipo de gráfico que queremos traçar: um gráfico de dispersão:
"""

chart = base.mark_circle()

"""
Por fim, especificamos os nomes das colunas que serão exibidas nos eixos x e y
usando o método encode():
"""

chart.encode(x='Quantity', y='UnitPrice')

# Tarefa 4
"""
O pacote altair oferece a opção de combinar todos os seus métodos em uma única linha
de código, assim:
"""

alt.Chart(sample_df).mark_circle().encode(x='Quantity', y='UnitPrice')

"""
Podemos
ver que obtivemos exatamente a mesma saída de antes. Este gráfico nos
mostra que existem muitos outliers (valores extremos)
para ambas as variáveis: a maioria dos valores de UnitPrice estão abaixo de 100, mas existem alguns acima de 300, e faixas de
quantidade de -200 a 800, enquanto a maioria das observações está entre -50 a 150.
"""

"""
Nós também podemos observar um padrão onde itens com preço unitário alto têm quantidade menores (itens acima de 50
em
termos de preço unitário têm quantidade próxima de 0) e o contrário
também é verdadeiro (itens com quantidade superior a 100 têm
preços unitários próximo de 0).
"""

# Tarefa 5
"""
Agora, digamos que queremos visualizar o mesmo gráfico ao adicionar as informações da coluna País(Country). Uma maneira fácil de
fazer
isso é usar o parâmetro de cor(color) do método encode(). Isto irá
colorir todos os pontos de dados de acordo com o seu valor na
coluna País:
"""

alt.Chart(sample_df).mark_circle().encode(x='Quantity', y='UnitPrice', color='Country')

"""
Adicionamos as informações da coluna País ao gráfico, mas como podemos ver, há muitos valores e é difícil diferenciar os
países: há muitos pontos azuis, mas é difícil dizer quais países eles estão representando.
"""

# Tarefa 6
"""
Com
o altair, podemos facilmente adicionar algumas interações no gráfico
para exibir mais informações para cada observação; só precisamos usar o
parâmetro tooltip do método encode() e especifique a lista de colunas a
serem exibidas e
em seguida, chame o método interactive() para tornar tudo interativo
"""

"""
Agora,
se passarmos o mouse sobre a observação com o valor UnitPrice mais alto
(aquele próximo a 600), podemos ver a informação exibida pela dica de
ferramenta: esta observação não possui nenhum valor para StockCode e sua
Descrição é Manual. Então, é parece que esta não é uma transação normal
que acontece no site. Pode ser um pedido especial que foi inserido
manualmente no sistema. Isso é algo que você terá que discutir com sua
parte interessada e confirmar.
"""

alt.Chart(sample_df).mark_circle().encode(x='Quantity',
                                          y='UnitPrice',
                                          color='Country',
                                          tooltip=['InvoiceNo', 'StockCode', 'Description', 'InvoiceDate', 'CustomerID']).interactive()

# Tarefa 7
"""
Para este tipo de variável, um histograma é geralmente usado para mostrar a distribuição de um
determinada variável. O eixo x de um histograma mostrará os valores possíveis nesta coluna
e o eixo y representará o número de observações que se enquadram em cada valor. Desde
o número de valores possíveis pode ser muito alto para uma variável numérica (potencialmente
um número infinito de valores potenciais), é melhor agrupar esses valores por pedaços (também chamados de bins).
Por
exemplo, podemos agrupar preços em categorias de 10 etapas (ou seja,
grupos de 10 itens cada), como 0 a 10, 11 a 20, 21 a 30 e
assim por diante.
"""

"""
Vejamos isso usando um exemplo real. Vamos traçar um histograma para 'UnitPrice'
usando os métodos mark_bar() e encode() com os seguintes parâmetros:
"""

alt.Chart(sample_df).mark_bar().encode(alt.X("UnitPrice:Q", bin=True),y='count()')

# Tarefa 8
"""
Por
padrão, o altair agrupou as observações em compartimentos de 100
etapas: 0 a 100, depois 100 a 200 e assim por diante. O tamanho do passo
escolhido não é o ideal, pois quase todas as observações caíram no
primeiro compartimento (0 a 100) e não podemos ver nenhum outro
compartimento. Com altair, podemos especificar os valores do parâmetro
bin e tentaremos isso com 5, ou seja, alt.Bin(step=5)
"""

"""
Isto
é muito melhor. Com este tamanho de passo, podemos ver que a maioria
das observações tem um preço unitário inferior a 5 (quase 4.200
observações). Também podemos ver que um pouco mais do que 500 pontos de
dados têm um preço unitário inferior a 10. A contagem de registros
continua diminuindo à medida que o preço unitário aumenta.
"""

alt.Chart(sample_df).mark_bar().encode(alt.X("UnitPrice:Q", bin=alt.Bin(step=5)),y='count()')

# Tarefa 9
"""
Vamos traçar o histograma para a coluna Quantidade com um tamanho de intervalo de 10:
"""

"""
Neste
histograma, a maioria dos registros possui uma quantidade positiva
entre 0 e 30 (três primeiros compartimentos mais altos). Há também um
compartimento com cerca de 50 observações que possuem uma quantidade
negativa de -10 a 0.
"""

alt.Chart(sample_df).mark_bar().encode(alt.X("Quantity:Q", bin=alt.Bin(step=10)),y='count()')

# Tarefa 10
"""
Agora,
vamos dar uma olhada nas variáveis ​​​​categóricas. Para tais
variáveis, há não há necessidade de agrupar os valores em categorias,
pois, por definição, eles têm um número limitado de valores potenciais.
Ainda podemos traçar a distribuição de tais colunas usando um gráfico de
barra simples. No altair, isso é muito simples – é semelhante a traçar
um histograma, mas sem o parâmetro bin. Vamos tentar isso na coluna
País(Country) e observar o número de registros para cada um de seus
valores:
"""

alt.Chart(sample_df).mark_bar().encode(x='Country',y='count()')

# Tarefa 11
"""
Podemos confirmar que o Reino Unido é o país mais representado neste conjunto de dados (e de longe),
seguido
pela Alemanha, França e Irlanda. Claramente temos dados desequilibrados
que podem afetar o desempenho de um modelo preditivo.
"""

"""
Agora
vamos analisar a coluna datetime, ou seja, InvoiceDate. O pacote altair
fornece algumas funcionalidades que podemos usar para agrupar
informações de data e hora por período, como dia, dia da semana, mês e
assim por diante. Por exemplo, se quisermos ter uma visão mensal da
distribuição de uma variável, podemos usar a função ano mês para agrupar
datas e horas. Também precisamos especificar que o tipo desta variável é
ordinal (há uma ordem entre os valores) adicionando :O ao nome da
coluna:
"""

alt.Chart(sample_df).mark_bar().encode(alt.X('yearmonth(InvoiceDate):O'),y='count()')

# Tarefa 12
"""
O
gráfico anterior nos diz que houve um grande aumento de itens vendidos
em novembro de 2011. Atingiu o pico de 800 itens vendidos no mês,
enquanto a média gira em torno de 300. Houve alguma promoção ou campanha
publicitária realizada naquele momento que possa explicar esse aumento?
Estas são as perguntas que você pode querer fazer aos seus stakeholders
para que possam confirmar este aumento repentino nas vendas.
"""

"""
Agora,
daremos uma olhada em outro tipo específico de gráfico chamado boxplot.
Este tipo de gráfico é utilizado para exibir a distribuição de uma
variável com base em seus quartis. Quartis são os valores que dividem um
conjunto de dados em trimestres. Cada trimestre contém exatamente 25%
das observações.
"""

"""
Outro
benefício de usar um boxplot é traçar a distribuição de variáveis
​​categóricas em relação a uma variável numérica e compará-las. Vamos
tentar com o País(Country) e Colunas de quantidade(Quantity) usando o
método mark_boxplot()
"""

"""
O
gráfico nos mostra como a variável Quantidade está distribuída pelos
diferentes países para este conjunto de dados. Podemos ver que o Reino
Unido tem muitos valores discrepantes, especialmente nos valores
negativos. A Irlanda é outro país que apresenta valores discrepantes
negativos. A maioria dos países tem quantidades de valor muito baixo,
exceto o Japão, Holanda e Suécia, que venderam mais itens.
"""

alt.Chart(sample_df).mark_boxplot().encode(x='Country:O', y='Quantity:Q')

# Tarefa 13
"""
Utilizar a base de dados de habitações chamada Ames Iowa Housing. Nesse caso, não é necessário baixar a base. É
necessário apenas inserir o endereço dela.
"""

file_url2 = 'https://github.com/FabrizioBF/datasets/blob/main/AmesIowaHousing.csv?raw=true&#39;'

"""
Usando o método read_csv do pacote pandas, carregue o conjunto de dados em uma nova variável chamada 'df':
"""
df = pd.read_csv(file_url2)
df

# Tarefa 14
"""
Trace
o histograma para a variável SalePrice usando mark_bar() e
funçãoencode() do pacote altair. Use alt.X e alt.Bin para especificar o
número de etapas de bin, ou seja, 50.000
"""

"""
Este
gráfico mostra que a maioria das propriedades tem um preço de venda
centrado em 100.000 – 150.000. Existem também alguns valores
discrepantes com um preço de venda alto acima de 500.000.
"""

alt.Chart(df).mark_bar().encode(alt.X("SalePrice:Q", bin=alt.Bin(step=50000)),y='count()')

# Tarefa 15
"""
Agora, vamos traçar o histograma para LotArea, mas desta vez com um tamanho de intervalo de 10.000:
"""

"""
LotArea tem uma distribuição totalmente diferente em relação ao SalePrice. Maioria das observações estão entre 0 e 20.000.
O
resto das observações representam uma pequena parte do conjunto de
dados. Também podemos notar alguns valores extremos acima de 150.000
"""

"""
Existe claramente uma correlação entre o tamanho do imóvel e o preço de venda.
Se
olharmos apenas para as propriedades com LotArea inferior a 50.000,
podemos ver uma relação linear: se traçarmos uma linha reta das
coordenadas (0,0) até o (20000,800000), podemos dizer que SalePrice
aumenta em 40.000 para cada aumento adicional de 1.000 para LotArea. A
fórmula desta reta linha (ou linha de regressão) será SalePrice = 40000 *
LotArea / 1000.
Podemos observar também que,
para alguns imóveis, embora seu tamanho seja bastante elevado, seu preço
não seguiu esse padrão. Por exemplo, a propriedade com tamanho de
160.000 foi vendida por menos de 300.000.
"""

alt.Chart(df).mark_circle().encode(x='LotArea:Q', y='SalePrice:Q')

# Tarefa 16
"""
Agora, vamos traçar o histograma para GlobalCond, mas desta vez com o padrão
tamanho do passo bin, ou seja, (bin=True):
"""

"""
Podemos ver que os valores contidos nesta coluna são discretos: eles só podem assumir um número finito de
valores
(qualquer número inteiro entre 1 e 9). Esta variável não é numérica,
mas sim ordinal: a ordem importa, mas você não pode realizar algumas
operações matemáticas, como adicionar o valor 2 ao valor 8. Esta coluna
é um mapeamento arbitrário para avaliar a qualidade geral da propriedade.
"""

alt.Chart(df).mark_bar().encode(alt.X("OverallCond", bin=True),y='count()')

# Tarefa 17
"""
Construa um boxplot com OverCond:O (':O' é para especificar que esta coluna
é ordinal) no eixo x e SalePrice no eixo y usando o método mark_boxplot()
"""

"""
Parece que a variável OverallCond está em ordem crescente: o preço de venda é
maior se o valor da condição for alto. No entanto, notaremos que SalePrice é
bastante
elevado para o valor 5, o que parece representar uma condição média.
Pode haver outros fatores que impactem o preço de venda desta categoria,
como maior concorrência entre compradores por esses tipos de imóveis.
"""

"""
Podemos constatar que, aproximadamente, o mesmo número de imóveis é vendido todos os anos,
exceto 2010. De 2006 a 2009, foram, em média, 310 imóveis vendidos
por ano, enquanto havia apenas 170 em 2010.
"""
alt.Chart(df).mark_boxplot().encode(x='OverallCond:O', y='SalePrice:Q')

# Tarefa 18
"""
Globalmente, o preço médio de venda é bastante estável ao longo dos anos, com uma ligeira
diminuição em 2010.
"""
alt.Chart(df).mark_bar().encode(alt.X('YrSold:O'), y='count()')

# Tarefa 19
"""
Vamos analisar a relação entre SalePrice e Neighborhood traçando um gráfico de barras,
"""

"""
O
número de imóveis vendidos varia consoante a sua localização. O bairro
‘NAmes’ tem o maior número de imóveis vendidos: mais de 220. Por outro
lado, bairros como 'Blueste' ou 'NPkVill' só tinham poucos imóveis
vendidos.
"""

alt.Chart(df).mark_bar().encode(x='Neighborhood',y='count()')

# Tarefa 20
"""
Vamos analisar a relação entre SalePrice e Neighborhood traçando um gráfico boxplot.
"""

"""
A
localização dos imóveis vendidos tem um impacto significativo no preço
de venda. Os bairros noRidge, NridgHt e StoneBr têm preço mais alto
geral. Também é importante notar que existem alguns valores extremos
para NoRidge, onde algumas propriedades foram vendidas por um preço
muito mais alto do que outros imóveis neste bairro.
"""
alt.Chart(df).mark_boxplot().encode(x='Neighborhood:O', y='SalePrice:Q')
