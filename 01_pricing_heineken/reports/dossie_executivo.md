# 📊 RELATÓRIO EXECUTIVO DE PRECIFICAÇÃO E ELASTICIDADE DE CESTA
**Documento Confidencial - Uso Interno da Diretoria Comercial**

**Data:** Março de 2026  
**Autor:** Janderson Batista Abreu | Inteligência de Dados & Pricing  
**Produto Auditado:** Cerveja Heineken Long Neck 330ml (Curva A+ / KVI)  

---

## 1. Sumário Executivo
A indústria notificou a rede sobre um reajuste no custo de reposição da Heineken LN de **R$ 5,00 para R$ 5,50**. A hipótese inicial da operação comercial era repassar o custo ao consumidor, elevando o preço de gôndola de R$ 6,50 para R$ 7,20, visando proteger a margem percentual da categoria de Bebidas.

Após auditoria de dados e simulações com Inteligência Artificial cruzando milhares de cupons fiscais, **desaconselhamos fortemente o aumento de preço**. A proteção de centavos na cerveja provocará uma fuga de fluxo de clientes que custará à loja **R$ 225,00 diários em lucro perdido** no setor do Açougue. A recomendação é manter o preço a R$ 6,50 e utilizar o produto como "Isca de Tráfego" (Loss Leader).

---

## 2. O Cenário: A Ilusão da Margem Individual
A análise isolada do produto sugere que o aumento para R$ 7,20 é favorável, pois, mesmo vendendo menos garrafas, a margem unitária compensaria a queda de volume. No entanto, no varejo físico, **não vendemos produtos isolados; vendemos cestas de compras.**

A Heineken LN é um item notável (KVI - *Key Value Item*). O consumidor memoriza seu preço e julga a competitividade da loja inteira com base nele.

---

## 3. Auditoria de Dados: O Efeito Âncora (Market Basket Analysis)
Para validar o comportamento do consumidor, a equipe de Dados extraiu uma amostra representativa de cupons fiscais da frente de caixa e aplicou um algoritmo de *Market Basket Analysis* (Análise de Cesta).

**A Descoberta:** Clientes que são atraídos pela Heineken não compram apenas cerveja. Identificamos uma fortíssima **Taxa de Anexo (Attach Rate)** com o setor de Perecíveis/Açougue.

* Aproximadamente **30% dos carrinhos** que contêm Heineken LN também levam itens de churrasco (Picanha Maturada, Carvão e Gelo).
* O lucro gerado por esses produtos "acompanhantes" é vastamente superior à margem da própria bebida.



---

## 4. Projeção de Risco (Machine Learning & Elasticidade Cruzada)
Para quantificar o risco de alterar a etiqueta da cerveja, treinamos um modelo preditivo de **Regressão Linear** para medir a Elasticidade Cruzada da Demanda. O objetivo foi responder: *"A cada Real que subimos na cerveja, quanto perdemos de venda nas carnes?"*

O modelo projetou os dois cenários para o caixa diário da loja, focando no produto âncora de maior rentabilidade (Picanha):

| Cenário de Preço (Heineken) | Margem da Cerveja | Previsão de Venda (Picanha) | Lucro Gerado (Açougue) |
| :--- | :---: | :---: | :---: |
| **Cenário A: R$ 6,50 (Atual)** | Apertada (Absorve custo) | 71 peças / dia | **R$ 1.775,00** |
| **Cenário B: R$ 7,20 (Aumento)** | Protegida (Repassa custo) | 62 peças / dia | **R$ 1.550,00** |

**🚨 O Risco Financeiro:** Ao optar pelo Cenário B, a loja experimenta uma redução de tráfego que resulta na não-venda de 9 peças de Picanha por dia. Isso representa um **rombo de R$ 225,00 diários (R$ 6.750,00/mês)** apenas no lucro bruto deste corte específico. O ganho marginal obtido com a cerveja mais cara é completamente obliterado pela perda no açougue.

---

## 5. Recomendação Estratégica
A Inteligência de Dados recomenda que a Diretoria Comercial adote as seguintes diretrizes:

1. **Congelamento de Preço:** Manter a Heineken LN a R$ 6,50. 
2. **Estratégia de Loss Leader:** Aceitar a redução de margem da categoria de Bebidas, tratando esse custo como "Investimento em Aquisição de Cliente" para o Açougue.
3. **Ação de Cross-Merchandising:** Posicionar pontos extras (ilhas) de carvão e cerveja próximos à vitrine de carnes premium para forçar o aumento do ticket médio e maximizar o efeito âncora mapeado pelos dados.


