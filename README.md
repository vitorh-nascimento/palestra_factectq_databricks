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
├── GUIA_PALESTRANTE_FATEC_TAQUARITINGA.md # Roteiro de palco, minutagem, contingência e FAQ
├── GUIA_DO_ALUNO_FATEC.md             # Guia prático para os alunos refazerem em casa
├── .gitignore                         # Padrão para Databricks e Python
└── README.md                          # Este arquivo de documentação
```

---

## 🚀 Como Executar

### Opção 1: Databricks Free Edition (Web UI)
1. Acesse [signup.databricks.com](https://signup.databricks.com) e crie/acesse sua conta gratuita (Free Edition).
2. No menu lateral, acesse **Workspace** > seu usuário > clique em **Import** (Importar).
3. Selecione o arquivo [`src/notebooks/demo_bakehouse.py`](file:///c:/dev/palestra_factectq_databricks/src/notebooks/demo_bakehouse.py).
4. O catálogo `samples.bakehouse` já vem pré-carregado no ambiente. Execute as células sequencialmente.

---

### Opção 2: Databricks CLI & Asset Bundles (DAB)

O projeto já está configurado para o seu workspace `https://dbc-08a827af-160b.cloud.databricks.com` com o profile ativo `dbc-08a827af-160b` e o **Serverless Starter Warehouse** (`741245947a35cac0`).

1. **Validar a configuração do bundle:**
   ```powershell
   databricks bundle validate
   ```

2. **Fazer o deploy para o workspace:**
   ```powershell
   databricks bundle deploy -t dev
   ```

3. **Executar o Job de validação da demo:**
   ```powershell
   databricks bundle run demo_bakehouse_job -t dev
   ```

---

## 🎯 Conteúdos Inclusos na Demo (CSI Cookie)

1. **Caso 1 (Volumetria):** Dimensionamento de linhas com `UNION ALL` no dataset `samples.bakehouse`.
2. **Caso 2 (Padrão Temporal):** Detecção de anomalias e conceito de dados sintéticos via `GROUP BY HOUR`.
3. **Caso 3 (Janela de Carga):** O mistério da queda de vendas do dia 17 e a importância de verificar `MIN` e `MAX`.
4. **Caso 4 (JOIN Relacional):** Identificação da franquia líder de faturamento (`sales_transactions` + `sales_franchises`).
5. **Caso 5 (Governança & LGPD):** Detecção de dados sensíveis (PII) e mascaramento dinâmico via Unity Catalog.
6. **Caso 6 (GenAI & NL2SQL):** Databricks Assistant e Genie convertendo português em SQL.
7. **Bônus (AI Functions):** Análise de sentimento de avaliações em tempo real com `ai_analyze_sentiment()`.

---

## 📋 Materiais de Apoio ao Palestrante

Consulte o documento completo:
👉 [**GUIA_PALESTRANTE_FATEC_TAQUARITINGA.md**](file:///c:/dev/palestra_factectq_databricks/GUIA_PALESTRANTE_FATEC_TAQUARITINGA.md)
* Minutagem detalhada de palco (0 a 60 min)
* Matriz de contingência (Plano B para internet, queries e cluster)
* Gabarito oficial do Quiz Relâmpago com os cookies
* FAQ das 5 perguntas mais frequentes de alunos de graduação
