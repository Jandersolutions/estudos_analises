import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell(hide_code=True)
def _(mo, os):
    import base64
    # Função para converter a imagem em código Base64
    def get_image_base64(path):
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:image/png;base64,{encoded_string}"

    # Carrega o banner de forma imutável para o export
    img_path = "reports/figures/banner_heineken.png"

    if os.path.exists(img_path):
        banner_executivo = mo.image(
            src=get_image_base64(img_path),
            alt="Banner Dossiê Heineken",
            width="100%",
            rounded=True
        )
    else:
        banner_executivo = mo.md("**Erro:** Banner não encontrado em `reports/figures/`")

    banner_executivo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 🎯 Dossiê Executivo: Otimização de Pricing e Elasticidade de Cesta
        **Projeto:** Auditoria de Repasse de Custo - Heineken LN 330ml
        **Metodologia:** CRISP-DM (Cross-Industry Standard Process for Data Mining)

        ---

        ## 1. O Contexto de Negócio (A Dor da Margem)
        A indústria notificou a nossa rede sobre um aumento no custo de reposição da **Heineken Long Neck 330ml**, passando de **R$ 5,00 para R$ 5,50**.

        A resposta imediata (e instintiva) da operação comercial foi sugerir o repasse integral desse aumento para o consumidor final, subindo o preço de gôndola de **R$ 6,50 para R$ 7,20**. O objetivo dessa manobra seria proteger a margem percentual do setor de Bebidas.

        ## 2. O Risco Estratégico (O "Ponto Cego" do Varejo)


        A Heineken não é um produto comum; ela é um **KVI (Key Value Item - Item Notável)**. Ela pertence à Curva A+ da loja e possui altíssima sensibilidade a preço. O cliente tem o valor de R$ 6,50 memorizado.

        O risco crítico que este laboratório visa auditar é o conceito de **Loss Leader (Isca de Tráfego)**:
        * Se o cliente achar a cerveja cara, ele irá para o concorrente.
        * Se ele for para o concorrente, perderemos apenas os centavos da margem da cerveja, ou perderemos o **lucro inteiro do Açougue** (Picanha, Carvão e Gelo) que ele compraria junto?

        ## 3. O Objetivo da Auditoria (Critério SMART)
        Em vez de tomar decisões baseadas na intuição (feeling) do comprador, este laboratório utiliza Engenharia de Dados de alta performance (**Polars**) e Machine Learning (**Regressão Linear**) para:
        1. Simular o impacto financeiro real do aumento de preço no caixa diário.
        2. Realizar uma **Análise de Cesta de Compras (Market Basket Analysis)** para medir a Taxa de Anexo (Attach Rate) da cerveja com produtos perecíveis.
        3. Calcular a **Elasticidade Cruzada**, provando matematicamente quantos reais o Açougue perde a cada R$ 1,00 que a Bebida sobe.

        A seguir, o detalhamento técnico, o processamento dos logs de PDV e a decisão executiva final para a operação.
    """)
    return


@app.cell
def _():
    import polars as pl
    import numpy as np
    import marimo as mo
    import os 

    return mo, np, os, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quinzena 1: Preço a R$ 6.50
    """)
    return


@app.cell
def _(np, pl):
    np.random.seed(42)
    df_preco_antigo = pl.DataFrame({
        "Preco_Venda_R$":[6.50] * 15,
        "Custo_Unitario_R$":[5.50] * 15, 
        "Volume_Vendido": np.random.normal(120,15,15).astype(int)
    })
    return (df_preco_antigo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quinzena 2: Preço a R$ 7.20 (Repasse de aumento)
    """)
    return


@app.cell
def _(np, pl):
    df_preco_novo = pl.DataFrame({
        "Preco_Venda_R$":[7.20] * 15, 
        "Custo_Unitario_R$":[5.50] * 15, 
        "Volume_Vendido": np.random.normal(75,12,15).astype(int)
    })
    return (df_preco_novo,)


@app.cell
def _(df_preco_antigo, df_preco_novo, pl):
    df_pdv_heineken = pl.concat([df_preco_antigo,df_preco_novo])
    return (df_pdv_heineken,)


@app.cell
def _(df_pdv_heineken, os):
    caminho_raw = "data/raw"
    os.makedirs(caminho_raw, exist_ok=True)
    arquivo_csv = f"{caminho_raw}/pdv_heineken_30dias.csv"
    df_pdv_heineken.write_csv(arquivo_csv)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔒 Governança de Dados Concluída
    O arquivo físico de auditoria foi gerado e salvo com sucesso no cofre: `{arquivo_csv}`.
        A nossa base bruta de operações agora está protegida e pronta para a modelagem financeira.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Extração
    """)
    return


@app.cell
def _(pl):
    caminho_arquivo = "data/raw/pdv_heineken_30dias.csv"
    df_raw = pl.read_csv(caminho_arquivo)
    df_raw 
    return (df_raw,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Transformação
    """)
    return


@app.cell
def _(df_raw, pl):
    df_financeiro = df_raw.with_columns(
        (pl.col("Preco_Venda_R$") * pl.col("Volume_Vendido")).alias("Faturamento_R$"), 
        (pl.col("Custo_Unitario_R$") * pl.col("Volume_Vendido")). alias("Custo_Total_R$")
    ).with_columns(
        (pl.col("Faturamento_R$") - pl.col("Custo_Total_R$")).alias("Lucro_Bruto_R$")
    )
    df_financeiro 
    return (df_financeiro,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Modegem
    """)
    return


@app.cell
def _(df_financeiro, pl):
    df_resultado = (
        df_financeiro.group_by("Preco_Venda_R$").agg(
            pl.col("Volume_Vendido").sum().alias("Total_Garrafas_Vendidas"),
            pl.col("Faturamento_R$").sum().round(2).alias("Faturamento_Total_R$"),
            pl.col("Lucro_Bruto_R$").sum().round(2).alias("Lucro_Bruto_Total_R$")
        ).sort("Preco_Venda_R$")
    )
    df_resultado 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Considerando que o fabricante elevou o preço a 5.50
    * cenario 1 = 6.50
    * cenario 2 - 7.20
    """)
    return


@app.cell
def _():
    lucro_6_50 = (6.50 - 5.50) * 1795
    lucro_6_50 
    return


@app.cell
def _():
    lucro_7_20 = (7.20 - 5.50) * 1781
    lucro_7_20 
    return


@app.cell
def _(np, pl):
    np.random.seed(42) 
    n_cupons = 5000
    cupons_heineken = np.arange(1, int(n_cupons * 0.3) + 1)
    dados_pdv = []
    for cupom in range(1, n_cupons + 1):
        # Todo cliente compra o básico
        dados_pdv.append({"Cupom_ID": cupom, "Produto": "Pao Frances 1KG", "Lucro_R$": 2.50})

        # Se o cliente é do grupo que comprou Heineken...
        if cupom in cupons_heineken:
            dados_pdv.append({"Cupom_ID": cupom, "Produto": "Heineken LN 330ml", "Lucro_R$": 1.00})

            # O comportamento âncora: 70% de chance de levar itens de churrasco junto!
            if np.random.rand() > 0.3:
                dados_pdv.append({"Cupom_ID": cupom, "Produto": "Picanha Maturada a Vácuo", "Lucro_R$": 25.00})
                dados_pdv.append({"Cupom_ID": cupom, "Produto": "Carvao Eucalipto 3KG", "Lucro_R$": 8.50})
                dados_pdv.append({"Cupom_ID": cupom, "Produto": "Gelo Filtrado 5KG", "Lucro_R$": 4.00})

    df_cupons_brutos = pl.DataFrame(dados_pdv)
    df_cupons_brutos
    return (df_cupons_brutos,)


@app.cell
def _(df_cupons_brutos, pl):
    # Passo A: Quais cupons tem Heineken? (Isolando a isca)
    ids_com_heineken = (
        df_cupons_brutos
        .filter(pl.col("Produto") == "Heineken LN 330ml")
        .select("Cupom_ID")
    )

    # Passo B: Pegar TODOS os produtos que estavam DENTRO desses mesmos cupons (Inner Join)
    df_cesta_completa = df_cupons_brutos.join(ids_com_heineken, on="Cupom_ID", how="inner")

    # Passo C: Tirar a Heineken da lista para ver apenas o "Lucro Indireto" dos acompanhantes
    df_acompanhantes = df_cesta_completa.filter(pl.col("Produto") != "Heineken LN 330ml")

    # Passo D: Calcular a frequência e o Lucro Indireto Total gerado pela âncora
    df_analise_cesta = (
        df_acompanhantes.group_by("Produto")
        .agg(
            pl.col("Cupom_ID").count().alias("Vezes_Comprado_Junto"),
            pl.col("Lucro_R$").sum().round(2).alias("Lucro_Indireto_Gerado_R$")
        )
        .sort("Lucro_Indireto_Gerado_R$", descending=True)
    )
    df_analise_cesta
    return


@app.cell
def _(mo, np, pl):

    from sklearn.linear_model import LinearRegression

    # ==========================================
    # 1. ETL: DADOS HISTÓRICOS (Preço Cerveja vs Venda Picanha)
    # ==========================================
    np.random.seed(42)
    dias = 60

    # Simulamos flutuações de preço da Heineken entre R$ 6.00 e R$ 8.00 ao longo de 60 dias
    preco_heineken_hist = np.random.uniform(6.00, 8.00, dias)

    # A regra de negócio embutida: Quanto mais cara a cerveja, menos picanha sai.
    # Volume Base = 150 peças. A cada R$ 1 na cerveja, perdemos em média 12 peças de carne (+ um ruído aleatório)
    venda_picanha_hist = 150 - (12 * preco_heineken_hist) + np.random.normal(0, 5, dias)

    df_hist = pl.DataFrame({
        "Preco_Heineken_R$": preco_heineken_hist,
        "Volume_Picanha": venda_picanha_hist.astype(int)
    })

    # ==========================================
    # 2. MODELAGEM PREDITIVA (Regressão Linear - CRISP-DM Fase 3)
    # ==========================================
    # Separando a variável preditora (X) e a variável alvo (y)
    X = df_hist["Preco_Heineken_R$"].to_numpy().reshape(-1, 1)
    y = df_hist["Volume_Picanha"].to_numpy()

    # Treinando o cérebro da máquina
    modelo = LinearRegression()
    modelo.fit(X, y)

    # O modelo descobriu a sensibilidade! 
    # modelo.coef_[0] nos diz quantas carnes perdemos por cada R$ 1,00 de aumento.

    # ==========================================
    # 3. TESTE DE CENÁRIOS (What-If Analysis)
    # ==========================================
    # Simulando o impacto dos nossos dois preços
    cenarios_preco = np.array([[6.50], [7.20]])
    previsao_picanha = modelo.predict(cenarios_preco).astype(int)

    df_cenarios = pl.DataFrame({
        "Cenario_Preco_Heineken_R$": [6.50, 7.20],
        "Previsao_Venda_Picanha_Qtd": previsao_picanha
    }).with_columns(
        # A Picanha nos dá R$ 25,00 de lucro limpo por peça
        (pl.col("Previsao_Venda_Picanha_Qtd") * 25.00).alias("Lucro_Projetado_Picanha_R$")
    )

    # Calculando a perda absoluta entre os dois cenários
    lucro_baixo = df_cenarios.filter(pl.col("Cenario_Preco_Heineken_R$") == 7.20)["Lucro_Projetado_Picanha_R$"][0]
    lucro_alto = df_cenarios.filter(pl.col("Cenario_Preco_Heineken_R$") == 6.50)["Lucro_Projetado_Picanha_R$"][0]
    perda_financeira = lucro_alto - lucro_baixo

    # ==========================================
    # 4. APRESENTAÇÃO GERENCIAL (MARIMO NATIVO)
    # ==========================================
    painel_ia = mo.vstack([
        mo.md("""
        ### 🤖 IA de Pricing: Regressão Linear de Elasticidade Cruzada

        O modelo de Machine Learning analisou 60 dias de histórico e encontrou a correlação matemática exata entre o preço da cerveja e a venda da carne.

        **Resultados da Projeção Diária:**
        """),

        # Passamos o DataFrame solto. O Marimo renderiza a tabela perfeita automaticamente!
        df_cenarios,

        mo.md(f"""
        🚨 **ALERTA DE ROMBO NO AÇOUGUE:** A Regressão Linear prova que, ao subirmos a Heineken para R$ 7.20, nós perderemos **R$ {perda_financeira:.2f} por dia** APENAS no lucro da Picanha. Isso destrói qualquer ganho de centavos que teríamos na margem da cerveja.
        """)
    ])

    # Retornando a variável no final da célula para exibir na tela
    painel_ia
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    * O Cenário 1 (A Isca Funcionando - Preço a R$ 6,50): A Inteligência Artificial previu que, com a cerveja barata atraindo clientes, venderemos 71 peças de picanha naquele dia.Cálculo Financeiro: 71 carnes $\times$ R$ 25,00 = R$ 1.775,00 de lucro no Açougue.
    * O Cenário 2 (A Isca Quebrada - Preço a R$ 7,20):A IA previu que o cliente achou a cerveja cara e foi para a concorrência. Com isso, a venda da picanha despenca para apenas 62 peças.Cálculo Financeiro: 62 carnes $\times$ R$ 25,00 = R$ 1.550,00 de lucro no Açougue.O Veredito Final (A Diferença):R$ 1.775,00 (Cenário Bom) - R$ 1.550,00 (Cenário Ruim) = R$ 225,00.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### "Senhores diretores, ao tentarmos proteger alguns centavos de margem na cerveja subindo o preço para R$ 7,20, nós causamos uma fuga de fluxo na loja. Essa fuga nos fez deixar de vender 9 peças de Picanha por dia (de 71 caiu para 62). Como a picanha é o nosso "Ouro", perder essas 9 vendas significa tirar R$ 225,00 de dinheiro vivo do nosso caixa diário. A cerveja deve continuar a R$ 6,50 para proteger o lucro do Açougue."
    """)
    return


@app.cell
def _(mo):


    # ==========================================
    # GERAÇÃO DO DOSSIÊ TÉCNICO E EXECUTIVO (CRISP-DM: DEPLOYMENT)
    # ==========================================

    dossie_final = mo.md(
        """
        # 📑 Dossiê Técnico e Executivo: Otimização de Pricing KVI (Heineken LN)
        **Área:** Inteligência Comercial & Data Science
        **Stack Tecnológica:** Python, Polars, Scikit-Learn, Marimo, UV (Cookiecutter)

        ---

        ## 1. Entendimento do Negócio (A Dor)
        A indústria repassou um aumento de custo de R$ 5,00 para R$ 5,50 no produto Curva A+ (Heineken LN 330ml). O instinto inicial da operação foi repassar o custo ao cliente (R$ 7,20) para proteger a margem percentual. O objetivo deste projeto foi validar matematicamente qual preço (R$ 6,50 ou R$ 7,20) maximiza o Lucro Bruto Absoluto da loja.

        ## 2. Arquitetura e Engenharia de Dados (ETL)
        O projeto foi estruturado sob rigorosa governança de dados:
        * **Fundação:** Utilização do *Cookiecutter Data Science* com gerenciador `uv` para isolamento de dependências, prevenindo dívida técnica.
        * **Extração e Cofre:** Geração de um simulador de PDV (`np.random.normal`) para 30 dias de operação, com a trava de aleatoriedade (`seed=42`) para garantir 100% de reprodutibilidade em auditorias. O arquivo bruto foi isolado fisicamente em `data/raw/pdv_heineken_30dias.csv`.

        ### 🚧 Trincheiras do Código (Lições Aprendidas na Operação):
        Durante a engenharia de dados, enfrentamos e superamos atritos reais de integração de sistemas:
        1. **Sintaxe de Módulos:** O erro `TypeError: 'module' object is not callable` ao tentar usar `np.random(42)`. A correção reforçou o uso correto dos métodos internos (`np.random.seed(42)`).
        2. **Tipagem de Dados em Python:** A compreensão de que a sintaxe `[6.50] * 15` em Python não representa um cálculo de margem percentual, mas sim a replicação de uma variável em lista ao longo de 15 dias para simular a etiqueta de preço estática na gôndola.
        3. **Case Sensitivity e Governança:** O colapso do `pl.concat` (ShapeError) devido a uma divergência de capitalização (`Preco_Venda_R$` vs `Preco_venda_R$`). O rigor do **Polars** bloqueou a concatenação, prevenindo que um dado sujo corrompesse o cálculo final. 

        ## 3. Modelagem Analítica e a Visão Estratégica
        O primeiro cruzamento de dados revelou que o aumento para R$ 7,20, avaliando o produto de forma isolada, traria maior lucro por unidade devido à queda de custo de reposição. 

        **O Ponto de Virada (Market Basket Analysis):**
        A análise não parou na margem do item. Foi levantada a hipótese de comportamento de compra cruzada. Ao analisarmos o *Attach Rate* (Taxa de Anexo), os dados provaram que a Heineken é um produto **KVI (Isca de Tráfego)**. Clientes que compram a cerveja a R$ 6,50 têm alta probabilidade de ancorar produtos de alta margem no carrinho, especificamente itens de churrasco.

        ## 4. Inteligência Artificial e Veredito (O Risco de R$ 225/dia)
        Para quantificar o risco de ruptura de fluxo, implantamos um modelo preditivo de **Regressão Linear** (`scikit-learn`) focado em Elasticidade Cruzada da Demanda.

        **A Matemática do Chão de Loja:**
        * A IA provou que a cada aumento no preço da cerveja, perdemos volume de Picanha.
        * Cenário A (Cerveja a R$ 6,50): Previsão de venda de 71 peças de Picanha (Lucro: R$ 1.775,00).
        * Cenário B (Cerveja a R$ 7,20): Fuga de clientes derruba a venda para 62 peças (Lucro: R$ 1.550,00).
        * **O Rombo:** A diferença entre os cenários resultou em uma perda projetada de exatos **R$ 225,00 diários** (9 peças não vendidas x R$ 25,00 de lucro limpo por peça).

        ### 🎯 A Ordem Executiva
        **A etiqueta da Heineken LN deve ser mantida a R$ 6,50.** O varejo não vive de margem percentual de cerveja; vive de Lucro Bruto Absoluto de carrinho. A estratégia de *Loss Leader* absorve o custo da indústria para proteger as centenas de reais geradas diariamente pelo açougue.
        """
    )

    # Exibindo o relatório na tela do Marimo
    dossie_final
    return


if __name__ == "__main__":
    app.run()
