# 💿 Aplicação — Questão 08: Coleção de CDs

## 📌 Sobre a aplicação

Esta aplicação foi desenvolvida em **Python com Streamlit** com base no diagrama de classes da questão **Coleção de CDs**.

O sistema permite gerenciar uma coleção de CDs, possibilitando o cadastro de artistas e CDs, além de consultas e operações de edição e exclusão.

---

## ✅ Funcionalidades

A aplicação permite:

- cadastrar artistas
- cadastrar CDs
- listar todos os CDs cadastrados
- buscar CDs por título
- buscar CDs por artista
- editar o nome de um artista
- editar os dados de um CD
- excluir CDs da coleção

---

## 🧱 Estrutura da modelagem utilizada

A aplicação foi implementada com base nas seguintes classes do diagrama:

### Classe `Artista`
**Atributo:**
- `nome`

**Métodos:**
- `cadastrar()`
- `editarNome()`
- `obterNome()`

### Classe `CD`
**Atributos:**
- `titulo`
- `anoLancamento`
- `artista`

**Métodos:**
- `cadastrar()`
- `editar()`
- `excluir()`
- `obterDescricao()`

### Classe `ColecaoCDs`
**Atributo:**
- `cds`

**Métodos:**
- `adicionarCD(cd)`
- `removerCD(cd)`
- `listarCDs()`
- `buscarPorTitulo(titulo)`
- `buscarPorArtista(nomeArtista)`

---

## 🖥️ Tecnologias utilizadas

- Python
- Streamlit
- Pandas

---

## 📁 Arquivos da aplicação

```text
app/
├── app.py
├── README.md
└── requirements.txt
