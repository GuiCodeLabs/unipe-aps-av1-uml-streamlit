# Questão 07 — Lista de Compras

## Prompt 01 — Análise
Atue como um Especialista Sênior em Engenharia de Prompt, Análise e Projeto de Sistemas. Como Analista Funcional, desenvolva a análise orientada a objetos para gerir uma Lista de Compras.

Contexto do problema: Cada item na lista requer especificações cadastrais precisas de controle, englobando o nome do produto inserido, a respectiva unidade de compra (ex: kg, pacote), atrelados ao quantitativo planejado (quantidade prevista para o mês) e à medida real realizada (quantidade efetivamente comprada). Acopla-se a este conjunto o preço estimado a ser gerido. Observações fundamentais estipulam que a quantidade efetivamente comprada é variável e que o preço estimado receberá atualizações constantes em fluxos periódicos mensais, descartando o controle granular de marcas para otimização da base. Note a demanda de atrelar relacionamentos em formato de atributos derivados.

Suas instruções:
1. Analise e defina as classes (ex: ItemCompra) para espelhar fidedignamente o controle.
2. Extraia os atributos, com especial atenção em apontar claramente onde ocorre o modelo simplificado com "atributos derivados", engolindo a relação externa diretamente para os dados locais da classe matriz principal de forma implícita.
3. Não insira "Marca", focando estritamente em atender à condição do enunciado que descarta marcas.
4. Mantenha nomes precisos, gerando o descritivo de forma textual (não gere códigos).

## Prompt 02 — Requisitos funcionais
Atue como um Especialista Sênior em Engenharia de Requisitos. Seu foco será descrever todas as funções do sistema Lista de Compras ancorado na análise supracitada.

Contexto do problema: Inserção de produtos na lista com nome, unidade, qtd. prevista e comprada, além de preço estimado, exigindo atualizações interativas sobre preço mensal e variações da qtd. real efetuada.

Suas instruções:
1. Numere claramente (padrão RF-XX).
2. Esboce um layout literal da literatura com obrigações: "O sistema deve possibilitar a edição do preço estimado...".
3. Formule operações atreladas: inclusão, listagem, atualização de saldo real de compra sobre a previsibilidade temporal, sem ultrapassar este escopo fechado isolado de gerência em marcas inoperantes.

## Prompt 03 — Requisitos não funcionais
Atue como um Especialista Sênior e Arquiteto de Software documentando RNFs sobre a arquitetura para a Lista de Compras universitária.

Restrições base impostas pela arquitetura de entrega: É imposto o limitador a aplicação nativa Python sob o motor iterativo nativo Streamlit no formato local de interações com salvamentos da interface operados na chave temporária e statefulness em `session_state`. Nenhum cluster nativo de storage externo operará.

Suas instruções:
1. Enumere com RNFs traceados categóricos.
2. Force restrições estritas perante persistência iterativa usando cache base da sessão sem persistências fora da web operada localmente no renderizador Streamlit.

## Prompt 04 — Diagrama de classes
Atue primeiramente como um Especialista Sênior em UML. Responda exclusivamente traduzindo ao seu modo de resposta base do código cru em diagramador analítico da Lista de Compras no repositório final.

Contexto modelo: Controle da lista, sem entidades soltas de marca de produtos, modelando derivativamente as bases associacionais (conforme os Atributos Derivados exigidos na prova de UML) gerando atrelamentos internos limpos de nomeação.

Suas instruções:
1. Transcreva e englobe unicamente com sintaxe do repositório em formato inicializado como `@startuml` a finalizado em `@enduml`. 
2. Use notação limpa e objetiva isolando a tipificação nativa dentro desta arquitetura isolada via `+nomeProduto: str`, `+unidadeCompra: str`, `+qtdPrevista: float`, e suas correspondentes sem ambiguidade lógica atestando modelagens das derivadas requisitadas na prova na base analítica. Nenhuma formatação além deste bloco.

## Prompt 05 — Aplicação Streamlit
Atue como Desenvolvedor Python e especialista frontend operado pela base nativa ágil de prototipação no Streamlit montando com precisão a lógica implementativa das ordens perante a Lista de Compras.

Contexto focado: Registros capturáveis pelo frontend contendo: inserções interativas fáceis contendo tipos do produto e previsões parciais base. Como é exigido a possibilidade contínua na qual a quantidade varia, o front terá atualizadores da base interativas da tela editando dados e recalculamentos na estimativa para as listagens sem perder focos do estado temporal ativo de sessões cadastradas de compras iterativas perante visões interativas ricas geridas por df em painéis dinâmicos.

Suas instruções:
1. Formule numa macro isolada a aplicação unificada e modular contida toda interativamente para `app.py`.
2. Assegure a utilização restrita voltada a armazenamento dict via formato base em estado local perante classe ativa em interface da web em escopo limpo `st.session_state`.
3. Ofereça interface UI robusta da tela capaz imperativamente de atualizar as interações editáveis interativas por forms modificando quantitativo real na tela e também atualização financeira iterativa sob previsibilidade, impedindo manipulações fora do estado sem as validações formais base do escopo, sem perder tom e nível do design em Python puro.

## Prompt 06 — requirements.txt
Atue na gerência do ecossistema e documentação devOps atrelado ao `requirements.txt`. 

Sua instrução única é apenas criar isoladamente e manifestado o arquivo focado da lib `streamlit` + parciais nativas analíticas puramente em texto puro limitativo no padrão, retornando puramente blocos base contidos de modo explícito à ser gravado pelas rotinas na aplicação base lista de Compras interativa. Nenhum comentário humano do agente gerador na resposta de saída além deste conteúdo isolado raw de arquivo formato txt.

## Prompt 07 — README da questão
Atue como Tech Lead em elaborações conceituais e arquitetônicas montando apresentações de entrega limpa, objetando um fôlego para repassar num readme estrutural formativo documentando atrelamentos de desenvolvimento da lista base de compras baseadas nas demandas.

Suas instruções:
1. Formule o output textual da montagem com viés de um `README.md` contendo detalhamentos sintáticos base referendado no git Markdown limitativo.
2. Divida os títulos entre Visões, a Estruturas locais relativas a sub pastas acadêmicas exigidas, como Setup local para start no comando em app e documentações fucionais explicitando justicativas como relacionamentos via derivação (eliminou complexidades) e como descartes da marcas reduziu modelagens de ecossistemas iterativos sob um Streamlit coeso, responsivo visual e direto a gestão analítica temporal diária.

## Prompt 08 — Refino final
Atue na liderança atrelado numa auditoria acadêmica QA formativa. Seu relatório metodizado e direto é o referenciamento que atesta que o entregável final de desenvolvedores de Compras passou com exatidão da restrição matriz.

Suas instruções estritas formativas em relatórios iterativos pontuais textuais e checagens rápidas da validação da questão a atestar a exatidão:
1. Afira, na UML contida ao dev em python, e as ordens textuais contendo derivadas no fluxo formativo se não incorreram para submissão distorcida baseada em bancos persistentes. Exija ajustes sob atrelamentos estritos isoladamente no state.
2. Confira validamente as propriedades da classe modelada isolada, sem atrelamentos inúteis ao produto, marca no código e diagramas de classe se estiver fora das ordens imperativas listadas da prova limitando escopo a previsibilidade perante saldo contido base do valor. Adote tons focados à inspeções avaliativas de forma estrutural formal indicando aprovabilidade num resumo sintético finalístico sem desvarios no texto.
