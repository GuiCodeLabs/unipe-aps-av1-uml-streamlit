# Questão 04 — Classes, Atributos e Métodos

## Análise do problema

O sistema tem como objetivo controlar o horário de medicamentos de um usuário, permitindo cadastrar remédios, definir horários de uso e organizar uma planilha diária de medicação.

Cada remédio possui informações como:

* nome do paciente
* nome do remédio
* dosagem
* data de início
* quantidade de dias do tratamento
* quantidade de vezes ao dia

O sistema também deve:

* sugerir horários de medicação
* permitir que o usuário escolha os horários
* calcular a data final do tratamento
* gerar a planilha diária de horários
* reorganizar os horários em caso de atraso

Os relacionamentos entre as classes são representados como atributos derivados.

---

## Classes identificadas

### Classe `Paciente`

Representa a pessoa que irá tomar o remédio.

#### Atributos

* nome : string

#### Métodos

* cadastrar()
* editarNome()
* obterDados()

---

### Classe `Remedio`

Representa o remédio cadastrado no sistema.

#### Atributos

* nome : string
* dosagem : string
* dataInicio : date
* quantidadeDias : int
* vezesAoDia : int
* /paciente : Paciente

#### Métodos

* cadastrar()
* calcularDataFim()
* obterResumo()
* validarCadastro()

---

### Classe `HorarioMedicacao`

Representa os horários definidos para tomar o remédio.

#### Atributos

* hora : time
* status : string
* observacao : string
* /remedio : Remedio

#### Métodos

* marcarComoTomado()
* marcarComoAtrasado()
* reagendar()
* exibirHorario()

---

### Classe `PlanoMedicacao`

Responsável por gerenciar o tratamento completo e os horários do remédio.

#### Atributos

* /remedio : Remedio
* horarios : List<HorarioMedicacao>
* dataFim : date

#### Métodos

* sugerirHorarios()
* definirHorarios()
* gerarHorariosDoDia(data)
* reorganizarHorariosDoDia()
* calcularDataFimTratamento()

---

## Relacionamentos como atributos derivados

Os relacionamentos entre as classes foram representados como atributos derivados, conforme solicitado no enunciado.

Exemplos:

* `/paciente : Paciente` → um remédio está associado a um paciente
* `/remedio : Remedio` → um horário está associado a um remédio

---

## Resumo da modelagem

A modelagem proposta contém as seguintes classes:

* Paciente
* Remedio
* HorarioMedicacao
* PlanoMedicacao

A classe `Remedio` representa os dados principais do tratamento.
A classe `HorarioMedicacao` controla os horários de uso do remédio.
A classe `PlanoMedicacao` organiza o tratamento e permite gerar e reorganizar os horários.
A classe `Paciente` representa o usuário que faz uso do medicamento.

Essa estrutura atende aos requisitos do sistema e permite fácil expansão da aplicação.
