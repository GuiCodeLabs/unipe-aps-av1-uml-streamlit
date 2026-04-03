# Questão 05 — Gastos Diários

## Prompt 01 — Análise
Atue como um Especialista Sênior em Engenharia de Prompt, Análise e Projeto de Sistemas. Como Analista Funcional, redija uma modelagem textual focando rigorosamente no recorte do domínio orçamentário atrelado puramente aos Gastos Diários de transações de entrada e relatórios de fluxo financeiro.

Contexto em Foco e Diretriz Crítica: O contexto acadêmico trata da inserção de registros de transacionamentos, requerendo a classificação mediante a um tipo de gasto, juntamente a data do dispêndio, valor correspondente e o vínculo exato com a forma de pagamento escolhida. Para os fechamentos mensais, o contexto exige: 1. total dos gastos mensais; 2. agrupamento por tipo de gasto; 3. agrupamento por forma de pagamento. 
NOTA VITAL DE RESTRIÇÃO: O enunciado exige incontestavelmente que você efetue a demonstração explícita atestando as inter-relações na modelagem como Atributos Derivados.

Suas instruções:
1. Examine e relacione os nomes das Classes requeridas identificadas (ex: Gasto).
2. Liste imperativamente os atributos. Deixe transparente os locais nos quais foi materializada a representação em Atributo Derivado contendo a info da intersecção de uso perante a forma e tipo.
3. Aborde nos métodos comportamentos para atender todas as agregações (total geral, por tipo, por forma de pagamento).
4. Forneça texto estruturado acadêmico. Não gere código ou diagramas nesta etapa.

## Prompt 02 — Requisitos funcionais
Atue como um Especialista Sênior de Requisitos e Engenharia de Software. Com base na análise das transições diárias de gastos efetuados, projete a listagem de features funcionais.

Contexto para formulação: Transações diárias possuem atributos fixos e balanço agrupador ao fim do mês exibindo categorias fragmentadas (tipagem e forma elegida).

Suas instruções:
1. Formule os RFs com numeração padrão (ex: RF-01, RF-02).
2. Escreva objetivamente: "O sistema deve calcular...", "O sistema deve cadastrar...".
3. Cubra minuciosamente as entradas base e as três agregações estatísticas relatadas: Total mensal, Total por Tipo, Total por Forma de pagamento.

## Prompt 03 — Requisitos não funcionais
Atue como um Arquiteto de Software Sênior especializado em Qualidade. Desenhe os Requisitos Não Funcionais perante o contexto dos Gastos rotineiros.

Restrições base: A interface renderizará em Python puro com Streamlit, sob gerenciamento local `session_state`. Nenhum banco de dados ou ambiente cloud complexo.

Suas instruções:
1. Englobe a grade categorial de RNFs (ex: RNF-01) cobrindo Desempenho, Usabilidade e Tecnologia.
2. Deixe claro o viés imperativo sobre as restrições arquiteturais (Python, Streamlit).
3. Produza formato claro e objetivo para aprovação de arquitetura acadêmica em laboratório prático.

## Prompt 04 — Diagrama de classes
Atue como um Especialista Sênior em UML Estrutural. Retorne apenas o código do diagrama PlantUML materializando os orçamentos Diários.

Contexto: Classes base de Gastos com Atributos Derivados para tipo e forma de pagamento, e métodos agregadores para o fechamento mensal e cálculo.

Suas instruções:
1. Forneça todo output contido em tag `@startuml` a `@enduml`.
2. Ilustre sem ambiguidades as classes contendo a modelagem com Atributo Derivado explicitamente demarcado como requisitado.
3. Não use linhas de associação para relacionamentos se o enunciado forçou atrelar e absorver a relação como em atributos derivados diretos na classe matriz que as absorveu nativamente. 
4. Zero saudações textuais antes ou depois. Só código PlantUML do diagrama é exigido na resposta.

## Prompt 05 — Aplicação Streamlit
Atue como um Desenvolvedor Python e Sênior Web. Materialize perfeitamente a camada estruturada de registros diários em formulários e exibições no fluxo de interface em interface com o framework interativo em Streamlit.

Contexto: O backend deve registrar os dados do dispêndio com tipagem predefinida contida para gastos, calendários cronológicos de saídas na operação e formas de remuneração associadas via valores pagos numéricos numa interface agradável e interativa em dashboard do balancete consolidado via totais agregando tudo ao final.

Suas instruções:
1. Crie globalmente `app.py` num script modular por função.
2. Armazene as listagens registradas em memória via statefulness nativa na estrutura base `st.session_state`. Não é preciso modelar ORMs com dados alocados.
3. Elabore rigorosas respostas sistêmicas à inserção falha, validando quantitativo decimal para impedir números irracionais numéricos incorretos em valores nulos de saídas cadastradas.
4. Implemente as três perspectivas de outputs de dados de fechamento numa visão visual do dashboard estruturada visual e categoricamente atraente como agrupadas com os fatiamentos corretos sem conflito na exibição no formulário na lateral. Mantenha tom padronizado para as disciplinas universitárias de UML em dev.

## Prompt 06 — requirements.txt
Atue como Desenvolvedor Python configurando o ambiente. Produza as referências restritas perante os módulos externos deste lab no ecossistema de Gastos.

Suas instruções:
1. Imprima num bloco a entrega isoladamente formatada estrita contendo o mapeamento de dependências.
2. Aborde apenas as bases (ex: `streamlit`, `pandas` para tabulações numéricas e render de df agregados). Nenhuma dependência inútil deve estar na lista.
3. Entrega pronta num arquivo textual final cru (raw mode) que a IA deva copiar e repassar perfeitamente.

## Prompt 07 — README da questão
Atue como Tech Lead elaborando um portal de apresentação padronizada profissional em formato de documentação visual Markdown rica nomeado README da solução "Gastos", baseando os módulos acadêmicos implementados local.

Suas instruções:
1. Confeccione formatações profissionais, dividindo o contexto da implementação com base restrita a Atributos Derivados nas estruturas lógicas modeladoras originais e como reflete na simplificação da agregação dos atributos parciais calculando e tabelando num app base `session_state`.
2. Inclua Estrutura do projeto, Tecnologias e explicite aos executores as diretrizes limpas para clonagem interativa e setup via comando local base de uso: `streamlit run app.py`.
3. Escreva um output detalhado focado em tom elucidativo em ambiente acadêmico limpo perfeitamente sem erros e bem estruturado por tabelamentos de cabeçalho (headings).

## Prompt 08 — Refino final
Atue como Arquiteto e Auditor QA em refinamento metodológico perante à matriz completa de "Gastos Diários".

Suas instruções:
1. Forneça o pente-fino cruzando nomenclaturas usadas perante Classes descritas nos RFs vs atributos Derivados atrelados nos diagramas em UML. Tudo corresponde estritamente em sincronia com os botões Python e dicionários em state no layout? Verifique isometria no seu veredicto do relatório entregável base.
2. Certifique formalmente na redação avaliativa sobre todos vetores restritos do prompt anterior apontando caso ocorram lixos operacionais implementados alheios aos requeridos nos relatórios analíticos de agrupamento orçamentário.
3. Entrega formatada num padrão rigoroso para balizar qualidade limpa do universitário antes da avaliação pelo seu tutor orientador acadêmico.
