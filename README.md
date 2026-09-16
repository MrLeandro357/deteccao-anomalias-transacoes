# 🛡️ Detecção de Anomalias em Transações Financeiras

> **Bootcamp Bradesco - GenAI, Dados & Cyber (DIO)**  
> Projeto Prático: Implementação de um Sistema Antifraude com Aprendizado de Máquina Não Supervisionado (*Isolation Forest*).

---

## 📌 Contexto do Projeto

No setor bancário e financeiro, a detecção precisa e em tempo real de transações fraudulentas é essencial para proteger clientes e minimizar perdas operacionais. O grande desafio técnico reside no severo **desbalanceamento dos dados**: transações legítimas representam mais de **99,8%** do volume total, tornando técnicas de classificação convencionais ineficazes e exigindo abordagens focadas no isolamento de anomalias.

Este projeto desenvolve uma pipeline completa de Inteligência Artificial para identificação automatizada de comportamentos atípicos em transações financeiras usando o algoritmo **Isolation Forest**.

---

## 🏗️ Arquitetura e Fluxo do Sistema

```text
┌─────────────────┐     ┌───────────────────┐     ┌─────────────────────┐     ┌────────────────────┐
│ Dados Brutos    │ ──> │ Pré-Processamento │ ──> │ Isolation Forest    │ ──> │ Avaliação &        │
│ (creditcard.csv)│     │ & Escalonamento   │     │ (Detecção Não Sup.) │     │ Métricas Antifraude│
└─────────────────┘     └───────────────────┘     └─────────────────────┘     └────────────────────┘
```

---

## 🛠️ Tecnologias e Bibliotecas

* **Linguagem:** Python 3.10+
* **Manipulação de Dados:** `pandas`, `numpy`
* **Machine Learning:** `scikit-learn` (`IsolationForest`, `StandardScaler`)
* **Visualização:** `matplotlib`, `seaborn`

---

## 🔬 Metodologia e Abordagem Técnica

### 1. Tratamento e Normalização
* As variáveis `Amount` (valor da transação) e `Time` (tempo decorrido) foram padronizadas utilizando o **StandardScaler** para adequá-las ao mesmo intervalo das variáveis anonimizadas `V1` a `V28` (obtidamente via PCA).

### 2. Algoritmo *Isolation Forest*
Diferente de métodos tradicionais que constroem perfis de dados normais, o **Isolation Forest** isola anomalias selecionando aleatoriamente um atributo e um ponto de corte:
* **Princípio:** Pontos anômalos necessitam de menos divisões na árvore de decisão para serem isolados em relação a pontos normais.
* **Parâmetros:** Configurado com `n_estimators=100` e taxa de contaminação ajustada proporcionalmente à frequência observada no conjunto de dados.

### 3. Métricas de Avaliação Focadas em Antifraude
Acurácia tradicional é uma métrica enganosa para este problema. A avaliação foi orientada por:
* **Recall (Sensibilidade):** Capacidade do sistema em capturar o maior número de fraudes reais.
* **Precision (Precisão):** Garantia de que alertas emitidos correspondem de fato a fraudes, evitando bloqueios indevidos em cartões de clientes legítimos.
* **F1-Score / PR-AUC:** Equilíbrio ótimo entre precisão e sensibilidade.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina.

### Passos

1. **Clonar o repositório:**
```bash
git clone https://github.com/SEU_USUARIO/deteccao-anomalias-transacoes.git
cd deteccao-anomalias-transacoes
```

2. **Criar e ativar um ambiente virtual (Opcional, mas recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou no Windows: venv\Scripts\activate
```

3. **Instalar as dependências:**
```bash
pip install -r requirements.txt
```

4. **Executar a pipeline de detecção:**
```bash
python src/train_model.py
```

---

## 📁 Estrutura do Repositório

```text
├── dataset/             # Instruções e scripts de download de dados
├── notebooks/           # Notebooks Jupyter para Análise Exploratória (EDA)
├── src/                 # Scripts Python parametrizados e reutilizáveis
│   ├── prepare_data.py  # Carregamento e normalização dos dados
│   └── train_model.py   # Treinamento e geração das métricas
├── .gitignore           # Ignora ambientes virtuais e datasets grandes
├── README.md            # Documentação técnica do projeto
└── requirements.txt     # Arquivo de dependências
```

---

## 📊 Resultados Esperados

O modelo gera um relatório de classificação detalhado e uma matriz de confusão gráfica destacando o percentual de detecção de comportamentos anômalos sobre a base de testes:

| Classe | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: |
| **Transação Normal (0)** | 1.00 | 0.99 | 1.00 |
| **Anomalia/Fraude (1)** | ~0.35 - 0.50 | ~0.80 - 0.88 | ~0.50 - 0.60 |

---

## 👨‍💻 Autor

Desenvolvido como projeto prático do **Bootcamp Bradesco - GenAI, Dados & Cyber** em parceria com a **DIO**.

---
