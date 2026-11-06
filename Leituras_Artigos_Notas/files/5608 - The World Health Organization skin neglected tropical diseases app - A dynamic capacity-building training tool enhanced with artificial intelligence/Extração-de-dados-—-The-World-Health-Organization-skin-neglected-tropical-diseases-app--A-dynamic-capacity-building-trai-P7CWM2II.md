---
tags: []
parent: 'The World Health Organization skin neglected tropical diseases app: A dynamic capacity-building training tool enhanced with artificial intelligence'
collections:
    - TCC_Leituras
$version: 388
$libraryID: 2
$itemKey: P7CWM2II

---
# Extração de dados — The World Health Organization skin neglected tropical diseases app: A dynamic capacity-building training tool enhanced with artificial intelligence

Revisão Evidentia 312 · TCC\_Leituras

**1. Título:** The World Health Organization skin neglected tropical diseases app: A dynamic capacity-building training tool enhanced with artificial intelligence

**2. Autores:** Jordi Serrano Pons; Adria Romero-Lopez; Iago Muñoz; Carme Carrion; Aïna Fuster-Casanovas; Jeannine Lemaire; Fernando Vaquero; Montse Garcia; Sarah Anwar; Christophe Hsu; Sofía Paz Villagrán Essmann; Annika B. Wilder-Smith; Caroline Mutio Mule; José Antonio Ruiz-Postigo

**3. Ano de publicação:** 2026

**4. Fonte de publicação:** Journal of Investigative Dermatology. DOI: 10.1016/j.jid.2026.03.043.

**5. Tipo de estudo:** Artigo original: descrição da ferramenta educativa OMS e desenvolvimento/avaliação experimental interna do classificador visual para profissionais de linha de frente.

**6. Tipo de veículo de publicação:** Artigo de periódico.

**7. RQ1 Técnica de visão computacional utilizada:** Recorte central da lesão, entrada RGB de 224 × 224 pixels e normalização pela média/desvio do ImageNet. CNN extrai bordas, textura e forma; triagem binária de NTD cutânea e classificação multiclasse em dois estágios, com lista de até cinco hipóteses.

**8. RQ2 Dataset utilizado:** 5.760 imagens de 12 NTDs cutâneas de publicações OMS e instituições colaboradoras; 16.577 imagens de outras dermatoses do Fitzpatrick17k; 2.469 recortes de pele sã derivados das imagens de NTD; 50.000 imagens não cutâneas do ImageNet. Soma das quatro categorias=74.806; não são todos pacientes nem todas fotos independentes.

**9. RQ2 Características da população / Doença ou manifestação dermatológica:** 12 NTDs cutâneas, incluindo hanseníase, úlcera de Buruli, leishmaniose cutânea, micetoma e outras; noma excluída. Rótulos de dermatologistas ou especialistas clínicos na coleta. Para hanseníase: 302 fotos de treino com tom caracterizado e 41 das 580 imagens do teste por doença; sem total de pessoas/idade/sexo.

**10. RQ2 Quantidade de imagens:** 74806

**11. RQ3 Avaliação de desempenho dos modelos:** Tabela 1, global top-1 → top-5: sensibilidade 80,4→99,8%, especificidade 98,7→62,4%, acurácia 97,7→66,6%, precisão 72,2→15,0%, F1 75,3→24,0%. Tabela 2, hanseníase (n=41): sensibilidade 87,8→97,6%, especificidade 95,7→35,6%, acurácia 95,17→40,0%, precisão 61,10→10,34%, F1 72,0→18,69%. Os 99,8% não são acurácia nem resultado específico de hanseníase.

**12. RQ4 Métricas utilizadas:** Sensibilidade/recall, especificidade, acurácia, precisão/VPP e F1, globais e por doença, top-k (k=1 a 5). Métrica prioritária: sensibilidade top-5, pela finalidade educativa.

**13. RQ5 Informações sobre tom de pele:** Tabela 3: nos 4.418 exemplos de treino de NTDs com tom descrito, claro (equiv. Fitzpatrick I–II) 164/4.418 (4%), moderado (III–IV) 1.147 (26%), escuro (V–VI) 3.107 (70%). Na hanseníase: 0 claros, 70 moderados e 232 escuros (302). Não extrapolar esses percentuais ao acervo inteiro.

**14. RQ6 Comparação do desempenho entre tons de pele:** Não há métricas estratificadas por tom de pele, embora a composição seja descrita. Os autores apontam risco de desempenho inferior em pessoas de pele clara, sem quantificá-lo.

**15. RQ7 Modelo ou Abordagem:** Classificador visual DenseNet-121 da WHO Skin NTDs App: 1) NTD cutânea versus não NTD; 2) diferenciação das 12 NTDs com lista de cinco hipóteses. Não é dispositivo diagnóstico autônomo.

**16. RQ8 Avaliação de generalização do modelo:** Avaliação interna em subconjunto retido da fototeca. Não apresenta validação externa/operacional do classificador; OMS recolhe novas imagens e menciona estudos de campo em diferentes fases. Usabilidade anterior não equivale a teste externo de acurácia.

**17. Método de validação:** Hold-out estratificado: 75% treino, 15% validação e 10% teste. Detecção de duplicatas por similaridade visual antes de dividir; conjuntos de validação/teste isolados. Teste de NTDs por doença soma 580 imagens (Tabela 2).

**18. Limitações e conclusões:** Desbalanceamento (algumas doenças <100 fotos de treino); desempenho top-1 especialmente baixo em cromoblastomicose e esporotricose. Top-5 aumenta sensibilidade à custa de falsos positivos. Sub-representação de pele clara; faltam validação externa e avaliação prospectiva de aprendizado dos profissionais. Uso proposto: formação e apoio, não diagnóstico definitivo.

## Trechos grifados e comentários

**[p. 1](zotero://open-pdf/library/items/6PPZZICI?page=1\&annotation=LFFXKQEI)** — “trained to identify 12 out of 13 skin NTDs through a convolutional neural network (DenseNet-121).”\
Tipo/RQ7: artigo original de desenvolvimento e avaliação interna do classificador da OMS. Identifica 12 NTDs cutâneas; noma excluída.

**[p. 6](zotero://open-pdf/library/items/6PPZZICI?page=6\&annotation=LGI3DNRI)** — “skin NTDs (n = 5760), other skin diseases (excluding NTDs; \[n = 16,577]), healthy skin (n = 2469), and non-skin images (n = 50,000).”\
RQ2: soma das categorias=74.806 imagens. OMS/colaboradores, Fitzpatrick17k, recortes de pele sã e ImageNet, respectivamente; só 5.760 são de NTDs cutâneas.

**[p. 6](zotero://open-pdf/library/items/6PPZZICI?page=6\&annotation=8YMEGZ5E)** — “input dimensions of 224 × 224 pixels required by the network”\
RQ1/RQ7: recorte central, RGB normalizado pelo ImageNet e DenseNet-121 em duas etapas (NTD vs. não NTD e 12 diagnósticos).

**[p. 6](zotero://open-pdf/library/items/6PPZZICI?page=6\&annotation=TKSDAKF6)** — “4% (164/4418) with light skin”\
RQ5/RQ6: no treino de NTDs foram descritas 164 claras (I–II), 1.147 moderadas (III–IV) e 3.107 escuras (V–VI); na hanseníase, 0/70/232. Não há métricas por grupo.

**[p. 6](zotero://open-pdf/library/items/6PPZZICI?page=6\&annotation=JJEXLH4R)** — “The dataset was initially split into training (75%), validation (15%), and test (10%) sets by using stratified sampling”\
Validação: hold-out estratificado com deduplicação visual antes da divisão; amostra de teste interno, sem revalidação em outra base.

**[p. 3](zotero://open-pdf/library/items/6PPZZICI?page=3\&annotation=52ILTZIM)** — “rising from 80.4% for the top-1 to 99.8% for the top-5.”\
RQ3/RQ4: sensibilidade global; top-5 aumenta cobertura, enquanto especificidade cai de 98,7 para 62,4% e precisão de 72,2 para 15%.

**[p. 4](zotero://open-pdf/library/items/6PPZZICI?page=4\&annotation=MMPMNZS9)** — “Leprosy 41 7.07 87.8 97.6 95.7 35.6 95.17 40.0 61.10 10.34 72.0 18.69”\
Tabela 2, hanseníase: 41 fotos (7,07%); pares top-1/top-5 (%): sensibilidade 87,8/97,6; especificidade 95,7/35,6; acurácia 95,17/40; precisão 61,10/10,34; F1 72/18,69.

**[p. 5](zotero://open-pdf/library/items/6PPZZICI?page=5\&annotation=MFR83PQB)** — “some patients will have light skin tones and therefore our database may not perform as desired in that context.”\
Limitação: baixa representação de tons claros pode afetar o desempenho em áreas não endêmicas e migrantes; hipótese, sem comparação de desempenho por fototipo.

**[p. 5](zotero://open-pdf/library/items/6PPZZICI?page=5\&annotation=FIIIBIF8)** — “WHO is currently gathering new images to be used as datasets for external validation.”\
RQ8: a validação externa ainda depende de novos dados; os resultados deste artigo são internos e não medem impacto educacional real.
