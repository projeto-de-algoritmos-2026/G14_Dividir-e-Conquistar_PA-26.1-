# G14_Dividir-e-Conquistar_PA-26.1-

Número da Dupla: 14<br>
Conteúdo da Disciplina: D&C<br>
Vídeo da Apresentação: ()

## Alunas
|Matrícula | Aluna |
| -- | -- |
| 231026840 |  Laryssa Félix |
| 231027005  |  Maria Samara |


## Sobre

### Sistema de Seleção de Candidatos para Bolsa de Estudos

Este projeto tem como objetivo demonstrar a aplicação prática do paradigma **Dividir e Conquistar** por meio da implementação do algoritmo **Mediana das Medianas**.

O sistema simula um processo de seleção para bolsas de estudo, permitindo analisar um grande conjunto de candidatos e encontrar informações importantes sem a necessidade de ordenar completamente todos os dados.

Além de servir como aplicação prática do algoritmo, o projeto permite comparar seu desempenho com métodos tradicionais baseados em ordenação.

---

## Modelagem do Problema

O processo seletivo é modelado a partir de um conjunto de candidatos, onde cada candidato possui:

- Nome
- Nota

Exemplo:

| Candidato | Nota |
|------------|--------|
| João | 850 |
| Maria | 920 |
| Ana | 780 |
| Pedro | 650 |

A partir desse conjunto, o sistema deve responder perguntas como:

- Qual é a nota de corte?
- Quem ocupa determinada posição no ranking?
- Quais são os candidatos com melhor desempenho?
- Quais candidatos pertencem aos 10% melhores?

O problema pode ser interpretado como um problema clássico de **seleção**, no qual se deseja encontrar o elemento que ocupa uma posição específica em um conjunto de dados.

Ao invés de ordenar completamente todas as notas, o algoritmo Mediana das Medianas permite localizar diretamente o elemento desejado, reduzindo o custo computacional.

Além disso, o problema também pode ser interpretado como uma aplicação do paradigma **Dividir e Conquistar**, pois o conjunto de dados é sucessivamente dividido em subconjuntos menores até que a solução seja encontrada.

---

## Algoritmo Utilizado: Mediana das Medianas

Para resolver o problema, foi utilizado o algoritmo **Mediana das Medianas**, um algoritmo clássico de seleção com complexidade linear no pior caso.

O funcionamento do algoritmo pode ser resumido em:

1. Divide o conjunto de elementos em grupos de cinco.
2. Ordena cada grupo individualmente.
3. Calcula a mediana de cada grupo.
4. Encontra a mediana das medianas.
5. Utiliza esse valor como pivô.
6. Particiona os elementos em três grupos:
   - menores que o pivô
   - iguais ao pivô
   - maiores que o pivô
7. Continua a busca apenas na partição necessária.

No contexto do sistema:

- Cada nota representa um elemento do conjunto.
- O algoritmo encontra a nota que ocupa uma posição específica.
- A nota mediana é utilizada como nota de corte.
- O algoritmo evita a necessidade de ordenar todas as notas.
- Garante desempenho linear mesmo no pior caso.

---

## Funcionamento do Sistema

O sistema desenvolvido permite:

- Cadastrar candidatos
- Listar candidatos cadastrados
- Calcular a nota de corte
- Encontrar candidatos em posições específicas do ranking
- Identificar os 10% melhores candidatos
- Gerar candidatos automaticamente para testes
- Comparar desempenho entre algoritmos

---

## Screenshots

### Tela Inicial

Representa o estado inicial do sistema, onde o usuário pode escolher uma das funcionalidades disponíveis.

<img width="377" height="232" alt="image" src="https://github.com/user-attachments/assets/452d19e7-96cb-4ef5-a272-2a37bec98424" />

---

### Sistema Vazio

<img width="353" height="53" alt="image" src="https://github.com/user-attachments/assets/b60d07ab-158c-452b-bfc0-2d70e77dd841" />

---

### Cadastro de Candidatos

Mostra o cadastro de candidatos contendo nome e nota. 

<img width="312" height="83" alt="image" src="https://github.com/user-attachments/assets/93c44623-ca85-4628-8b86-1aef61b08447" />

---

### Listar Candidatos

Exibe uma lista com os cadidatos cadastrados. (Neste exemplo cadastramos cinco pessoas)

<img width="276" height="160" alt="image" src="https://github.com/user-attachments/assets/080e2157-402b-48c8-9666-5d490ee4aa40" />

---

### Nota de Corte

Exibe o resultado da execução do algoritmo Mediana das Medianas para encontrar a mediana das notas.

<img width="258" height="55" alt="image" src="https://github.com/user-attachments/assets/ff1418a7-1d4a-4df3-bba8-7741305e8118" />


---

### Busca por Posição K

Demonstra a busca pelo candidato que ocupa uma posição específica no ranking.

Exemplo:

- 1º colocado
- 10º colocado
- 100º colocado

<img width="277" height="87" alt="image" src="https://github.com/user-attachments/assets/cf136656-4e2f-42e1-839b-0c76a62e731d" />


---

### Top 10% dos Candidatos

Mostra os candidatos com melhor desempenho no processo seletivo. (Neste exemplo cadastramos mais cinco pessoas)

<img width="295" height="112" alt="image" src="https://github.com/user-attachments/assets/f08af9c9-31f4-4c50-a462-9e08687ff862" /> <br>

<img width="239" height="284" alt="image" src="https://github.com/user-attachments/assets/84b39798-a7a3-4e33-9402-79dd656c475f" />

---

### Gerar Relatório

Mostra o total de candidatos, note de corte, melhor e pior nota.

<img width="318" height="348" alt="image" src="https://github.com/user-attachments/assets/0d2dfbd4-823a-4f80-8a44-b6615c613097" />

---
### Geração Automática de Cadidatos

Gera candidatos automaticamente.

<img width="331" height="85" alt="image" src="https://github.com/user-attachments/assets/d01c476c-8ab7-4e9f-81a7-f4ea31f02ce2" /> <br>

<img width="258" height="346" alt="image" src="https://github.com/user-attachments/assets/b90fb416-0463-4a80-a02f-6b1823e22c94" />

---

### Comparação de Desempenho

Exibe os tempos de execução entre a abordagem tradicional baseada em ordenação e o algoritmo Mediana das Medianas.

<img width="442" height="399" alt="image" src="https://github.com/user-attachments/assets/20d59634-1e02-4959-ad76-e7280f154c67" />

---

## Instalação

### Linguagem

Python 3.10+

### Pré-requisitos

- Python 3 instalado
- pip instalado

### Passos

Clone o repositório:

```bash
git clone <url-do-repositorio>
cd projeto_bolsa
```

---

## Uso

Para executar o projeto, utilize o seguinte comando:

```bash
python main.py
```

Após executar:

- Cadastre candidatos manualmente ou gere dados automaticamente.
- Consulte a nota de corte.
- Busque candidatos em posições específicas.
- Visualize os 10% melhores candidatos.
- Execute testes de desempenho.

---

## Regras do Sistema

O sistema trabalha com um conjunto de candidatos cadastrados.

Cada candidato deve possuir:

- Nome
- Nota

As notas são utilizadas para:

- Determinar a nota de corte
- Construir o ranking
- Selecionar os melhores candidatos

A posição k representa a colocação desejada dentro do conjunto de candidatos.

Exemplos:

- k = 1 → melhor candidato
- k = 10 → décimo colocado
- k = 100 → centésimo colocado

---

## Como Encontrar a Nota de Corte

O sistema utiliza o algoritmo Mediana das Medianas para localizar a mediana do conjunto de notas.

Processo:

1. Divide as notas em grupos de cinco.
2. Calcula a mediana de cada grupo.
3. Encontra a mediana das medianas.
4. Utiliza esse valor como pivô.
5. Continua o processo recursivamente até encontrar a mediana.

O valor encontrado é utilizado como nota de corte.

---

## Buscar um Candidato pela Posição

O usuário pode informar uma posição k.

Exemplo:

```text
k = 50
```

O sistema retorna:

```text
50º colocado
```

Isso permite identificar rapidamente candidatos em posições específicas do ranking.

---

## Gerar Candidatos Automaticamente

Para facilitar os testes, o sistema pode gerar automaticamente grandes conjuntos de candidatos.

Exemplos:

```text
100 candidatos
1000 candidatos
10000 candidatos
100000 candidatos
```

Cada candidato recebe uma nota aleatória.

Essa funcionalidade é utilizada principalmente para a análise de desempenho do algoritmo.

---

## Comparação de Desempenho

O sistema compara duas abordagens:

### Ordenação Completa

```python
sorted(notas)
```

Complexidade:

```text
O(n log n)
```

### Mediana das Medianas

```python
mediana_das_medianas(notas, k)
```

Complexidade:

```text
O(n)
```

Os tempos de execução são medidos utilizando:

```python
time.perf_counter()
```

---

## Observações Importantes

- O algoritmo não precisa ordenar todas as notas.
- A mediana é encontrada diretamente.
- O algoritmo possui complexidade linear no pior caso.
- O projeto demonstra o paradigma Dividir e Conquistar.
- O desempenho se torna mais relevante conforme o volume de dados aumenta.

---

## Justificativa do Algoritmo

O algoritmo Mediana das Medianas foi escolhido por ser uma solução eficiente para problemas de seleção.

Diferentemente dos métodos tradicionais, que normalmente exigem a ordenação completa dos dados, a Mediana das Medianas encontra diretamente o elemento desejado utilizando uma estratégia baseada em Dividir e Conquistar.

Ao dividir o conjunto em grupos menores, calcular medianas intermediárias e utilizar uma mediana robusta como pivô, o algoritmo garante desempenho linear mesmo no pior caso.

Esse comportamento o torna adequado para aplicações que trabalham com grandes volumes de dados, como sistemas de seleção, rankings, estatísticas e análise de desempenho.

---

## Estrutura do Projeto

```text
projeto_bolsa/

├── candidato.py
│   └── Classe responsável por representar um candidato
│
├── mediana_das_medianas.py
│   └── Implementação do algoritmo Mediana das Medianas
│
├── sistema_bolsa.py
│   └── Regras de negócio do sistema
│
└── main.py
    └── Programa principal e interação com o usuário
```
