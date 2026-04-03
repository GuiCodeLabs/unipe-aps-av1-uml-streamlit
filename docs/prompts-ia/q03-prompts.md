# Questão 03 — Boneco em Movimento

## Prompt 01 — Análise
Atue como um Especialista Sênior em Engenharia de Prompt e Análise e Projeto de Sistemas. Sua tarefa primária é planejar a análise estrita em texto e formatar a camada lógica inicial orientada a objetos para resolver o sistema de controle de um Boneco em Movimento.

Contexto do problema: Uma arquitetura enxuta lida com uma essência física: um boneco contendo características de base imperativas que são nome, a marcação de posição no eixo X e posição no eixo Y em tela cartesianas, associado de pertencer à uma direção atual limitando-se unicamente às opções cardiais lógicas estáticas: cima, baixo, direita ou esquerda.

Suas instruções:
1. Examine as exigências do contexto supracitado. Mapeie expressamente quais são as Classes resultantes desta avaliação, descrevendo textualmente suas atuações essenciais.
2. Extraia os atributos fundamentais detalhados junto com tipos recomendados, baseados na imutabilidade das quatro posições do Boneco.
3. Formalize os métodos que devem governar os desdobramentos motores de estado sobre os eixos X e Y.
4. Mantenha os nomes aderindo fielmente às boas práticas de padrão camelCase ou snake_case apropriado do linguajar em programação com nomes em português do Brasil, num contexto puramente da classe acadêmica.
5. Não responda códigos ou gere marcações UML agora. E não invente características ausentes (velocidade de pulo ou vida não são solicitados). Foque no texto de modelagem.

## Prompt 02 — Requisitos funcionais
Atue como um Especialista Sênior em Engenharia de Requisitos Acadêmicos. Traga o modelo da análise anterior e aplique sua expertise transacionando seus princípios para uma estrutura de levantamento formal de necessidades (Requisitos Funcionais) visando interagir assertivamente com simulações de transição de posição em eixos sobre o "Boneco".

Contexto do problema: O boneco existe, possui um nome e está em determinada região da tela caracterizado pela posição X e a posição Y, estando atrelado de forma orientacional às direções (cima, baixo, direita e esquerda).

Suas instruções:
1. Liste os Requisitos Funcionais extraídos que a aplicação futura deverá entregar ao cliente da modelagem, expressos de modo catalogado e com identificação formal RF (como RF-01, RF-02).
2. Utilize formulação frasal mandatória: "O sistema deve autorizar o acesso à transição de...", "O sistema deve recalcular automaticamente...".
3. Mantenha uma correlação forte do que será efetuado pelo boneco interativamente com as atualizações que implicarão perante os atributos de eixo solicitados na restrição acadêmica sem expansão exacerbada.

## Prompt 03 — Requisitos não funcionais
Atue como um Arquiteto de Software focado também em Requisitos Complementares não Funcionais. O alvo do documento está nas exigências qualitativas para suportar estavelmente as funções sistêmicas de manipulação lógica atreladas a um Boneco em eixos X e Y.

Contexto limitativo: A execução deverá ser processada sem complicações robustas engessadas usando estritamente linguagem de programação em Python sobre a visualização via web framework do Streamlit para testagem simplificada e amostragem na faculdade.

Suas instruções:
1. Documente minuciosamente subcategorias de arquitetura, focando sua restrição total à usabilidade focada em interface limpa perante as mudanças posicionais.
2. Indique o requisito mandatório a execução puramente sob o motor renderizado via interface em botões ou widgets de interação direcional do Streamlit na camada de UI.
3. Estabeleça explicitamente um requisito perante armazenamento de sessão via estado transitório `session_state` e o caráter responsivo atrelado da tela a cada refresh e alteração posicional. Emita o rol no formato oficial de engenharia, como por exemplo RNF-01 à diante, entregando o rol de qualidades e restrições sem complexar redes além da web local.

## Prompt 04 — Diagrama de classes
Atue como um Analista Estrutural Sênior e perito em marcações no formato PlantUML. Baseie o desenho unicamente sobre a essência base imposta na matriz de modelagem sobre o Boneco que movimenta através da abstração do grid do plano de visualização.

Contexto: Foi isolado a criação com atributos fixos sobre identificação (nome) e coordenadas de controle lógico em números (posição X, e posição Y), acrescidas da estrita direção cardial (alocada numa limitação rigorosa sendo cima, baixo, esquerda ou direita).

Suas instruções:
1. Formule exclusivamente a escrita base do Diagrama de Classes e Enumeradores se necessários. Apresente toda marcação no bloco raw fechado entre `@startuml` e iterando para `@enduml`.
2. Inclua o respectivo diagrama com os enums descritivos da Direção (caso decida externalizá-los desta forma por elegância nas restrições cartesianas), e apresente fielmente tipos primitivos correspondentes ao Python, mais métodos interativos perante as atualizações cardiais na estrutura desenhada sobre o Boneco.
3. É vedado ao diagrama extrapolar e manifestar entidades, heranças ou atributos que deturpam o plano original. Todo conteúdo do seu retorno será única e exclusivamente o componente formatado do código. Nenhuma frase acessória passará sob aval do avaliador.

## Prompt 05 — Aplicação Streamlit
Atue como um Desenvolvedor Python Sênior focado em construção fluida no framework Streamlit. Prossiga sobre o diagrama formal gerado previamente na arquitetura conceitual para, via materialização em um projeto Python contendo o controle do "Boneco em Movimento".

Contexto esperado de Codificação: Crie a mecânica onde todo os cenários do diagrama cobrem os dados vivos: O estado deve reconhecer o "nome", o estado cartesiando base posicionado sobre "posição X" e "posição Y". Será exigido também a resposta posicional alocada a direções restritas de "cima, baixo, direita, esquerda".

Suas instruções:
1. O produto técnico é fundamentalmente gerado sobre arquivo nomeado obrigatoriamente como `app.py`. Tudo deve ser comportado dentro e centralizadamente.
2. Atue instancionando o objeto modelado num estado do componente temporal guardando os estados via `st.session_state` com um refresh ágil frente aos inputs dimensionáveis sem requerer uso externo inoportunos e perigosos como conexões via SQLite por ausência descritiva.
3. Implemente no layout botões bem estruturados que respondam perante o fluxo. Use funções nativas lógicas mapeadas num diagrama estético onde ao clicar e movimentar para Direita ou Acima o estado reajusta os números perante a interface de renderização do Streamlit sobre o usuário logado para interagir.
4. Adote condutas como validações onde a direção selecionada é informada nos eixos para impedir movimentos distorcidos num tom formal acadêmico e providencie a robustez requerida isenta funcionalmente de erros nos comandos interativos.

## Prompt 06 — requirements.txt
Atue como um Engenheiro DevOps especializado na montagem do contêiner lógico local em empacotamentos no ecossistema Python. Esta fase requer materialização no formato base cru do descritivo `requirements.txt` sob a lógica de rodar o framework da estrutura gráfica voltado aos "Bonecos em Movimentos" no Streamlit.

Contexto lógico do pacote: Você precisará alinhar como se instala os módulos sem extravagâncias de dados externos da Web, visto que atuará sob coordenadas e estados transitórios básicos com botões do módulo principal do app.

Suas instruções:
1. Forme estritamente o código limpo, isento de introduções explicativas e conversacionais de IA.
2. Contemple internamente a chamada padrão da biblioteca do Streamlit para resolver as construções sistêmicas orientadas do ecossistema e sua arquitetural de estado virtual em Python. Apenas os trechos dos requisitos necessários formam este arquivo.

## Prompt 07 — README da questão
Atue como líder de Arquitetura Sênior de Projetos Ágeis. Como condutor principal de engenharia civil formal num domínio sistêmico documentacional, aplique estruturação plena na formulação rica de Markdown direcionada para preencher a visualização matriz sobre "README.md" associado à base restrita do "Boneco".

Contexto da Documentação: O desenvolvedor universitário desenhou, extraiu e formou na UI do Python um gerenciador posicional perante um objeto físico que movimenta sobre base bidimensional frente as marcações X e Y submetidos num limitante cardinal de orientações do próprio Streamlit via controle statefulness.

Suas restrições documentacionais na montagem textual:
1. Insira linguagem focada voltada a apresentação do modelo OO, detalhando assertivamente a montagem da análise conceitual ligada às limitações dos requisitos implementados.
2. Demonstre visualmente, no sumário e texto base Markdown a expectativa exata de estruturação organizacional com suas pastas padrão solicitadas num fluxo limpo: arquivos divididos sob nomenclaturas `analise/`, `diagramas/`, do script na base iterativa contida em `app/`.
3. Ofereça de forma estritamente polida o procedimento descritivo (Step-By-Step guide) que orienta ao revisor técnico de qualidade (QA) como realizar a carga transacional e execução local via CMD/Terminal executando devidamente a aplicação.

## Prompt 08 — Refino final
Atue como Revisor Final Sênior e Arquiteto de Integração (QA Analist). Retenha sobre seu domínio estrito as checagens perante toda a linha de tempo do que foi processado na produção iterativa para o escopo estático das orientações do "Boneco em Movimento".

Sua diretiva perante aos arquivos criados antes (Análises, as listas RF/RNFs do processo de requerimentos, a transcrição UML de código PlantUML, a formatação em Streamlit e documentações agregadas):
1. Processe e exiba um retorno analítico denso de controle de qualidade atestando que os dados posicionais criados sobre Eixo Cartesianos interagem em perfeita coesão com a nomenclatura criada estaticamente na camada da diagramação estritamente modelada.
2. Inspecione rigidamente de forma simulada as ações de nomes sobre as orientações cardinais. Não devem haver comportamentos no arquivo que induzam distorção de contexto do que estendeu a limitação inicial que impunha ser apenas perpassados cima, baixo, leste (direita) e oeste (esquerda), eliminando invenções em zigue-zague ausentes de análise prévia.
3. Retorne propostas imediatas de lapidação se detectar e emitir parecer da fidelização textual para homogeneizar a coesão geral dos 7 blocos anteriores antes da execução acadêmica final. Responda num relatório curto focando em unicamente validar a entrega.
