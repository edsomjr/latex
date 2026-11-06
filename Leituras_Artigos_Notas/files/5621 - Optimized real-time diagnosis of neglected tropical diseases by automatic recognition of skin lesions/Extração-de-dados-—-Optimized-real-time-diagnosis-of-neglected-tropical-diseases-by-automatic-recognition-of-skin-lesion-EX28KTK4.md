---
tags: []
parent: 'Optimized real-time diagnosis of neglected tropical diseases by automatic recognition of skin lesions'
collections:
    - TCC_Leituras
$version: 398
$libraryID: 2
$itemKey: EX28KTK4

---
# Extração de dados — Optimized real-time diagnosis of neglected tropical diseases by automatic recognition of skin lesions

Revisão Evidentia 312 · TCC\_Leituras

**1. Título:** Optimized real-time diagnosis of neglected tropical diseases by automatic recognition of skin lesions

**2. Autores:** Nyatte Steyve; Perabi Steve; Mengata Ghislain; Salomé Ndjakomo; Ele pierre

**3. Ano de publicação:** 2022

**4. Fonte de publicação:** Informatics in Medicine Unlocked

**5. Tipo de estudo:** Estudo experimental de desenvolvimento e comparação de classificadores para detecção precoce de três doenças tropicais negligenciadas.

**6. Tipo de veículo de publicação:** Artigo de periódico.

**7. RQ1 Técnica de visão computacional utilizada:** Detecção, segmentação e classificação: conversão para cinza, limiar de Otsu, morfologia (dilatação/erosão), filtros de bordas e textura (Canny, Sober como grafado, Gabor, Robert); medidas da textura, dimensão fractal, zonas homogêneas e bordas.

**8. RQ2 Dataset utilizado:** Base própria de imagens de lesões coletadas em Camarões, com colaboração de profissionais rurais de Akonolinga. Repositório indicado para características/código: dodo12/MTNskin-Diagnosis; imagens mediante solicitação.

**9. RQ2 Características da população / Doença ou manifestação dermatológica:** Três classes: 372 imagens de hanseníase, 420 de úlcera de Buruli, 262 de leishmaniose cutânea. Pretende identificar manifestações precoces. Sem número de pessoas, perfil demográfico ou confirmação por caso descritos.

**10. RQ2 Quantidade de imagens:** 1054

**11. RQ3 Avaliação de desempenho dos modelos:** Tabela 2: em % (acurácia, especificidade, F-score, recall, “Precision/Sensitivity”): KNN 84/67/66/97/88; ANN 94/89/85/84/77; SVM 94/94/86/87/97; BHO-SVM 96/94/89/90/92. Os números são globais para as três doenças, sem desempenho isolado para hanseníase. Média de 27 ms para detectar lesões no computador utilizado.

**12. RQ4 Métricas utilizadas:** Acurácia, especificidade, F-score, recall, coluna rotulada “Precision/Sensitivity” e tempo de processamento. O texto chama os 92% de sensibilidade, embora também informe recall de 90%; não é possível resolver a ambiguidade sem a definição/agregação.

**13. RQ5 Informações sobre tom de pele:** Não informa mensuração do tom ou fototipos. Origem camaronesa, níveis de cinza e variação de iluminação não descrevem distribuição de tons de pele.

**14. RQ6 Comparação do desempenho entre tons de pele:** Sem comparação entre tons de pele.

**15. RQ7 Modelo ou Abordagem:** SVM otimizada por algoritmo Black Hole (BHO-SVM). Tabela 2 compara KNN, rede neural artificial e SVM convencional; o texto também cita árvores de decisão, sem resultados dessa técnica na tabela.

**16. RQ8 Avaliação de generalização do modelo:** Avaliação sobre imagens com diferentes fundos, iluminação, formato/tamanho e contraste. Não testa em base, centro ou população externa; comparação com literatura não equivale a validação externa.

**17. Método de validação:** Protocolo de partição não esclarecido: não informa proporções treino/teste, número de folds ou separação por paciente. As 100 iterações são de otimização, não validação cruzada.

**18. Limitações e conclusões:** Autores concluem potencial para triagem em tempo real e propõem ampliar a base e adicionar variáveis clínicas/ambientais. Limitações para a extração: método de validação e referência diagnóstica pouco descritos, métricas sem estratificação por doença ou pele e nomenclatura ambígua de precisão/sensibilidade. Sem comparação laboratorial prospectiva na mesma população.

## Trechos grifados e comentários

**[p. 1](zotero://open-pdf/library/items/25H3ZWE3?page=1\&annotation=N449IKED)** — “Optimized real-time diagnosis of neglected tropical diseases by automatic recognition of skin lesions”\
Identificação — Estudo experimental, Informatics in Medicine Unlocked, 33 (2022), artigo 101078.

**[p. 4](zotero://open-pdf/library/items/25H3ZWE3?page=4\&annotation=W6UL264S)** — “We counted 372 images of lesions due to leprosy”\
RQ2 — Camarões: 372 imagens de hanseníase, 420 de úlcera de Buruli e 262 de leishmaniose cutânea; 1.054 no total.

**[p. 4](zotero://open-pdf/library/items/25H3ZWE3?page=4\&annotation=2JBJND9H)** — “In Otsu Thresholding, a threshold value is not chosen”\
RQ1 — Limiarização automática de Otsu para binarização após conversão para cinza, seguida de morfologia.

**[p. 8](zotero://open-pdf/library/items/25H3ZWE3?page=8\&annotation=LBDBW8LB)** — “filters (Canny, Sober, Gabor, and Robert)”\
RQ1 — Extração de textura, dimensão fractal, áreas homogêneas e bordas. Sober é a grafia do artigo.

**[p. 5](zotero://open-pdf/library/items/25H3ZWE3?page=5\&annotation=QVL8JZXT)** — “we apply a black hole algorithm (BHO)”\
RQ7 — A meta-heurística Black Hole otimiza a SVM utilizada para classificação.

**[p. 9](zotero://open-pdf/library/items/25H3ZWE3?page=9\&annotation=SC6APD23)** — “Metrics % KNN ANN SVM BHO-SVM”\
RQ3/RQ4 — Tabela 2: BHO-SVM atingiu acurácia 96%, especificidade 94%, F-score 89%, recall 90% e “Precision/Sensitivity” 92%. Os autores usam dois nomes na última linha; resultado não estratificado por doença.

**[p. 9](zotero://open-pdf/library/items/25H3ZWE3?page=9\&annotation=E5EPKAZA)** — “needed only about 27 ms to detect lesions”\
RQ3 — Tempo médio de detecção: 27 ms no computador do estudo (sem evidência de teste em atendimento clínico).

**[p. 10](zotero://open-pdf/library/items/25H3ZWE3?page=10\&annotation=UFG7MNR3)** — “backgrounds, low contrast images, and various lighting conditions.”\
RQ5/RQ6/RQ8 — Há variação visual nas imagens, sem avaliação por pigmentação ou em base externa. Partições de treino/teste não informadas.

**[p. 10](zotero://open-pdf/library/items/25H3ZWE3?page=10\&annotation=IP5UQZEE)** — “we will also combine other types of data”\
Limitações — Ampliação da base e inclusão de dados clínicos e ambientais são propostas futuras.
