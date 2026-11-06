---
tags: []
parent: 'Potential of the World Health Organization’s Skin NTDs App to Support and Improve the Detection of Skin-Related Neglected Tropical Diseases: Protocol for a Performance Evaluation and Feasibility Study in Senegal'
collections:
    - TCC_Leituras
$version: 431
$libraryID: 2
$itemKey: L4PWK3M8

---
# Extração de dados — Potential of the World Health Organization’s Skin NTDs App to Support and Improve the Detection of Skin-Related Neglected Tropical Diseases: Protocol for a Performance Evaluation and Feasibility Study in Senegal

Revisão Evidentia 312 · TCC\_Leituras

**1. Título:** Potential of the World Health Organization’s Skin NTDs App to Support and Improve the Detection of Skin-Related Neglected Tropical Diseases: Protocol for a Performance Evaluation and Feasibility Study in Senegal

**2. Autores:** Dior Sall; Dominik Jockers; Pauline Dioussé; Jonas Wachinger; Gilbert Batista; Jose Antonio Ruiz Postigo; Laurene Petitfour; Charlotte Robert; Bachir Mansour Diallo; Fulgence Abdou Faye; Yacine Dieng; Maresa Neuerer; Agbogbenkou Tevi Dela-Dem Lawson; Felicitas Schwermann; Carme Carrion; Louis Hyacinthe Zoubi; Papa Mamadou Diagne; Christa Kasang; Fatou Ndiaye Oumar Sy; Mahamath Cisse; Till Bärnighausen; Madoky Diop

**3. Ano de publicação:** 2025

**4. Fonte de publicação:** JMIR Research Protocols

**5. Tipo de estudo:** Protocolo de estudo de métodos mistos: avaliação quantitativa de acurácia diagnóstica e investigação qualitativa pré-implementação (usabilidade, aceitabilidade e viabilidade).

**6. Tipo de veículo de publicação:** Protocolo publicado em periódico científico.

**7. RQ1 Técnica de visão computacional utilizada:** Classificação por CNN de fotografias de lesões obtidas com smartphone, com sugestões diagnósticas em cascata. Não descreve segmentação, pré-processamento nem treinamento pelos autores.

**8. RQ2 Dataset utilizado:** Coleta planejada de imagens clínicas no hospital regional de Thiès, Senegal (Kobo Collect); inclui também fotografias de pele saudável. Não nomeia dataset público ou identifica os dados de treinamento das CNNs.

**9. RQ2 Características da população / Doença ou manifestação dermatológica:** Pacientes ≥1 ano atendidos na dermatologia de Thiès, com lesão em área não identificável; excluem face, dedos, cicatrizes/tatuagens identificáveis. Inclui DTNs cutâneas como hanseníase e outras dermatoses. Componente qualitativo prevê 70–80 interlocutores, inclusive pessoas de comunidades afetadas pela hanseníase. Alvo quantitativo ≈800 imagens, NÃO total observado.

**10. RQ2 Quantidade de imagens:** Não informado ou não aplicável como total único. Deixar o campo inteiro vazio; ver dataset e população.

**11. RQ3 Avaliação de desempenho dos modelos:** Sem resultados de desempenho neste protocolo. Coleta iniciada em agosto de 2024. Pretende comparar predições com diagnóstico de dermatologista; acerto top-1/3/5 se o diagnóstico de referência estiver na lista. Os 75% de acurácia são hipótese do cálculo amostral e não desempenho observado.

**12. RQ4 Métricas utilizadas:** Planejadas: acurácia, sensibilidade (recall), especificidade, precisão (VPP), F1 e AUC ROC. Avaliações top-1, top-3 e top-5. Segundo classificador sempre atribui uma de 12 DTNs: não estima especificidade contra pele saudável/condições fora da lista.

**13. RQ5 Informações sobre tom de pele:** Tom de pele é citado como possível modificador da acurácia; sem escala ou grupos de fototipos definidos para a análise.

**14. RQ6 Comparação do desempenho entre tons de pele:** Não apresenta resultados ou plano explícito de comparação entre tons de pele.

**15. RQ7 Modelo ou Abordagem:** WHO Skin NTDs App, versão beta: Broad Skin Condition Screener (24 condições comuns + categoria agregada com 12 DTNs) e Skin NTD Classifier (diferencia as 12 DTNs). Duas CNNs em cascata; backbone/versão de pesos não reportados. Árvore de decisão offline é componente distinto.

**16. RQ8 Avaliação de generalização do modelo:** Avaliação planejada do aplicativo existente em pacientes senegaleses com referência local; não há resultados nem identificação da população de treinamento. Estudo em hospital único, não multicêntrico.

**17. Método de validação:** Protocolo de avaliação clínica local prospectiva por comparação independente com dermatologista. Top-1/3/5 e avaliação do segundo algoritmo em casos confirmados de uma das 12 DTNs. Não há divisão de treino/teste ou k-fold, pois não treinam modelos.

**18. Limitações e conclusões:** Amostra limitada ao hospital regional de Thiès; prevalência e espectro de casos podem diferir de outras localidades, e doenças raras podem ficar sub-representadas. A avaliação proposta visa subsidiar a adoção e estudos comunitários; nenhuma acurácia clínica foi demonstrada nesta publicação.

## Trechos grifados e comentários

**[p. 2](zotero://open-pdf/library/items/U3GWPYI7?page=2\&annotation=UVXFEATB)** — “We are conducting a diagnostic accuracy study combined with a qualitative preimplementation usability exploration.”\
Tipo de estudo — Trata-se do protocolo, não do artigo de resultados; combina avaliação diagnóstica e investigação qualitativa.

**[p. 2](zotero://open-pdf/library/items/U3GWPYI7?page=2\&annotation=UFB7C9HE)** — “approximately 800 skin lesion images”\
RQ2 — Aproximadamente 800 é a meta planejada, não uma contagem de imagens já analisadas; deixar vazio o campo inteiro de imagens efetivamente utilizadas.

**[p. 2](zotero://open-pdf/library/items/U3GWPYI7?page=2\&annotation=ZQVC4FG4)** — “the first results expected to be available in 2025.”\
RQ3 — Coleta iniciada em agosto de 2024. Esta publicação não reporta resultados de desempenho.

**[p. 2](zotero://open-pdf/library/items/U3GWPYI7?page=2\&annotation=E2R6V3IP)** — “The app uses 2 AI algorithms in a cascade.”\
RQ1/RQ7 — Duas CNNs do app beta: triagem de 24 condições comuns + classe agrupada DTN; classificador específico diferencia as 12 DTNs, incluindo hanseníase.

**[p. 4](zotero://open-pdf/library/items/U3GWPYI7?page=4\&annotation=VE9XHP6R)** — “aged 1 year or older”\
RQ2 — Pacientes ≥1 ano com lesão visível em área não identificável. Local: dermatologia do hospital regional de Thiès, Senegal.

**[p. 4](zotero://open-pdf/library/items/U3GWPYI7?page=4\&annotation=8GYQ2CUN)** — “we selected 75% as a”\
RQ3 — Acurácia de 75% é pressuposto para dimensionamento da amostra; não transcrever como resultado do modelo.

**[p. 4](zotero://open-pdf/library/items/U3GWPYI7?page=4\&annotation=TRHAMPF3)** — “the dermatologist’s diagnosis as the reference standard”\
Validação/RQ8 — Avaliação clínica planejada do app existente, com diagnóstico do dermatologista como padrão de referência; nenhum resultado externo disponível neste protocolo.

**[p. 2](zotero://open-pdf/library/items/U3GWPYI7?page=2\&annotation=KZJ6EBJ3)** — “including accuracy, sensitivity, specificity, precision, F1-score”\
RQ4 — Métricas planejadas, além de AUC ROC; avaliar acertos top-1, top-3 e top-5. Sem novas métricas medidas aqui.

**[p. 3](zotero://open-pdf/library/items/U3GWPYI7?page=3\&annotation=W3BCGITX)** — “variations in demographic characteristics, skin tones”\
RQ5/RQ6 — Tom de pele é possível fonte de variação, sem classificação sistemática ou resultados estratificados.

**[p. 7](zotero://open-pdf/library/items/U3GWPYI7?page=7\&annotation=4BFHAEDF)** — “limited to skin conditions presented at the dermatology”\
Limitações — Centro único em Thiès; diferenças de prevalência e poucos casos de algumas DTNs podem limitar a generalização e a análise por doença.
