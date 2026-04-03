# Questão 01 — Classes, Atributos e Métodos

## Classe ContaLuz
### Atributos
- dataLeitura: date
- numeroLeitura: int
- kwGasto: float
- valorPagar: decimal
- dataPagamento: date
- mediaConsumo: float
- mesReferencia: string

### Métodos
- cadastrarConta()
- editarConta()
- calcularMediaConsumo()
- obterMesReferencia()
- registrarPagamento(data)

## Classe ControleContasLuz
### Atributos
- contas: List<ContaLuz>

### Métodos
- adicionarConta(conta)
- removerConta(numeroLeitura)
- listarContas()
- buscarMenorConsumo()
- buscarMaiorConsumo()