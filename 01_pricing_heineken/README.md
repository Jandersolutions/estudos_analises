# 🛒 analise_Heineken: Otimização de Pricing e Elasticidade Cruzada no Varejo

<a target="_blank" href="[https://cookiecutter-data-science.drivendata.org/](https://cookiecutter-data-science.drivendata.org/)">
    <img src="[https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter](https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter)" alt="Cookiecutter Data Science" />
</a>
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Polars](https://img.shields.io/badge/Polars-Fast_Data_Frames-yellow.svg)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-Scikit_Learn-orange.svg)

> **Inteligência de Pricing: Protegendo o Lucro Absoluto do supermercado contra a ilusão da margem percentual.**

---

> ⚠️ **REGRA DE OURO DO CHÃO DE LOJA (NÃO FAÇA CTRL+C / CTRL+V)**
> Se você está clonando este repositório para estudar, **não copie e cole os scripts!** Digite o código linha a linha. A memória muscular separa o analista que apenas aperta botões do Engenheiro de Dados que constrói a fundação. Para dominar o ecossistema (Polars, ETL, Machine Learning), você precisa sentir os atritos da sintaxe. Mãos no teclado!

---

## 📌 O Contexto de Negócio (A Dor da Frente de Caixa)
Quem vive o varejo sabe: quando a indústria "caneta" um aumento de custo, o instinto de sobrevivência da operação é repassar o valor para a gôndola. Proteger a margem percentual na planilha do Excel é fácil; o difícil é prever o estrago que isso causa no fluxo da loja.

Este projeto ataca um problema real de **Pricing Estratégico**. A indústria repassou um aumento de R$ 0,50 no custo de reposição da cerveja **Heineken Long Neck 330ml** (Curva A+). A sugestão comercial era subir o preço de R$ 6,50 para R$ 7,20.

**O Ponto Cego:** A Heineken não é apenas uma cerveja; ela é um **KVI (Key Value Item)**. Ela opera como uma **Isca de Tráfego (Loss Leader)**. O objetivo da minha auditoria foi provar que proteger os centavos da margem da bebida espantaria o cliente para o concorrente, sangrando o lucro dos produtos que realmente pagam a conta de luz da loja: a cesta de churrasco do Açougue.

## 🚀 Impacto Financeiro (O Veredito em Reais)
Construí um motor de **Market Basket Analysis** cruzando milhares de cupons fiscais e treinei um modelo de **Regressão Linear** para calcular a Elasticidade Cruzada.

A IA foi implacável: o aumento do preço da cerveja faria o supermercado perder volume de tráfego, resultando em um **rombo projetado de R$ 225,00 por dia** apenas em vendas de Picanha Maturada que deixariam de acontecer. 
**A decisão baseada em dados:** O custo da cerveja foi absorvido para proteger o lucro absoluto gigantesco gerado pelas vendas casadas no Açougue.

---

## 🛠️ Stack Tecnológica (Engenharia de Alta Performance)
No varejo de Big Data, código lento custa dinheiro. Abandonei ferramentas legadas e estruturei este laboratório com o que há de mais agressivo e seguro no mercado:

* **[uv (Astral)](https://docs.astral.sh/uv/):** Gerenciador de pacotes e ambientes virtuais em Rust. Evita dívida técnica e isola dependências em milissegundos.
* **[Polars](https://pola.rs/):** Motor de DataFrames ultrarrápido com tipagem rigorosa. Se o PDV mandar dados sujos, o Polars bloqueia a fraude de auditoria.
* **[Scikit-Learn](https://scikit-learn.org/):** O cérebro matemático para a Regressão Linear.
* **[Marimo](https://marimo.io/):** Framework de relatórios reativos. O fim dos notebooks que quebram quando rodados fora de ordem.
* **[Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/):** Arquitetura CRISP-DM padrão ouro da indústria.

---

## ⚙️ Como Reproduzir a Auditoria (Passo a Passo)

A governança é total. A semente matemática (`seed=42`) está travada para garantir que qualquer C-Level ou auditor chegue no mesmo centavo.

### 1. Clone a Matriz e Entre na Pasta
```bash
git clone https://github.com/SEU_USUARIO/analise_heineken.git
cd analise_heineken
```


### 2. Levante o Ambiente Blindado

```bash
uv add polars marimo numpy scikit-learn
```


### 3. Abra o painel executivo

```bash
uv run marimo edit pricing_heineken.py
```


## 🏗️ Estrutura do Repositório (Governança CCDS)

```text

├── README.md          <- O dossiê executivo do projeto.
├── data
│   ├── processed      <- Dados cruzados e limpos para o Machine Learning.
│   └── raw            <- O cofre: log imutável extraído da frente de caixa (PDV).
│
├── notebooks          <- Laboratórios e EDA.
│
├── pyproject.toml     <- O "motor" moderno do projeto, gerenciando dependências.
│
├── reports            <- Relatórios gerados para a Diretoria Comercial.
│
└── analise_heineken   <- O código-fonte da operação.
    │
    ├── __init__.py    
    ├── dataset.py     <- Simulação do ETL do ERP.
    ├── features.py    <- Engenharia de variáveis financeiras (Lucro Bruto, Faturamento).
    └── modeling                
        ├── predict.py <- Inferência de cenários (What-If Analysis).
        └── train.py   <- Treinamento do algoritmo de Regressão Linear.
```
