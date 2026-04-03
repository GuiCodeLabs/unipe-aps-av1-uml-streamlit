# Estrutura e Metodologia de Engenharia de Prompts

Este documento descreve a arquitetura e a metodologia utilizadas para a criação dos prompts de cada questão (01, 03, 05, 07, 09 e 11). O objetivo desta padronização foi garantir que qualquer IA (como o Claude, ChatGPT ou Gemini) que receba esses prompts gere artefatos consistentes, profissionais e inteiramente fiéis aos enunciados acadêmicos, evitando respostas rasas ou alucinações.

Para garantir resultados unificados em todos os 8 artefatos solicitados (Análise, RF, RNF, Diagrama de Classes, App Streamlit, Requirements, README e Refino), cada prompt foi desenhado seguindo o framework estrutural abaixo:

## 1. Atribuição de Papel Sênior (Role-Prompting)
Todo prompt inicia forçando a IA a encarnar um profissional de alto nível específico para a tarefa daquele recorte. Isso eleva significativamente a qualidade do vocabulário e a profundidade da resposta.
*   **Exemplos utilizados:** *Especialista Sênior em Engenharia de Prompt, Analista Funcional, Arquiteto de Software Especializado em UML, Desenvolvedor Python Sênior focado em Streamlit, Tech Lead.*
*   **Por que funciona:** Evita que a IA responda como um "assistente genérico" e impõe o uso de jargões técnicos adequados (ex: usar termos como "estado transacional", "persistência volátil", "associação").

## 2. Contexto Delimitado (Task Context)
Imediatamente após a atribuição do papel, o prompt injeta a essência da questão. Ao invés de simplesmente mandar a IA "fazer", nós isolamos as regras de negócio para que a IA não precise advinhar ou inferir coisas perigosas.
*   **Exemplos utilizados:** Fornecer os atributos exatos (ex: data, valor, kw, posições X e Y), citar os métodos que precisam de fechamento (ex: "mês de menor consumo").
*   **Por que funciona:** Mantém o domínio fechado. Garante que classes não requisitadas (como "Login" ou "Autenticação") não sejam inventadas no meio da prova.

## 3. Instruções Limpas e Imperativas (Directives)
A parte operacional do prompt. Sempre construída em formato de lista numerada (1, 2, 3...) contendo verbos de ação imperativos.
*   **Diretrizes aplicadas:** "Examine", "Liste", "Utilize a numeração RF-01...", "Escreva no formato...".
*   **Por que funciona:** IAs respondem de forma muito mais coesa e não ignoram etapas quando o fluxo está fragmentado em passos fáceis de processar (Step-by-Step).

## 4. Restrições e Tratamentos Específicos (Constraints)
Esta é a camada de segurança do prompt. Onde nós explicitamente blindamos e proibimos a IA de seguir caminhos não desejados pelas "pegadinhas" ou particularidades restritas de cada enunciado.
*   **Exemplos de blindagem injetada:**
    *   Questão 05 e 07: Exigência vital de forçar que a IA representasse os relacionamentos **exclusivamente como "Atributos Derivados"**.
    *   Questão 09: Regra estrita forçando a IA a gerar um código PlantUML que revelasse **SOMENTE os nomes das classes e multiplicidades**, blindando contra atributos internos.
    *   Geral: Obrigar o uso estrito de `st.session_state` nativo e **proibir** criações extravagantes com bancos de dados complexos para alinhamento rápido e acadêmico.
*   **Por que funciona:** Delimita a fronteira (o que a IA *não* pode fazer), reduzindo drasticamente "Feature Creep" (adição de código desnecessário) e erros de escopo.

## 5. Exigência Exata do Formato de Saída (Output Formatting)
O passo final de cada prompt determina agressivamente o formato de devolução da resposta.
*   **Exemplos utilizados:** O uso obrigatório das tags em código crú `@startuml` a `@enduml`, bloqueio de textos comunicativos (ex: "Aqui está o..."), formatação de textos em listas, obrigatoriedade do App concentrado internamente inteiro no arquivo `app.py`.
*   **Por que funciona:** Prepara saídas amigáveis à esteiras automatizadas, onde o avaliador ou o aluno pode simplesmente "Copiar e Colar" a inteligência transacional pronta.

---

## 💡 Resumo do Fluxo por Artefato
O design transversal da engenharia de prompt obedeceu o alinhamento em esteira (Pipeline):

1. **Análise Textual:** Pensa primeiro no objeto (Classes/Atributos).
2. **RF / RNF:** Pega o objeto pensado e transforma em funcionalidade / restrição acadêmica.
3. **Diagrama (UML):** Exige tradução apenas para código visual (PlantUML).
4. **App (Python):** Absorve as regras para transformar em iteratividade visual na UI web.
5. **Requirements:** Cria a base instaladora crua.
6. **README:** Embrulha o projeto como um portfólio profissional unificado.
7. **Refino Final (QA):** Coloca o LLM contra a parede para atuar criticamente se a IA produtora alucinou ou contradisse os passos anteriores. 
