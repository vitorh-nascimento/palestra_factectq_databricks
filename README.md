# Palestra Fatec Taquaritinga: Do cookie ao dashboard (Databricks & Carreira)

Projeto oficial e repositório de suporte para a palestra conduzida por **Vitor Hugo Nascimento** (Lead Data Engineer & Technical Mentor) na **Fatec Taquaritinga** em 11/11/2026.

---

## 📁 Estrutura do Projeto

O projeto adota o padrão moderno da indústria com **Databricks Asset Bundles (DABs)**:

```text
palestra_factectq_databricks/
├── databricks.yml                      # Configuração do Databricks Asset Bundle (DAB)
├── resources/
│   ├── bakehouse_job.yml              # Definição do Job/Workflow para automação
│   ├── bakehouse_dashboard.yml        # Definição do Dashboard AI/BI Lakeview
│   └── bakehouse_genie.yml            # Definição declarativa do Genie Space (AI Agent)
├── src/
│   ├── notebooks/
│   │   └── demo_bakehouse.py          # Notebook oficial da demo CSI Cookie (formato Databricks)
│   ├── dashboards/
│   │   └── bakehouse_dashboard.lvdash.json # Definição JSON do dashboard executivo
│   ├── genie/
│   │   └── bakehouse_space.geniespace.json # Especificação do espaço conversacional do Genie
│   └── sql/                           # Scripts SQL individuais para cada caso da demo
│       ├── 01_volumetria.sql
│       ├── 02_vendas_por_hora.sql
│       ├── 03_misterio_dia17.sql
│       ├── 04_franquia_campea.sql
│       ├── 05_governanca_lgpd.sql
│       ├── 06_ai_sentiment.sql
│       └── quiz_validacoes.sql
├── GUIA_DO_ALUNO_FATEC.md             # Guia prático para os alunos refazerem em casa
├── .gitignore                         # Padrão para Databricks e Python
└── README.md                          # Este arquivo de documentação
```

---

## 🚀 Como Executar

Você pode explorar o projeto de dois modos:

### Caminho A: Para alunos (Recomendado)
A maneira mais rápida e 100% gratuita no navegador:
1. Acesse **[signup.databricks.com](https://signup.databricks.com)** e crie sua conta no **Databricks Free Edition** (sem cartão de crédito).
2. No menu lateral do workspace, clique em **Workspace** > seu usuário > **Import** (Importar).
3. Selecione o arquivo [`src/notebooks/demo_bakehouse.py`](src/notebooks/demo_bakehouse.py).
4. O catálogo `samples.bakehouse` já vem pré-instalado em todas as contas. Execute as células sequencialmente.

---

### Caminho B: Para quem quer ir além (Deploy via Databricks Asset Bundles)
Para quem deseja testar o fluxo de CI/CD profissional de Engenharia de Dados via Databricks CLI:

1. **Configurar a autenticação:**
   Certifique-se de ter o Databricks CLI instalado (`v1.0.0` ou superior). Configure seu perfil local autenticando com seu workspace:
   ```powershell
   databricks auth login --host <SEU_WORKSPACE_URL>
   ```
   *(A CLI gerencia seu perfil no arquivo `~/.databrickscfg` ou via variável de ambiente `DATABRICKS_HOST`)*.

2. **Validar o bundle:**
   ```powershell
   databricks bundle validate -t dev
   ```

3. **Fazer o deploy para seu workspace:**
   ```powershell
   databricks bundle deploy -t dev
   ```
   *O bundle provisiona automaticamente o notebook, o Job agendado, o espaço do Genie e o Dashboard AI/BI buscando o warehouse disponível via lookup.*

4. **Executar o Job de validação:**
   ```powershell
   databricks bundle run demo_bakehouse_job -t dev
   ```

---

## 🔎 Os 6 Casos + Bônus (CSI Cookie)

Cada investigação possui seu script SQL isolado para consulta rápida em [`src/sql/`](src/sql/):

* [**Caso 1 · Volumetria:** `src/sql/01_volumetria.sql`](src/sql/01_volumetria.sql) — Dimensionamento inicial de linhas com `UNION ALL` no dataset `samples.bakehouse`.
* [**Caso 2 · Vendas por Hora:** `src/sql/02_vendas_por_hora.sql`](src/sql/02_vendas_por_hora.sql) — Detecção de anomalias e identificação de dados sintéticos via agregação por hora.
* [**Caso 3 · O Mistério do Dia 17:** `src/sql/03_misterio_dia17.sql`](src/sql/03_misterio_dia17.sql) — Auditoria de corte temporal e verificação de integridade da carga (`MIN` e `MAX`).
* [**Caso 4 · A Franquia Campeã:** `src/sql/04_franquia_campea.sql`](src/sql/04_franquia_campea.sql) — O primeiro `JOIN` relacional cruzando fatos de vendas e dimensões de franquias.
* [**Caso 5 · Governança & LGPD:** `src/sql/05_governanca_lgpd.sql`](src/sql/05_governanca_lgpd.sql) — Localização de colunas PII e conceito de máscaras dinâmicas de coluna no Unity Catalog.
* [**Caso 6 · GenAI & NL2SQL:** `src/genie/bakehouse_space.geniespace.json`](src/genie/bakehouse_space.geniespace.json) — Agente conversacional do Databricks Genie traduzindo perguntas em português para SQL.

### 💡 Bônus e Quiz

* [**Bônus · IA dentro do SQL:** `src/sql/06_ai_sentiment.sql`](src/sql/06_ai_sentiment.sql) — Análise de sentimento de avaliações de clientes em tempo real com `ai_analyze_sentiment()`.
* [**Quiz Relâmpago:** `src/sql/quiz_validacoes.sql`](src/sql/quiz_validacoes.sql) — Queries de comprovação e gabarito das perguntas da dinâmica com cookies.

---

## 🎓 Para Continuar Estudando e Certificar

* **Databricks Academy:** [databricks.com/learn/training](https://www.databricks.com/learn/training) — Cursos oficiais gratuitos, trilhas de aprendizagem e materiais de estudo.
* **Certificações Databricks:** [databricks.com/learn/certification](https://www.databricks.com/learn/certification) — Guias e exames recomendados (*Data Analyst Associate* e *Data Engineer Associate*).

---

## 📋 Materiais de Apoio

* 👉 [**GUIA_DO_ALUNO_FATEC.md**](GUIA_DO_ALUNO_FATEC.md): Tutorial mastigado para estudantes refazerem a demo e praticarem desafios para portfólio.

---

Palestra realizada por **[Programmers AI, Data & Software](https://www.programmers.com.br)**, parceira Databricks. Conheça também o programa **[Desafiado](https://www.programmers.com.br/desafiado/)**.
