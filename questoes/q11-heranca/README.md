# Questão 11 — Herança

## Descrição da questão

Esta questão trabalha o conceito de **herança** na orientação a objetos.

O enunciado apresenta duas classes:
- `Funcionario`
- `Cliente`

A proposta é identificar os atributos e métodos comuns entre elas e, a partir disso, criar uma **superclasse**, reformulando a modelagem para evitar repetição e melhorar a organização do sistema.

---

## Objetivo

Aplicar o conceito de herança por meio da criação de uma superclasse chamada `Pessoa`, concentrando nela os dados e comportamentos comuns às classes `Funcionario` e `Cliente`.

---

## Estrutura da solução

A modelagem proposta ficou organizada da seguinte forma:

- `Pessoa` → superclasse
- `Funcionario` → subclasse de `Pessoa`
- `Cliente` → subclasse de `Pessoa`

Também foram consideradas classes auxiliares para representar melhor os relacionamentos:
- `Endereco`
- `Telefone`
- `Cargo`
- `Profissao`

---

## Superclasse criada

A superclasse definida foi:

### `Pessoa`

Ela reúne os elementos comuns entre funcionário e cliente:

#### Atributos
- `nome : string`
- `dataNascimento : date`
- `/endereco : Endereco`
- `/telesContato : Colecao<Telefone>`

#### Métodos
- `cadastrar()`
- `obterIdade()`

---

## Classes reformuladas

### `Funcionario`
Passa a herdar de `Pessoa` e mantém apenas os elementos específicos:

#### Atributos
- `matricula : integer`
- `/cargo : Cargo`
- `salario : real`
- `dataAdmissao : date`

#### Métodos
- `reajustarSalario(percentual : real)`
- `promover(novoCargo : Cargo)`

---

### `Cliente`
Passa a herdar de `Pessoa` e mantém apenas os elementos específicos:

#### Atributos
- `codigo : string`
- `/profissao : Profissao`

---

## Arquivos da questão

```text
q11-heranca/
├── README.md
├── analise/
│   ├── q11-classes-atributos-metodos.md
│   ├── q11-requisitos.txt
│   └── q11-requisitos-nao-funcionais.txt
├── diagramas/
│   └── diagrama-classes-q11.puml
└── app/
    ├── app.py
    ├── README.md
    └── requirements.txt