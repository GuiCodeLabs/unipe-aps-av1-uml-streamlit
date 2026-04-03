# Questão 11 — Herança

## Análise do problema

A questão apresenta duas classes: `Funcionario` e `Cliente`.
O objetivo é criar uma superclasse que reúna os atributos e métodos comuns entre elas, reformulando a modelagem com herança.

Os elementos em comum identificados foram:
- nome
- dataNascimento
- /endereco : Endereco
- /telesContato : Colecao<Telefone>
- cadastrar()
- obterIdade()

Com isso, a melhor solução é criar a superclasse `Pessoa`.

---

## Classes reformuladas

### Superclasse `Pessoa`
Representa os dados comuns entre funcionário e cliente.

#### Atributos
- nome : string
- dataNascimento : date
- /endereco : Endereco
- /telesContato : Colecao<Telefone>

#### Métodos
- cadastrar()
- obterIdade()

---

### Subclasse `Funcionario`
Herda de `Pessoa` e representa o funcionário da organização.

#### Atributos
- matricula : integer
- /cargo : Cargo
- salario : real
- dataAdmissao : date

#### Métodos
- reajustarSalario(percentual : real)
- promover(novoCargo : Cargo)

---

### Subclasse `Cliente`
Herda de `Pessoa` e representa o cliente.

#### Atributos
- codigo : string
- /profissao : Profissao

#### Métodos
- cadastrar()
- obterIdade()

> Observação:
> Os métodos `cadastrar()` e `obterIdade()` já são herdados de `Pessoa`.
> Portanto, na prática, `Cliente` não precisa reescrevê-los, a menos que exista alguma especialização futura.

---

## Classes auxiliares

### Classe `Endereco`
Representa o endereço associado à pessoa.

#### Atributos
- logradouro : string
- numero : string
- bairro : string
- cidade : string
- estado : string
- cep : string

#### Métodos
- cadastrar()
- atualizar()

---

### Classe `Telefone`
Representa um telefone de contato.

#### Atributos
- numero : string
- tipo : string

#### Métodos
- cadastrar()
- atualizar()

---

### Classe `Cargo`
Representa o cargo ocupado pelo funcionário.

#### Atributos
- nome : string
- descricao : string

#### Métodos
- cadastrar()
- atualizar()

---

### Classe `Profissao`
Representa a profissão do cliente.

#### Atributos
- nome : string
- descricao : string

#### Métodos
- cadastrar()
- atualizar()

---

## Resumo da herança

A estrutura final fica assim:
- `Pessoa` como superclasse
- `Funcionario` como subclasse de `Pessoa`
- `Cliente` como subclasse de `Pessoa`

Essa solução evita duplicação de atributos e métodos, melhora a organização da modelagem e aplica corretamente o conceito de herança.