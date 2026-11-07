# Guia de Bolso do Palestrante · Fatec Taquaritinga
**Palestra:** "Do cookie ao dashboard: Databricks & Carreira"  
**Palestrante:** Vitor Hugo Nascimento  
**Data:** 11/11/2026 | **Duração:** 60 minutos  
**Arquivo do Notebook:** [`src/notebooks/demo_bakehouse.py`](src/notebooks/demo_bakehouse.py)

---

## ⏱️ Cronograma de Palco (Minuto a Minuto)

| Minuto | Bloco | Atividade Central | Meta / Gatilho de Atenção |
|---|---|---|---|
| **00 – 05** | Abertura | Conexão como ex-aluno da Fatec; Levantar a mão (Pix, delivery, streaming). | Plateia engajada nos primeiros 120s. |
| **05 – 15** | O que é Área de Dados | Analogia da Padaria (Engenheiro, Analytics Eng, BI, Cientista). | Desmistificar: não precisa ser gênio da matemática. |
| **15 – 22** | Lakehouse & Databricks | Bronze (farinha crua), Silver (massa), Gold (cookie pronto). Porteiro: Unity Catalog. | Explicar arquitetura sem jargões complexos. |
| **22 – 45** | **Demo ao Vivo: CSI Cookie** | Casos 1 a 6 + Bônus de IA no dataset `samples.bakehouse`. | Ensinar a desconfiar do dado; palpites antes das queries. |
| **45 – 52** | **Quiz Relâmpago** | 6 perguntas rápidas valendo cookies físicos. | Elevar energia da sala ao máximo. |
| **52 – 58** | **Carreira & Trajetória** | De estagiário Fatec a Lead Data Engineer no interior; 3 passos práticos. | Mostrar caminho viável e palpável. |
| **58 – 60** | **Encerramento & Q&A** | Frase-âncora ("Desconfiem do dado!"), QR Codes e abertura de perguntas. | Pergunta-gatilho pronta se houver silêncio. |

---

## 🛡️ Matriz de Contingência (Plano B)

| Situação Imprevista | O que fazer no palco (Sem perder o ritmo) |
|---|---|
| **Internet da Fatec oscilou ou caiu** | Mude imediatamente para a apresentação de slides de backup ou vídeo gravado da demo rodando no notebook local. Conduza as perguntas e os palpites da plateia exatamente da mesma forma. |
| **Query demorou para responder (cluster aquecendo)** | Não fique em silêncio esperando. Use o tempo para adiantar o contexto do caso seguinte: *"Enquanto o cluster serverless processa a agregação, me digam uma coisa: vocês já pararam pra pensar como..."* |
| **Databricks Assistant / Genie alucinou ou errou o SQL** | Transforme em momento de ouro e aplique a lição: *"Olhem que excelente exemplo! A IA gerou uma agregação incorreta. Se vocês não soubessem SQL, teriam engolido esse resultado. É exatamente por isso que nós precisamos de profissionais que entendam o dado!"* |
| **Tempo estourou / restam menos de 15 minutos** | Pule o Caso 1 (volumetria), vá direto para os Casos 2 (horários) e 4 (JOIN), reduza o quiz para 4 perguntas e mantenha o bloco de carreira íntegro. |

---

## ❓ FAQ Antecipado: As 5 Perguntas que os Alunos vão Fazer

1. **"Precisa saber muito Python e Estatística para começar em Engenharia de Dados?"**  
   * **Resposta:** *"Para começar, o mais importante é lógica e SQL. A estatística pesada fica mais com Ciência de Dados. O engenheiro lida com organização de dados, pipelines, performance e confiabilidade. Python você aprende a sintaxe básica no primeiro mês para automação."*

2. **"Dá para trabalhar remoto para fora ou para São Paulo morando em Taquaritinga/região?"**  
   * **Resposta:** *"Sim! Eu sou a prova viva disso. Trabalho em Matão/região atendendo clientes nacionais e internacionais. A área de dados é uma das mais consolidadas em regimes remoto e híbrido de tecnologia."*

3. **"Vale a pena aprender Spark puro ou ir direto para o Databricks?"**  
   * **Resposta:** *"O Databricks usa Apache Spark por baixo do capô, mas simplifica 90% da dor de cabeça de infraestrutura. Comecem pelo Databricks Free Edition usando SQL e PySpark. O conceito fundamental de processamento distribuído é o mesmo."*

4. **"Qual nuvem devo escolher primeiro: AWS, Azure ou Google Cloud (GCP)?"**  
   * **Resposta:** *"Tanto faz a nuvem para começar. O Databricks roda nas três com a mesmíssima experiência de usuário. Se você domina a arquitetura Lakehouse e SQL, migrar de Azure para AWS é só questão de entender as permissões da nuvem."*

5. **"Como montar portfólio para conseguir o primeiro estágio sem experiência prévia?"**  
   * **Resposta:** *"Crie uma conta gratuita no Databricks Free Edition, pegue um dataset público do Kaggle ou use a própria Bakehouse, crie uma camada Bronze, Silver e Gold em um notebook público no GitHub e poste um artigo ou print explicativo no LinkedIn. Isso já supera 95% dos currículos em branco."*

