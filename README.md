# Modelo Preditivo para Diabetes

- [1. Objetivos](#link2)
- [2. Workflow](#link2)
- [3. Desenvolvimento](#link3)
- [4. Deploy](#link4)
- [5. Versões](#link5)
- [6. Links](#link6)


<a id="link1"></a>
## 1. Objetivos
Descrever o processo de criação de uma aplicação que ao receber um conjunto de dados de um paciente, possa identificar ou prever se esse paciente irá desenvolver ou não diabetes.

Para esse objetivo será usada a técnica de Machine Learning para criação de um modelo preditivo.

Para esse exemplo será usado o aprendizado supervisionado, isto é, junto com os dados de entrada informaremos o resultado desejado, dessa forma o algoritmo usado irá analisar a entrada e a saída e poderá identificar os padrões presentes, gerando o modelo preditivo.

Alem do aprendizado supervisionado temos o não supervisionado.

Será usado um ambiente simples, com um dataset pequeno, focando nas etapas executadas e termos um quadro geral do processo.

<a id="link2"></a>
## 2. Workflow

Para atingir o objetivo vamos seguir o seguinte workflow:

### 1 - Definir o objetivo:
Todo o trabalho a ser realizado depende da definição clara e precisa do que deverá ser realizado, do problema a ser resolvido. Com o objetivo bem definido, será possível a correta coleta de dados, a escolha do algoritmo e etc.

### 2 - Obter os dados:
Apartir dos dados será possível resolver o problema.</br>
Nessa fase deverá ser identificado onde estão os dados, como processar, tratamentos a serem realizados (limpeza, codificação, dados faltantes, sujeira e etc)
Se estão estruturados ou não estruturados</br>

### 3 - Algoritmo:
Atualmente existem mais de sessenta algoritmos de Machine Learning.</br>
A escolha correta vai depender das etapas 1 e 2 alem dos resultados de validação.</br>
Por acontecer de ser necessário testar vários algoritmos durante o processp.

### 4 - Treinamento:
Nessa etapa podem ser aplicadas muitas técnicas.</br>
Os dados serão divididos em treino, teste  para aplicação do algoritmo.</br>
Nessa etapa os dados são divididos em treino, teste.

### 5 - Testes e Validação:
Nessa etapa o modelo será testado e validado usando os dados de teste.</br>
Apartir da acurácia pode ser necessário obter novos dados, alterar infomações, trocar o algoritmo.</br>
Esse processo demanda um esforço até que atenda os objetivos.

<a id="link3"></a>
## 3. Desenvolvimento

Para o desenvolvimento do modelo preditivo, será usado a linguagem python com o jupyter notebook.</br>

Essa escolha fica a critério do desenvolvedor, podendo usar uma ferramenta open source ou proprietária</br>

Como exemplos temos o python, R, SAS, SPSS.

Para facilitar o processo de desenvolvimento será usado um dataset pronto, em um caso prático, seria necessário
obter os dados na origem, esses dados poderiam estar em várias origem (relacional ou não), deveriam ser tratados (limpos) e etc...

Os dados serão obtidos do site kaggle (site de competições de Machine Learning)

Nome do arquivo: diabetes.csv

![Screenshot](/images/m01.jpg)

![Screenshot](/images/m02.jpg)

Para o desenvolvimento do código python será usado jupyter notebook, poderia ser usado o shell do python, mas o jupyter proporciona uma melhor visualização e facilita o desenvolvimento.

O dataset será carregado usando a biblioteca pandas.

Ele contem as seguintes colunas, onde as 8 primeiras serão usadas pelo algoritmo para encontrar os padrões
e obter como resultado a coluna Outcome que será o resultado ou previsão.

| Nome        | Tipo           | 
| ------------- |:-------------:|
| Pregnancies   | preditora     |
| Glucose   | preditora     |
| BloodPressure   | preditora     |
| SkinThickness   | preditora     |
| Insulin   | preditora     |
| BMI   | preditora     |
| DiabetesPedigreeFunction   | preditora     |
| Age   | preditora     |
| Outcome   | target     |

Para que o algoritmo possa aprender, são fornecidos dados históricos com o resultado esperado (Outcome)</br>

Esse é o aprendizado supervisionado.

![Screenshot](/images/m03.jpg)

![Screenshot](/images/m05.jpg)

Após a carga dos dados deve ser realizada a análise dos dados, para verificar se existem valores null, correlação e etc, para garantir a qualidade dos dados para que possa gerar um bom modelo.

![Screenshot](/images/m06.jpg)

![Screenshot](/images/m07.jpg)

Após o tratamento, deve ser verifica a distribuição do dataset, isto é, quantos casos positivos e quantos negativos.

![Screenshot](/images/m08.jpg)

É importante saber isso para que essa proporção seja mantida nos datasets de treino e de teste.

O dataset de treino será usado para criação do modelo e o de teste para validação.

Como o retorno é um valor 1 ou 0 (sim ou não) deve ser usado um algotitmo de classificação.

Nesse teste será usado o algoritmo Naive Bayes, mas outros podem ser usados como o Random Forest ou Regressão Logística
, para análise de qual pode trazer o melhor resultado.

Todos esses algoritmos estão presentes na biblioteca scikit-learn, que é uma biblioteca de aprendizado de máquina para a linguagem de programação Python.

- Importando o scikit-learn

![Screenshot](/images/m09.jpg)

- Dividindo o dataset em treino e teste

![Screenshot](/images/m10.jpg)

- Usando o algoritmo, treinando o modelo e verificando a acurácia com os dados de treino.

![Screenshot](/images/m11.jpg)

- Usando o modelo com os dados de teste

![Screenshot](/images/m12.jpg)

A acurácia foi menos, mas nesse caso foram usados dados não vistos pelo modelo. Dependo do objetivo pode ser necessário refazer o desenvolvimento, obter novos dados e etc para obter uma acurácia maior.

- O modelo foi salvo e agora será usado para fazer previsões com novos dados.

![Screenshot](/images/m13.jpg)


<a id="link4"></a>
## 4. Deploy

Para o deploy do modelo será usado o micro framework web baseado em python, devido a sua facilidade na implemantação.

Se não estiver presente no ambiente, efetuar a instalação.

```pip install flask```

Criar uma estrutura de pastas conforme a imagem:

![Screenshot](/images/m14.jpg)

```python app.py```</br>
Start da aplicação, expondo a porta 5000 para ser acessado.</br>

![Screenshot](/images/m15.jpg)

```app.py```</br>
Arquivo principal da aplicação, que vai definir as "rotas", que serão acessadas via browser, e os comandos.

```app/static/css/main.css```</br>
Arquivo com o css usado na página de consulta.

```app/static/model/modelo_diabetes_v1.sav```</br>
Arquivo com o modelo criado na fase de desenvolvimento.

```app/templates/pagina1.html```</br>
Arquivo com a página html de consulta</br>
Ao informar os valores e clicar no botão, os dados serão capturados e o modelo será aplicado. Retornando o resultado.

![Screenshot](/images/m16.jpg)

![Screenshot](/images/m17.jpg)

![Screenshot](/images/m18.jpg)

![Screenshot](/images/m19.jpg)

![Screenshot](/images/m20.jpg)

<a id="link5"></a>
## 5. Versões

- Python 3.5.2 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:53:06)
- sklearn = '0.17.1'

<a id="link6"></a>
## 6. Links

Dataset kaggle</br>
https://www.kaggle.com/uciml/pima-indians-diabetes-database

Scikit-Learn</br>
https://scikit-learn.org/stable/