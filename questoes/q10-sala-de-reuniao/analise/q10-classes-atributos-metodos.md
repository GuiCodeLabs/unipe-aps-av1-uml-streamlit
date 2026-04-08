# Questão 10 — Sala de Reunião

## Classe SalaReuniao
### Atributos
- numero : string
- quantidadeLugares : int

### Métodos
- cadastrar()
- editarCapacidade()
- obterDisponibilidade(data, horarioInicio, horarioFim)

---

## Classe Funcionario
### Atributos
- nome : string
- cargo : string
- ramal : string

### Métodos
- cadastrar()
- editarDados()
- obterContato()

---

## Classe Reuniao
### Atributos
- data : date
- horarioInicio : time
- horarioFim : time
- assunto : string
- /funcionario : Funcionario
- /sala : SalaReuniao

### Métodos
- agendar()
- editar()
- realocar(novaSala, novaData, novoHorarioInicio, novoHorarioFim)
- cancelar()
- obterResumo()

---

## Classe ControleReunioes
### Atributos
- reunioes : List<Reuniao>
- salas : List<SalaReuniao>
- funcionarios : List<Funcionario>

### Métodos
- adicionarSala(sala : SalaReuniao)
- adicionarFuncionario(funcionario : Funcionario)
- agendarReuniao(reuniao : Reuniao)
- realocarReuniao(reuniao : Reuniao, novaSala : SalaReuniao, novaData : date, novoHorarioInicio : time, novoHorarioFim : time)
- cancelarReuniao(reuniao : Reuniao)
- listarReunioesPorData(data : date)
- consultarSalasLivres(data : date, horarioInicio : time, horarioFim : time)
- verificarConflito(sala : SalaReuniao, data : date, horarioInicio : time, horarioFim : time)