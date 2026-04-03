# Questão 3 - Boneco em Movimento

## Sobre a questão

Esta questão propõe a modelagem de uma classe capaz de representar um boneco em movimento na tela.

De acordo com o enunciado, esse boneco deve possuir:
- nome
- posição da coordenada X
- posição da coordenada Y
- direção atual

A direção atual pode assumir os seguintes valores:
- cima
- baixo
- esquerda
- direita

O objetivo da atividade é identificar as classes, atributos e métodos envolvidos nesse cenário, além de representar a solução por meio da análise orientada a objetos, do diagrama de classes e da aplicação em Python com Streamlit.

---

## Objetivo da modelagem

A proposta desta questão é representar um objeto que possui:

- **estado**, por meio dos seus atributos
- **comportamento**, por meio dos seus métodos de movimentação

Nesse cenário, o boneco precisa armazenar sua posição atual e permitir deslocamentos na tela conforme a direção escolhida.

---

## Estrutura da solução

A solução da questão foi organizada em três partes principais:

### 1. Análise
Contém a identificação das classes, atributos, métodos e requisitos do problema.

### 2. Diagrama
Contém o diagrama de classes desenvolvido em PlantUML com base na análise realizada.

### 3. Aplicação
Contém a implementação prática da solução utilizando Python e Streamlit.

---

## Classe principal identificada

### `Boneco`

A classe principal do problema é `Boneco`, pois ela representa diretamente o elemento central do cenário.

Ela é responsável por armazenar os dados do boneco e executar suas ações de movimentação.

### Atributos da classe `Boneco`

- `nome: String`
- `posicaoX: int`
- `posicaoY: int`
- `direcaoAtual: Direcao`

### Métodos da classe `Boneco`

- `mover(): void`
- `moverCima(): void`
- `moverBaixo(): void`
- `moverEsquerda(): void`
- `moverDireita(): void`
- `alterarDirecao(novaDirecao: Direcao): void`
- `exibirPosicao(): String`
- `exibirEstado(): String`

---

## Estrutura auxiliar

### `Direcao`

Para melhorar a organização da modelagem, foi utilizada uma enumeração chamada `Direcao`, responsável por definir os valores possíveis para a direção atual do boneco.

### Valores possíveis

- `CIMA`
- `BAIXO`
- `ESQUERDA`
- `DIREITA`

Essa decisão ajuda a evitar valores inválidos e deixa o modelo mais claro.

---

## Requisitos identificados

### Requisitos funcionais
- cadastrar o nome do boneco
- armazenar a posição X
- armazenar a posição Y
- armazenar a direção atual
- mover o boneco para cima
- mover o boneco para baixo
- mover o boneco para a esquerda
- mover o boneco para a direita
- alterar a direção do boneco
- exibir a posição atual
- exibir o estado atual do boneco

### Requisitos não funcionais
- a aplicação deve ser desenvolvida em Python
- a interface deve ser implementada com Streamlit
- o sistema deve ter interface simples e fácil de usar
- a movimentação deve ocorrer com resposta imediata
- o código deve ser legível e organizado

---

## Organização da pasta

```text
q03-boneco-em-movimento/
├── analise/
│   ├── identificacao-classes.md
│   └── requisitos.txt
├── diagramas/
│   └── diagrama-classes.puml
├── app/
│   ├── app.py
│   └── requirements.txt
└── README.md