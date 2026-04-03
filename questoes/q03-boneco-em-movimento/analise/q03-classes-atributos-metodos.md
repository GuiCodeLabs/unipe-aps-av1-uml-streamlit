# Questão 3 - Boneco em Movimento

## 1. Entendimento do problema

O cenário apresenta a necessidade de criar uma classe que represente um boneco capaz de se mover na tela.

De acordo com o enunciado, esse boneco deve possuir:
- nome
- posição da coordenada X
- posição da coordenada Y
- direção atual

A direção atual pode assumir um dos seguintes valores:
- cima
- baixo
- direita
- esquerda

A partir disso, o objetivo da análise é identificar:
- a classe principal do problema
- seus atributos
- seus métodos
- possíveis estruturas auxiliares para organizar melhor a modelagem

---

## 2. Classe principal identificada

### Classe: Boneco

A classe principal do cenário é `Boneco`, pois ela representa diretamente o objeto central do problema.

É essa classe que concentra:
- os dados do boneco
- sua posição atual
- sua direção
- suas ações de movimentação

---

## 3. Atributos da classe Boneco

Os atributos identificados a partir do enunciado são:

- `nome: String`
- `posicaoX: int`
- `posicaoY: int`
- `direcaoAtual: Direcao`

### Justificativa dos atributos

- `nome`: identifica o boneco
- `posicaoX`: representa a posição horizontal do boneco
- `posicaoY`: representa a posição vertical do boneco
- `direcaoAtual`: informa para qual direção o boneco está apontando ou se movendo

---

## 4. Métodos da classe Boneco

Os métodos identificados para representar o comportamento do boneco são:

- `mover(): void`
- `moverCima(): void`
- `moverBaixo(): void`
- `moverEsquerda(): void`
- `moverDireita(): void`
- `alterarDirecao(novaDirecao: Direcao): void`
- `exibirPosicao(): String`
- `exibirEstado(): String`

### Justificativa dos métodos

- `mover()`: representa a ação genérica de movimentar o boneco de acordo com a direção atual
- `moverCima()`: move o boneco para cima
- `moverBaixo()`: move o boneco para baixo
- `moverEsquerda()`: move o boneco para a esquerda
- `moverDireita()`: move o boneco para a direita
- `alterarDirecao(novaDirecao)`: permite mudar a direção atual do boneco
- `exibirPosicao()`: retorna a posição atual do boneco
- `exibirEstado()`: retorna um resumo com nome, posição e direção atual

---

## 5. Classe auxiliar identificada

### Enumeração: Direcao

Para organizar melhor a modelagem, faz sentido criar uma estrutura auxiliar chamada `Direcao`.

Essa estrutura serve para limitar os valores possíveis da direção atual do boneco.

### Valores da enumeração Direcao

- `CIMA`
- `BAIXO`
- `ESQUERDA`
- `DIREITA`

### Justificativa

Usar uma enumeração deixa o modelo mais organizado e evita valores inválidos para a direção, como textos digitados de forma errada.

---

## 6. Relacionamento entre as estruturas

A classe `Boneco` utiliza a enumeração `Direcao` no atributo `direcaoAtual`.

Ou seja:
- um `Boneco` possui uma direção atual
- essa direção deve ser um dos valores definidos em `Direcao`

---

## 7. Conclusão da análise

A modelagem da questão 3 pode ser representada principalmente por:
- uma classe principal chamada `Boneco`
- uma enumeração auxiliar chamada `Direcao`

A classe `Boneco` concentra os dados e comportamentos do cenário, enquanto `Direcao` organiza os valores possíveis de direção do movimento.