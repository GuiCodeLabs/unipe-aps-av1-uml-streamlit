# Questão 01 — Conta de Luz

## Prompt 01 — Análise
Atue como um Especialista Sênior em Engenharia de Prompt, Análise e Projeto de Sistemas. O objetivo desta tarefa é elaborar a análise textual orientada a objetos para o contexto de um sistema de Conta de Luz, extraindo com precisão as classes, atributos e métodos envolvidos.

Contexto do problema: O sistema deve cadastrar contas de luz, que contêm data da leitura, número da leitura, KW gasto, valor a pagar, data do pagamento e média de consumo. Além da persistência do cadastro, o sistema deve fornecer respostas a duas consultas: exibição do mês de menor consumo e exibição do mês de maior consumo.

Suas instruções:
1. Examine o enunciado e liste os nomes das Classes que precisam ser projetadas (ex: ContaDeLuz, SistemaContas).
2. Para cada classe identificada, liste os atributos necessários junto com seus respectivos tipos propostos, acompanhados dos métodos públicos.
3. Certifique-se de prever métodos estritamente focados para atender o cálculo/consulta interativa do mês de menor e maior consumo.
4. Mantenha os nomes padrão Brasil acadêmico (CamelCase para classes, snake_case ou camelCase padronizado para métodos/atributos).
5. A saída deve ser exclusivamente um texto estruturado, profissional e com tom acadêmico (não gere código fonte nem diagramas nesta etapa).
6. Atenção plena: sob nenhuma hipótese invente atributos ou métodos de fora do que foi solicitado no enunciado.

## Prompt 02 — Requisitos funcionais
Atue como um Especialista Sênior em Engenharia de Requisitos. Seu objetivo acadêmico é redigir a lista concisa de Requisitos Funcionais do sistema de cadasto de Conta de Luz, garantindo rastreabilidade lógica contínua desde a análise inicial.

Contexto do problema: A gestão necessita do registro de faturas de luz contemplando os campos: data da leitura, número da leitura, KW gasto, valor a pagar, data do pagamento e média de consumo. O sistema necessitará ter ações de entrada para esses cadastros e as duas saídas de consulta cruciais: mês de menor consumo e de maior consumo.

Suas instruções:
1. Liste detalhadamente os Requisitos Funcionais estruturados em uma lista numerada profissional (ex: RF-01, RF-02).
2. Siga o padrão da literatura usando "O sistema deve permitir..." ou "O sistema deve apresentar...".
3. O escopo é estrito: englobe cadastro rigoroso e as duas consultas citadas.
4. Diretriz crucial: Garanta consistência descritiva. Tudo deve espelhar o enunciado; não inclua ou proponha controle de usuários, logins, ou persistências externas avulsas. Seja literal à necessidade.

## Prompt 03 — Requisitos não funcionais
Atue como um Especialista Sênior em Engenharia de Requisitos e Arquitetura de Software. O seu papel é documentar profissionalmente todos os Requisitos Não Funcionais (RNFs) mandatórios para a aplicação "Conta de Luz".

Restrições base: A solução entregue será integralmente implementada em linguagem Python com o micro-framework Streamlit visando renderização da interface web. Por se tratar de um projeto com foco acadêmico puramente de modelagem e prototipagem, a execução e armazenamento deve ser leve, fluindo localmente.

Suas instruções:
1. Documente os Requisitos Não Funcionais agrupando-os por categorias clássicas de engenharia (ex: Tecnologias, Desempenho, Usabilidade, Manutenibilidade).
2. Utilize uma numeração de padrão traceado (ex: RNF-01, RNF-02).
3. Seja incisivo a respeito das restrições de tecnologia: decrete o uso estrito e exclusivo do Streamlit para o frontend e gerenciamento em memória por via de `session_state` nativo da ferramenta (a adoção de banco de dados só deve ser listada se justificada plenamente caso a memória for um gargalo fatal).
4. Empregue linguagem profissional, formal, e de tom acadêmico, produzindo entregáveis limpos e livres de excessos para os revisores de arquitetura.

## Prompt 04 — Diagrama de classes
Atue como um Arquiteto de Software e Especialista Sênior em UML Estrutural. A sua missão é transferir a análise lógica para uma manifestação representacional estrita gerando o código em formato PlantUML do projeto de controle da Conta de Luz.

Contexto modelado: Classes mapeadas baseadas no cadastro de contas de luz que mantêm a data da leitura, número da leitura, KW gasto, valor a pagar, data de pagamento e média de consumo. São requeridos obrigatoriamente métodos atrelados à varredura e resposta perante as lógicas de obtenção do maior e de menor consumo do sistema.

Suas instruções:
1. Forneça como saída unicamente o bloco de código raw de sintaxe PlantUML aberto por `@startuml` e concluído com `@enduml`.
2. Ilustre a composição das classes contendo a totalidade dos atributos perfeitamente tipados (ex: `- kw_gasto: float`) e a assinatura cirúrgica dos métodos exigidos para dar vazão à regra de negócio de consultas maiores e menores consumos (ex: `+ calcularMesMenorConsumo(): ContaDeLuz`).
3. Mantenha os nomes inequivocamente sincronizados com o modelo conceitual de análise definido nas etapas prévias deste desenvolvimento de software.
4. Nenhuma explicação ou saudação em texto fora do componente de código será tolerada.

## Prompt 05 — Aplicação Streamlit
Atue como um Desenvolvedor Python Sênior focado em aplicações web com o framework Streamlit em contexto de experimentação acadêmica e prova de conceito arquitetural. A meta agora é construir um arquivo Python singular, nominado `app.py`, materializando perfeitamente as regras de negócio de cadastro da Conta de Luz.

Contexto para codificação: É imperativo desenvolver uma interface que admita o ingresso contínuo de registros referentes à Conta de Luz. Cada ocorrência deve carregar os dados especificados pelo domínio: data da leitura, número da leitura, kW gasto, valor a pagar, data do pagamento e média de consumo. O layout deve mostrar de forma persistida painéis dinâmicos dos dados agregados apontando visualmente e com exatidão o mês provido no qual houve o menor consumo registrado, assim como o mês do maior consumo.

Suas instruções:
1. Retorne o aplicativo estrito de forma coesa inserido em um arquivo único referencial `app.py`.
2. Para armazenamento do estado transacional de entrada da UI, instancie uma lista global no escopo do `st.session_state`. Nenhum framework ORM, ou banco de dados externo se faz aplicável aqui sem extrema necessidade de design — mantenha o estado em sessão volátil de fácil testabilidade acadêmica.
3. Modularize rigidamente o layout dividindo-o em funções de renderização nítidas e desacopladas em Python (ex: `def render_cadastro():`, `def render_indicadores_consumo():`).
4. Implemente obrigatoriamente validações nos formulários, barrando campos numéricos negativos ou em branco para assegurar confiabilidade e estabilidade perante o requisito.
5. Crie uma interface limpa, acadêmica e altamente visual. Empregue adequadamente contentores estéticos disponíveis nas documentações mais modernas do pacote Streamlit.
6. Entregue um código maduro e que execute sem erros ao receber o comando básico de `run`.

## Prompt 06 — requirements.txt
Atue como um Arquiteto de Software DevOps voltado ao ecossistema Python. Esta fase exige a compilação do manifesto contendo as diretrizes de dependência requeridas pelas funcionalidades do sistema modelado sobre consumo de Contas de Luz no framework Streamlit.

Contexto: O repositório acadêmico do aplicativo não possui complexas dependências interligadas, dependendo fortemente apenas do runtime principal do pacote `streamlit` contendo talvez um import nativo do `pandas` para tabulações que possam ter sido evocados em tabela.

Suas instruções:
1. Produza estritamente o conteúdo planificado final do seu arquivo de saída, `requirements.txt`.
2. Forneça o arquivo englobando o mínimo possível, contudo recomendando versões genéricas modernas para compatibilidade máxima com ambientes locais de avaliação na disciplina acadêmica.
3. Não escreva textos discorrendo sobre a instalação fora do delimitador de dados que preenche o output exigido puramente para ser colado e processado pelo gerenciador `pip`.

## Prompt 07 — README da questão
Atue como um Tech Lead e Autor Técnico em equipes ágeis, com vasta bagagem acadêmica para formalizações. É o seu encargo redigir um documento primário central sob nome de `README.md` abrangente, voltado à comunidade e aos avaliadores técnicos da aplicação focada em controle de Contas de Luz operado sob interface Streamlit.

Contexto em Foco: A modelagem OO de faturas (data leitura, dt pag, KW, valor pagar etc) obteve vida na estruturação visual respondendo qual o mês de mínimo, assim como o de máximo consumo do escopo registrado. Isto engloba pacotes de Análise, Requirements Funcionais, códigos PlantUML, aplicação SessionState iterativa e requirements.

Suas instruções:
1. Formule uma linguagem erudita, elucidativa e fortemente instrutiva baseada nos pilares do GitHub Flavored Markdown. Empregue blocos de sintaxe enriquecidos (negrito tático, blockquotes para ressalvas).
2. Institua uma hierarquia clássica de projeto contemplando categoricamente estas pautas seções obrigatórias encadeadas: Cabeçalho imponente com Visão Geral e problema central; Estrutura de Diretórios com apresentação semântica ilustrando caminhos esperados (contendo `analise/`, `diagramas/`, `app/`, `README.md`); Quadro de Tecnologias Utilizadas e, por fim, Guia Passo a Passo de Execução de clones locais.
3. Na seção de modelagem cite especificamente porque a segregação orientada a objetos simplificou as agregações de maior e menor consumo exigidas de forma cabal.

## Prompt 08 — Refino final
Atue como um Auditor Técnico Sênior e Revisor de Qualidade (QA) garantindo consistência holística do ciclo de Engenharia de Software. Neste instante final, o escopo demanda uma revisão minuciosa e estruturada de aprovação antes do empacotamento completo rumo à finalização da avaliação de arquitetura para a Conta de Luz.

Suas diretrizes investigativas e proposições que fornecerá:
1. Emita um relatório técnico avaliativo cruzando em sua análise todas as informações previamente documentadas e geradas até agora, passando pela modelagem das Classes, Diagramas, RFs, RNFs e Python.
2. Analise profundamente as nomenclaturas. Proponha resoluções imeditas de inconsistência caso detecte atributos nomeados de forma destoante entre os artefatos de saída (ex: variação entre "data_da_leitura" e "data_leitura" será inaceitável em tom acadêmico).
3. Verifique com rigor e advirta se a modelagem respeitou as fronteiras perfeitamente (se a funcionalidade exata que retorna mês de maior/menor consumo atende às responsabilidades descritas do modelo, conforme escopo enxuto imposto).
4. Entregue um checklist terminal final formatado profissionalmente, apontando em subdiretórios de saída virtuais (`analise/`, `diagramas/`, `app/`) assegurando que não foi materializado 'lixo de código' espúrio. A clareza e fidelidade com o enunciado são a métrica master para atestar o fim deste sistema.
