---
tags: []
parent: 'Evaluating Advanced Machine Learning Models for... : The American Journal of Dermatopathology'
collections:
    - TCC_Leituras
$version: 292
$libraryID: 2
$itemKey: 3FDTF5DQ

---
# Vargas-Clavijo et al. (2025) — RQs e anotações

**Título:** *Evaluating Advanced Machine Learning Models for Histopathological Diagnosis of Hansen Disease*.\
**Autores:** Mariana Vargas-Clavijo; Nora Cardona-Castro; Juan Pablo Ospina-Gómez; Héctor Serrano-Coll.\
**Publicação:** *The American Journal of Dermatopathology*, 47(4), 301–307, abril de 2025. Artigo original de revista. O PDF apresenta copyright 2024, mas a edição bibliográfica é de 2025. Não localizei DOI no PDF.\
**Fonte:** PDF fornecido pelo usuário; sete páginas. Página 1 do PDF = página editorial 301; página 7 = 307.

A cópia PDF contém **23 grifos com comentários**. O original no Zotero foi preservado. As anotações estão incorporadas à cópia, sem alteração direta do banco de dados do Zotero. Ao final deste documento estão os trechos grifados e os comentários correspondentes, prontos para consulta/cópia.

**Enquadramento:** estudo descritivo, observacional e transversal de classificação de **microfotografias histopatológicas H\&E**, distinguindo hanseníase de pele saudável. Não se trata de fotografias clínicas de lesões externas nem de dermatoscopia. Para a revisão, sua inclusão depende de o escopo aceitar histopatologia como modalidade de análise das manifestações dermatológicas; essa modalidade deve permanecer explicitamente identificada.

## RQ1. Quais técnicas de visão computacional são utilizadas para identificar manifestações dermatológicas associadas à hanseníase?

O estudo utiliza classificação de imagens histopatológicas de cortes de tecido corados por hematoxilina-eosina (H\&E). As microfotografias foram obtidas em microscópio óptico **LEICA dm500**, nas ampliações **4×, 10× e 40×**, e armazenadas em **JPG** (PDF p. 2 / editorial 302; grifo 6).

O fluxo de desenvolvimento segue **CRISP-DM**, com compreensão do problema e dos dados, exploração por histogramas, mapas de calor e gráficos de correlação, preparação/limpeza/integração e confirmação do formato, modelagem e avaliação. Os autores descrevem “normalização” para manter pixels entre **0 e 255**, sem fornecer transformação matemática suficiente para reproduzi-la (grifos 7–8).

Não são especificados tamanho final das imagens, representação vetorial usada nos classificadores, extração explícita de atributos de textura/forma/cor, segmentação de ROI, aumento de dados ou normalização de coloração histológica. Não se deve inferir uma CNN, transferência de aprendizado ou segmentação por aparecerem possibilidades genéricas da ANN na discussão. Os padrões histopatológicos da Tabela 1 e Figura 1 orientam a categorização das imagens; não constituem, por si só, uma etapa computacional de segmentação implementada.

## RQ2. Quais conjuntos de dados e populações são utilizados no desenvolvimento e na avaliação desses modelos?

Foi constituído um **dataset próprio**, selecionado por conveniência de um banco de amostras, com **106 lâminas H\&E**: amostras de **55 pacientes com hanseníase** e **51 controles de pele saudável**. Os controles vieram de tecido descartado em cirurgias plásticas de voluntários sem história pessoal ou familiar de hanseníase. As amostras com hanseníase tinham confirmação clínica, bacteriológica, histopatológica e molecular; o texto cita coloração para bacilos álcool-ácido resistentes e teste de DNA. As lâminas foram reavaliadas e reclassificadas por dermatopatologista (PDF p. 2; grifos 2–4).

| Categoria                | Lâminas/amostras, Tabela 2 | Microfotografias, Tabela 2 |
| ------------------------ | -------------------------- | -------------------------- |
| Hanseníase indeterminada | 26                         | 137                        |
| Espectro tuberculoide    | 14                         | 84                         |
| Espectro lepromatoso     | 15                         | 101                        |
| Pele saudável            | 51                         | 318                        |
| **Total**                | **106**                    | **640**                    |


São **322 imagens com hanseníase** e **318 saudáveis**. As 640 imagens não correspondem a 640 pacientes independentes. O texto apresenta 24,6% de amostras indeterminadas, enquanto a Tabela 2 apresenta 24,5%; a contagem é 26/106, aproximadamente 24,53%. A expressão textual “among the leprosy samples” não deve alterar o denominador das porcentagens da tabela, que é o total de 106 amostras.

O contexto institucional é colombiano (Universidad CES, Instituto Colombiano de Medicina Tropical e Universidad de Antioquia), mas o PDF não detalha locais de recrutamento de cada participante, idade, sexo, etnia, tons de pele ou distribuição geográfica da população. Não há grupo de outras dermatoses para diagnóstico diferencial. Os dados são declarados disponíveis **mediante solicitação aos autores**, sem repositório público identificado (PDF p. 1; grifo 23).

## RQ3. Quais métodos, procedimentos são utilizados para avaliar o desempenho desses modelos e quais resultados são reportados?

A avaliação usa **holdout interno de 80% para treino e 20% para validação**. Aplicado a 640 imagens, isso corresponde a **512 e 128 imagens**, respectivamente, por cálculo. As matrizes de confusão mostram 128 imagens avaliadas: **55 saudáveis e 73 com hanseníase**. Esses denominadores são imagens de avaliação, não os números de pacientes da amostra total (PDF p. 2, 4–5; grifos 9 e 11).

Não se informa se o particionamento ocorreu por paciente ou lâmina, nem estratificação, semente, repetições ou validação cruzada. Como há múltiplas imagens por lâmina, a independência entre treino e validação não fica demonstrada; isso constitui uma limitação de relato e um risco a investigar, não prova de vazamento. Embora legendas usem “test images”, a metodologia descreve apenas treino e validação, sem terceiro conjunto de teste independente.

São comparados cinco modelos por acurácia, sensibilidade, especificidade e matrizes de confusão. Para a ANN também são apresentadas curva ROC/AUC e curva de perda. A **ANN apresenta a maior acurácia e sensibilidade na Tabela 3: 0,70 e 0,74**, com especificidade 0,65 e AUC 0,71. A SVM apresenta maior especificidade (0,80), porém menor sensibilidade (0,47 na tabela; 0,48 na figura). Não são reportados intervalos de confiança ou testes estatísticos de diferença entre modelos.

A perda da ANN estabiliza aproximadamente na 10ª iteração (Figura 4B), mas a curva de treino não demonstra sozinha ausência de sobreajuste. Não há curva pareada de perda de validação ou detalhes suficientes de arquitetura e otimização para reproduzir o treinamento (grifo 20).

A discussão cita sensibilidade de 69% de patologistas para hanseníase indeterminada a partir de outro estudo. **Não houve comparação direta humano versus IA nos mesmos casos**, e a sensibilidade global da ANN não é desempenho específico para a forma indeterminada. Não concluir superioridade clínica dessa comparação indireta (PDF p. 6; grifo 21).

## RQ4. Quais métricas são utilizadas para avaliar o desempenho desses modelos e quais resultados são reportados?

**Transcrição da Tabela 3 (PDF p. 4 / editorial 304; grifos 12–16), escala 0–1:**

| Modelo                       | Acurácia | Sensibilidade / recall | Especificidade |
| ---------------------------- | -------- | ---------------------- | -------------- |
| Rede neural artificial (ANN) | 0,70     | 0,74                   | 0,65           |
| Árvore de decisão (DT)       | 0,67     | 0,59                   | 0,78           |
| SVM                          | 0,61     | 0,47                   | 0,80           |
| Regressão logística (LR)     | 0,65     | 0,55                   | 0,78           |
| Random forest (RF)           | 0,66     | 0,63                   | 0,71           |


A **ROC-AUC da ANN é 0,71** (Figura 4A e texto, grifo 19). Não confundir AUC com acurácia ou probabilidade de diagnóstico correto de uma imagem individual, apesar da interpretação usada no texto. AUC resume capacidade de discriminação ao variar limiares. Não há AUC dos demais modelos apresentada, nem F1, precision/valor preditivo positivo ou intervalos de confiança tabulados. O uso narrativo da palavra “precision” não equivale ao reporte dessa métrica.

**Matrizes das Figuras 2 e 3, conferidas visualmente:**

| Modelo | Verdadeiros negativos | Falsos positivos | Falsos negativos | Verdadeiros positivos |
| ------ | --------------------- | ---------------- | ---------------- | --------------------- |
| ANN    | 36                    | 19               | 19               | 54                    |
| DT     | 43                    | 12               | 30               | 43                    |
| LR     | 43                    | 12               | 33               | 40                    |
| RF     | 39                    | 16               | 27               | 46                    |
| SVM    | 44                    | 11               | 38               | 35                    |


Para ANN, cálculos a partir da matriz resultam em acurácia **90/128 = 70,31%**, sensibilidade **54/73 = 73,97%** e especificidade **36/55 = 65,45%**, compatíveis com os valores arredondados reportados.

**Divergências a preservar:**

*   **RF:** o texto da página editorial 303 apresenta acurácia **63%**, mas Tabela 3 e Figura 3E apresentam **66%**. A matriz fornece 85/128 = **66,41%**. Para síntese, usar 0,66 da tabela com ressalva; não substituir silenciosamente o relato divergente (grifos 16–17).
*   **SVM:** Tabela 3/texto apresentam **0,61 / 0,47 / 0,80**; Figura 3G e legenda apresentam **0,62 / 0,48 / 0,80**. A matriz fornece 79/128 = **61,72%**, 35/73 = **47,95%** e 44/55 = **80%**, coerentes com o arredondamento da figura. Manter ambas as fontes identificadas (grifos 14 e 18).

## RQ5. Como o desempenho dos modelos varia entre diferentes grupos ou tons de pele?

**Não avaliado/reportado.** Não há classificação de tons de pele, distribuição demográfica ou métricas estratificadas por etnia, sexo, idade ou outros grupos. A modalidade H\&E não permite inferir automaticamente o tom de pele clínico dos participantes.

Apesar de o dataset identificar formas indeterminada, tuberculoide e lepromatosa, os resultados são binários e não apresentam sensibilidade por subtipo. Tampouco há resultados separados por ampliação microscópica. A hipótese dos autores de que lesões indeterminadas dificultam a classificação não é acompanhada de uma análise de desempenho por esse grupo. Não concluir equivalência entre grupos a partir dos resultados agregados (PDF p. 6; grifos 21–22).

## RQ6. Quais modelos e abordagens de inteligência artificial são utilizados para identificar manifestações dermatológicas associadas à hanseníase?

São treinados **ANN, árvore de decisão, SVM, regressão logística e random forest**, para classificação binária de microfotografias como pele saudável ou hanseníase (PDF p. 2; grifo 10).

Não são detalhados arquitetura, número de camadas/unidades, ativações ou otimizador da ANN, nem kernel/C da SVM, número de árvores ou critérios de ajuste dos demais modelos. A representação das imagens que alimenta os classificadores também não é suficientemente descrita. Assim, registrar **ANN de arquitetura não especificada**, sem inferir CNN, rede profunda, MLP específico ou modelo pré-treinado.

A ANN foi favorecida pelos autores por acurácia e sensibilidade superiores na comparação apresentada. A SVM preserva maior especificidade à custa de sensibilidade menor. Nenhum resultado demonstra identificação automática de subtipos histopatológicos ou detecção segmentada de nervos, granulomas ou bacilos.

## RQ7. Como a capacidade de generalização dos modelos é avaliada, especialmente quando são utilizados conjuntos de dados diferentes daqueles empregados no treinamento?

A avaliação se limita a **holdout interno do mesmo dataset**. Não há validação em dataset externo, instituição independente, outro microscópio, população adicional ou estudo prospectivo. A unidade de separação entre conjuntos não é esclarecida; isso limita a interpretação da independência das imagens de validação.

Os autores reconhecem a necessidade de ampliar a variedade de microfotografias e **incluir outros diagnósticos diferenciais**, ausentes da comparação com pele saudável. Essas ações são necessidades futuras, não experimentos realizados. Não há comprovação de generalização entre tons de pele, subtipos, serviços ou equipamentos (PDF p. 6; grifo 22).

O desempenho moderado interno e a convergência da perda de treino não demonstram prontidão para implantação clínica. O artigo também não compara diretamente o modelo com patologistas no mesmo conjunto de casos.

## RQ8. O artigo foi publicado em que tipo de veículo de publicação? (revista, conferência)

**Revista científica.** Artigo original (*Original Study*) publicado em **The American Journal of Dermatopathology**, **volume 47, número 4, abril de 2025, páginas 301–307**, Wolters Kluwer. O copyright é 2024; para identificar a edição apresentada, usar **2025**, distinguindo-o de eventual data de publicação antecipada que o PDF não esclarece. Não é artigo de conferência (PDF p. 1; grifo 1).

# Trechos e notas para o Zotero

Cada número corresponde a uma anotação no PDF. Os trechos textuais abaixo são literais, com quebras de linha/hifenização de fim de linha normalizadas. Nas tabelas, os valores são transcritos na ordem das colunas; suas escalas são explicadas em cada nota. Os comentários podem ser copiados diretamente para o Zotero.

## 01. Modalidade e publicação

**Página 1 · Título e identificação editorial**

**Trecho grifado:**

> (Am J Dermatopathol 2025;47:301–307)

**Comentário:**

RQ1/RQ8 — Estudo de diagnóstico histopatológico de hanseníase, com microfotografias de cortes H\&E, e não fotografias clínicas da superfície da pele. Artigo original de revista: The American Journal of Dermatopathology, volume 47, número 4, abril de 2025, páginas 301–307. O copyright 2024 não substitui o ano da edição (2025).

## 02. Desenho e amostra

**Página 2 · Materials and Methods — Study Type and Sample Size**

**Trecho grifado:**

> A descriptive, observational cross-sectional study was conducted on 106 slides with hematoxylin–eosin (H\&E)-stained tissue sections from 55 leprosy patients and 51 healthy skin controls.

**Comentário:**

RQ2/RQ3 — Estudo descritivo, observacional e transversal. São 106 lâminas: 55 pacientes com hanseníase e 51 controles de pele saudável. Diferenciar lâminas/pacientes de 640 microfotografias; imagens não são 640 pacientes independentes.

## 03. Seleção por conveniência e controles

**Página 2 · Study Type and Sample Size**

**Trecho grifado:**

> These samples were selected at convenience from the sample bank with extended informed consent for use in future research, and healthy skin samples were collected from discarded tissue resulting from plastic surgery on volunteer individuals with no personal or family history of leprosy.

**Comentário:**

RQ2/RQ7 — Seleção por conveniência de banco de amostras; controles provenientes de tecido descartado de cirurgia plástica, sem história pessoal/familiar de hanseníase. Não há controle com outras dermatoses, limitando a avaliação do diagnóstico diferencial. O contexto institucional é colombiano, mas os locais de origem e as características demográficas de cada participante não são detalhados.

## 04. Confirmação diagnóstica

**Página 2 · Study Type and Sample Size**

**Trecho grifado:**

> the leprosy patient samples used in the study were confirmed through clinical, bacteriological, histopathological, and molecular diagnostics.

**Comentário:**

RQ2/RQ3 — Confirmação por métodos clínicos, bacteriológicos, histopatológicos e moleculares; o texto menciona coloração para bacilos álcool-ácido resistentes e teste de DNA. As lâminas H\&E foram reavaliadas/reclassificadas por dermatopatologista. Não há análise de concordância entre avaliadores apresentada.

## 05. Dataset de microfotografias

**Página 2 · Study Type and Sample Size**

**Trecho grifado:**

> A total of 640 microphotographs were captured, comprising 318 microphotographs of healthy skin and 322 with leprosy (137 indeterminate, 84 tuberculoid spectrum, and 101 lepromatous spectrum).

**Comentário:**

RQ2 — Dataset próprio: 640 imagens, 318 saudáveis e 322 com hanseníase (137 indeterminadas, 84 espectro tuberculoide, 101 espectro lepromatoso). Tabela 2: 26, 14 e 15 lâminas com esses padrões, respectivamente, mais 51 controles. As métricas são binárias; não há desempenho separado por subtipo.

## 06. Aquisição das imagens

**Página 2 · Study Type and Sample Size**

**Trecho grifado:**

> These were stored in JPG format at 4X, 10X, 40X using a LEICA dm500 optical microscope camera

**Comentário:**

RQ1/RQ2 — Microfotografias JPG de microscópio LEICA dm500, ampliações 4×, 10× e 40×. Não é dermatoscopia nem fotografia clínica. Não são detalhados resolução final, recorte/ROI, segmentação, normalização de cor histológica ou aumento de dados.

## 07. Processo de desenvolvimento

**Página 2 · Design and ML Algorithm Training**

**Trecho grifado:**

> The design and training of the ML algorithm were based on the Cross-Industry Standard Process for Data Mining methodology

**Comentário:**

RQ1/RQ3 — Processo CRISP-DM: compreensão do problema/dados, preparação, modelagem e avaliação. Há exploração com histogramas, mapas de calor e correlações; validação/limpeza/integração e confirmação de formato. Essas etapas não especificam, por si só, uma técnica de extração de características ou segmentação implementada.

## 08. Normalização e divisão interna

**Página 2 · Workflow and ML Model Analysis**

**Trecho grifado:**

> The 640 labeled microphotographs were loaded and normalized to ensure pixel values were within a range of 0–255.

**Comentário:**

RQ1/RQ3 — O artigo chama de normalização a manutenção dos pixels no intervalo 0–255. Não informa fórmula, padronização de cor, tamanho de entrada ou representação usada nos classificadores. Não substituir por 0–1 nem presumir transferência de aprendizado.

## 09. Treino e validação

**Página 2 · Workflow and ML Model Analysis**

**Trecho grifado:**

> Subsequently, the data were split into 80% for training and 20% for validation.

**Comentário:**

RQ3/RQ7 — Holdout interno 80%/20% das 640 imagens: 512/128 por cálculo. Matrizes mostram 128 imagens avaliadas (55 saudáveis e 73 hanseníase). Não se informa divisão por paciente/lâmina, estratificação, semente ou validação cruzada. Múltiplas imagens por lâmina tornam relevante a possibilidade de dependência entre conjuntos, sem comprovar vazamento. Não há conjunto externo; legendas usam test para o conjunto avaliado, sem descrever terceiro subconjunto.

## 10. Cinco modelos

**Página 2 · Workflow and ML Model Analysis**

**Trecho grifado:**

> Five different ML models were then trained: ANNs, decision trees (DT), support vector machines (SVM), logistic regression (LR), and random forests (RF).

**Comentário:**

RQ6 — Rede neural artificial (ANN), árvore de decisão, SVM, regressão logística e random forest. Não há arquitetura/camadas da ANN nem hiperparâmetros suficientes dos modelos. Não classificar automaticamente a ANN como CNN ou deep learning; tampouco atribuir uma rede pré-treinada não informada.

## 11. Matriz de confusão da ANN

**Página 4 · Figura 2 — legenda**

**Trecho grifado:**

> The model correctly classified 36/55 healthy images and 54/73 leprosy images.

**Comentário:**

RQ3/RQ4 — ANN: TN=36, FP=19, FN=19, TP=54; total 128 imagens. Acurácia=(36+54)/128=70,31%; sensibilidade=54/73=73,97%; especificidade=36/55=65,45% (cálculos a partir da figura). Artigo arredonda para 70%, 74% e 65%. Estes denominadores são imagens de avaliação, não novos pacientes.

## 12. Artificial neural networks — métricas

**Página 4 · Tabela 3**

**Trecho grifado:**

> Artificial neural networks 0.70 0.74 0.65

**Comentário:**

RQ3/RQ4/RQ6 — Tabela 3, Artificial neural networks: acurácia, sensibilidade e especificidade, respectivamente: 0.70 0.74 0.65. Escala 0–1; validação interna. Maior acurácia e sensibilidade entre os modelos; AUC 0,71. Não há intervalos de confiança ou teste de diferença estatística.

## 13. Decision trees — métricas

**Página 4 · Tabela 3**

**Trecho grifado:**

> Decision trees 0.67 0.59 0.78

**Comentário:**

RQ3/RQ4/RQ6 — Tabela 3, Decision trees: acurácia, sensibilidade e especificidade, respectivamente: 0.67 0.59 0.78. Escala 0–1; validação interna.

## 14. Support vector machines — métricas

**Página 4 · Tabela 3**

**Trecho grifado:**

> Support vector machines 0.61 0.47 0.8

**Comentário:**

RQ3/RQ4/RQ6 — Tabela 3, Support vector machines: acurácia, sensibilidade e especificidade, respectivamente: 0.61 0.47 0.8. Escala 0–1; validação interna. Divergência: Figura 3G/legenda indica 0,62/0,48/0,80 e contagens TN=44, FP=11, FN=38, TP=35. Preservar os dois relatos; não corrigir a tabela silenciosamente.

## 15. Logistic regression — métricas

**Página 4 · Tabela 3**

**Trecho grifado:**

> Logistic regression 0.65 0.55 0.78

**Comentário:**

RQ3/RQ4/RQ6 — Tabela 3, Logistic regression: acurácia, sensibilidade e especificidade, respectivamente: 0.65 0.55 0.78. Escala 0–1; validação interna.

## 16. Random forests — métricas

**Página 4 · Tabela 3**

**Trecho grifado:**

> Random forests 0.66 0.63 0.71

**Comentário:**

RQ3/RQ4/RQ6 — Tabela 3, Random forests: acurácia, sensibilidade e especificidade, respectivamente: 0.66 0.63 0.71. Escala 0–1; validação interna. Divergência: texto da p. 303 informa acurácia 63%, enquanto Tabela 3 e Figura 3E indicam 66%. Contagens 39+46 acertos em 128 sustentam aproximadamente 66,41%.

## 17. Random Forest: divergência no texto

**Página 3 · Results — Validation of Different ML Models**

**Trecho grifado:**

> DT, LR, and RF—achieved accuracies of 67%, 65%, and 63%

**Comentário:**

RQ4 — Texto atribui 63% de acurácia à RF; Tabela 3 e Figura 3E reportam 66%. A sensibilidade de RF é 63%, o que pode explicar uma troca, mas o artigo não esclarece. Usar 0,66 da tabela com ressalva explícita.

## 18. SVM: divergência na figura

**Página 5 · Figura 3 — legenda G**

**Trecho grifado:**

> The model correctly classified 44/55 healthy images and 35/73 leprosy images. The model Acc is 0.62, Sen is 0.48, and Spec is 0.80.

**Comentário:**

RQ4 — SVM na Figura 3G: TN=44, FP=11, FN=38, TP=35. Calculados: acurácia 79/128=61,72%, sensibilidade 35/73=47,95%, especificidade 44/55=80%. Arredondam para 0,62/0,48/0,80; Tabela 3 e texto usam 0,61/0,47/0,80. Não misturar fontes sem indicar a divergência.

## 19. AUC e interpretação

**Página 4 · Performance of ANN Model via ROC and Loss Curves**

**Trecho grifado:**

> The area under the curve (AUC) is 0.71, suggesting moderate performance in correctly classifying images.

**Comentário:**

RQ4 — ROC-AUC da ANN = 0,71. O texto seguinte a interpreta como probabilidade de classificar corretamente uma microfotografia; essa equivalência não é adequada: AUC resume discriminação entre classes ao variar limiares, não acurácia ou probabilidade individual de diagnóstico. Não há IC ou AUC dos demais modelos reportados.

## 20. Curva de perda

**Página 4 · Performance of ANN Model via ROC and Loss Curves**

**Trecho grifado:**

> From approximately the 10th iteration, the curve stabilizes, approaching a very low value.

**Comentário:**

RQ3/RQ7 — Curva de perda estabiliza aproximadamente na 10ª iteração; Figura 4B mostra perda de treinamento. Convergência de treino não demonstra ausência de overfitting ou generalização externa. Não são apresentadas curvas pareadas de perda de validação ou detalhes suficientes de otimização.

## 21. Comparação indireta com patologistas

**Página 6 · Discussion**

**Trecho grifado:**

> the sensitivity of histopathological detection by expert pathologists for this clinical form is 69%

**Comentário:**

RQ3/RQ5 — Discussão compara referência bibliográfica de sensibilidade de patologistas para hanseníase indeterminada com desempenho global dos modelos. Não houve comparação direta humano versus IA no mesmo conjunto, nem sensibilidade da ANN estratificada por forma indeterminada. Não concluir superioridade clínica a partir desta comparação indireta.

## 22. Diversidade e generalização

**Página 6 · Discussion — limitações**

**Trecho grifado:**

> The main limitation of this study is the need for more extensive training of ANN models using a wider variety of microphotographs from patients with leprosy and healthy

**Comentário:**

RQ2/RQ5/RQ7 — Autores reconhecem necessidade de mais diversidade e inclusão de diagnósticos diferenciais. Não há validação externa, entre instituições/equipamentos, nem desempenho estratificado por tons de pele, grupos demográficos, ampliação ou subtipo. H\&E não informa automaticamente tom de pele clínico. Generalização para outras dermatoses permanece não avaliada.

## 23. Acesso aos dados

**Página 1 · Declaração de disponibilidade de dados**

**Trecho grifado:**

> The raw data supporting the conclusions of this article will be made available by the authors, without undue reservation, to any qualified researcher.

**Comentário:**

RQ2 — Dados disponíveis mediante solicitação aos autores segundo declaração do artigo. Não há repositório público nomeado/linkado ou identificador de dataset no PDF. Não classificar como base pública aberta para download.
