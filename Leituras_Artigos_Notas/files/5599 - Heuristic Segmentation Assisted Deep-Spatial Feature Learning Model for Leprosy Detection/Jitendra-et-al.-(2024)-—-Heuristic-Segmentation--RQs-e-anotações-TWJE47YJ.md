---
tags: []
parent: 'Heuristic Segmentation Assisted Deep-Spatial Feature Learning Model for Leprosy Detection'
collections:
    - TCC_Leituras
$version: 311
$libraryID: 2
$itemKey: TWJE47YJ

---
# Jitendra et al. (2024) — Heuristic Segmentation: RQs e anotações

**Título:** *Heuristic Segmentation Assisted Deep-Spatial Feature Learning Model for Leprosy Detection*.\
**Autores:** R Jitendra; Jay B Simha; Shinu Abhi; Vineet K Chadha.\
**Veículo:** *SN Computer Science*, 2024, volume 5, artigo 737.\
**DOI:** 10.1007/s42979-024-03053-3.\
**Fonte:** PDF fornecido, 17 páginas; os números abaixo são posições no PDF.

Estudo original experimental computacional de classificação binária de imagens de pele como **hanseníase ou normal**, com segmentação de ROI e extração de atributos híbridos. Não é validação clínica prospectiva. As RQs abaixo são as oito perguntas do TCC, distintas das perguntas internas do próprio artigo.

A cópia PDF contém **22 grifos com comentários**. O original do Zotero foi preservado; as anotações foram incorporadas à cópia PDF, sem alteração direta do banco de dados do Zotero. Os trechos e comentários aparecem ao final. As inconsistências do artigo são preservadas e identificadas, sem substituir os resultados publicados por valores recalculados.

## RQ1. Quais técnicas de visão computacional são utilizadas para identificar manifestações dermatológicas associadas à hanseníase?

O pipeline combina **pré-processamento, segmentação FFCM, atributos GLCM e atributos profundos AlexNet**, seguidos de classificação por Random Forest (p. 5–13).

*   **Pré-processamento:** conversão RGB para cinza, equalização de histograma (chamada adaptativa na p. 5), filtro mediano 2D e normalização Z-score (p. 13; grifo 5).
*   **Segmentação:** Fuzzy C-Means com otimização dos centroides pelo algoritmo Firefly, denominado FFCM. São descritos dois clusters, fundo e lesão, fuzzificação 2 e objetivo Rosenbrock. Não exige definição manual de pontos iniciais segundo os autores (grifos 7–9).
*   **Recuperação da ROI em cor:** multiplicação da máscara binária pelos pixels RGB correspondentes; exemplos nas Tabelas 2–3 (p. 8; grifo 10).
*   **Atributos GLCM/descritivos:** contraste, energia, entropia, homogeneidade, correlação, variância, média e desvio-padrão, concatenados conforme Eq. 22. Algumas passagens resumem apenas cinco atributos; distâncias, direções, quantização e dimensão total não são integralmente especificadas (p. 9–10; grifo 11).
*   **AlexNet:** vetor de 4096 atributos de camada totalmente conectada, concatenado ao vetor GLCM. A metodologia identifica FC6; os resultados identificam FC7 (grifos 12–13).

Há divergência de dimensões: **150×70** na preparação/entrada da rede versus **256×300** para a ROI antes da extração na p. 13. Não é explicado claramente se há uma etapa adicional de redimensionamento. O artigo também fornece configurações conflitantes do Firefly: população **25** e beta **1** na p. 8, versus população **2** e atração base **2** na p. 13.

## RQ2. Quais conjuntos de dados e populações são utilizados no desenvolvimento e na avaliação desses modelos?

Os autores reuniram imagens de **fontes primárias**, incluindo hospitais, e **secundárias**, como sites e bases online. Citam **220 imagens**, mas a seção de aquisição afirma que o processamento para anotações deu origem a **450 imagens de hanseníase**. Outras seções retomam 220. Não há explicação suficiente para relacionar essas contagens, nem para concluir que a diferença decorre de recortes, aumento de dados ou novas coletas (p. 5, 10, 12–13; grifos 2–3).

Também são usados controles de pele normal, mas faltam contagem da classe negativa, total final reconciliado e distribuição por subconjunto. Por isso, não calcular tamanhos definitivos de treino e validação a partir de 220 ou 450.

O texto descreve diversidade de locais anatômicos — mãos, palmas, membros, coxas, face, nariz e costas — e de cores de pele, formas, dimensões e orientações das lesões. Não informa número de pacientes únicos, distribuição de idade/sexo, escala ou contagem de tons de pele, procedência individual, proporções por fonte, critérios de confirmação diagnóstica ou detalhamento dos anotadores. As instituições de apoio são indianas, mas isso não determina a origem de todas as imagens de uma base mista (grifo 4).

Não há dataset público nomeado de forma inequívoca, URLs completos das fontes ou repositório. A declaração informa **disponibilidade mediante solicitação razoável ao autor correspondente** (p. 16; grifo 21).

## RQ3. Quais métodos, procedimentos são utilizados para avaliar o desempenho desses modelos e quais resultados são reportados?

O artigo declara **80% das amostras para treinamento e 20% para “inner cross-validation”**. Não fornece número de folds, repetições, semente, separação por paciente/fonte ou detalhes de validação aninhada. Portanto, registrar uma divisão interna 80/20, sem classificá-la como k-fold ou nested cross-validation confirmada. O conjunto final e seus denominadores permanecem ambíguos (p. 12; grifo 15).

A Tabela 6 compara **GLCM + Random Forest** com **GLCM + AlexNet + Random Forest**, usando pré-processamento e classificador comuns declarados. O híbrido apresenta acurácia de **96,6%**, versus **92,7%** do GLCM: diferença de **3,9 pontos percentuais**. Não há linha interna de AlexNet isolado, FCM sem Firefly ou modelo sem segmentação. Assim, essa comparação não isola o benefício de cada componente (p. 14; grifos 16–19).

A Tabela 4 descreve Adam, taxa de aprendizado **0,0001**, **200 épocas**, dropout **50%**, entrada com normalização zero-center, pooling 3×3 e stride 4. A p. 13 também menciona **100 iterações**, sem esclarecer sua relação com as épocas. Número de camadas e camada de extração variam entre passagens. Não há identificação inequívoca do checkpoint/base de pré-treinamento, camadas congeladas ou protocolo completo de ajuste.

Não são apresentados intervalos de confiança, testes de significância, contagens da matriz de confusão ou procedimento que explique as médias da Tabela 6. A segmentação é ilustrada nas Tabelas 2–3, mas não avaliada por Dice, IoU ou comparação quantitativa com máscaras de referência. O artigo não oferece benchmark de latência ou validação clínica que sustente a alegação de uso em tempo real (grifos 10 e 22).

## RQ4. Quais métricas são utilizadas para avaliar o desempenho desses modelos e quais resultados são reportados?

**Tabela 6, p. 14 — resultados internos reportados como médias:**

| Configuração, classificador Random Forest | Acurácia | Precisão | Recall | F-score reportado |
| ----------------------------------------- | -------- | -------- | ------ | ----------------- |
| GLCM                                      | 92,7%    | 89,5%    | 92,1%  | 0,9402            |
| GLCM + AlexNet                            | 96,6%    | 99,7%    | 95,8%  | 0,9771            |


A Tabela 5 define acurácia, precisão, recall e F-score em função de TP, TN, FP e FN, mas não fornece essas contagens. F-score é definido como a média harmônica de precisão e recall.

**Ressalvas de consistência:**

1.  Para GLCM, aplicar a fórmula publicada a **P=0,895 e R=0,921** resulta em **F1≈0,9078**, diferente de **0,9402**. Embora a tabela use “average”, o método de agregação não é explicado e os valores não são reconciliáveis com a informação fornecida. Manter 0,9402 como valor reportado, acompanhado da ressalva (grifo 16).
2.  Para o híbrido, P=0,997 e R=0,958 resultam em F1≈0,9771, coerente com o valor publicado. Isso não valida os demais resultados ou o protocolo.
3.  A introdução (p. 3) informa **sensibilidade 95,7%** e **especificidade 95,9%**, enquanto a tabela informa recall **95,8%** e não apresenta especificidade. Em uma mesma matriz binária, a acurácia é uma média ponderada de sensibilidade e especificidade: **96,6% não fica entre 95,7% e 95,9%**. A agregação não está descrita; não reconstruir uma matriz ou escolher silenciosamente um relato (grifo 18).

Não há AUC, desempenho por tom de pele, Dice/IoU ou intervalos de confiança. Os valores da Tabela 7 — por exemplo, GLCM **88,51%**, GAN + DenseNet-121 **94,25%**, CNN **91%** e CNN + Inception-v3 **93%** — vêm de comparações com literatura, não devem substituir o baseline interno de 92,7%.

A comparação com Lo et al. exige cautela adicional: a própria p. 3 relata acurácia 95,3%/sensibilidade 93,5% com cor e 73,8%/70,7% sem cor; a Tabela 7 combina **73,8% e 93,5%**. Além disso, a tarefa desse estudo citado é detecção de bacilos em blocos histopatológicos, diferente da classificação de fotografias de lesões (grifo 20).

## RQ5. Como o desempenho dos modelos varia entre diferentes grupos ou tons de pele?

**Não avaliado quantitativamente.** O artigo declara imagens de pacientes com diferentes cores de pele e diversidade anatômica/morfológica, mas não fornece distribuição por escala de tons, etnia, sexo, idade ou região, nem métricas estratificadas (p. 5 e 13; grifo 4).

Não há comparação de desempenho entre tons claros/escuros, subtipos de hanseníase ou locais anatômicos. Diversidade declarada de imagens não comprova equidade nem robustez entre grupos. As métricas globais não permitem concluir que o desempenho seja equivalente.

## RQ6. Quais modelos e abordagens de inteligência artificial são utilizados para identificar manifestações dermatológicas associadas à hanseníase?

A abordagem proposta é **híbrida**: segmentação por **FFCM (Firefly + Fuzzy C-Means)**, extração de atributos **GLCM/descritivos e AlexNet**, concatenação e classificação final por **Random Forest** em duas classes: **1=hanseníase, 0=normal** (p. 5–13).

AlexNet é utilizada como extrator profundo de **4096 atributos**. A metodologia/Eq. 23 e a Tabela 4 apontam **FC6**, mas a descrição experimental da p. 13 aponta **FC7**. O texto alterna descrições de três/cinco camadas convolucionais e duas/três totalmente conectadas; Figura 1 e Tabela 4 indicam cinco convolucionais, mas a reprodução integral não fica resolvida. Não presumir ImageNet ou um checkpoint específico sem identificação explícita suficiente.

Random Forest utiliza bootstrap e votação de árvores. O parâmetro **m=50** aparece no contexto de seleção/split por nó; **não deve ser convertido em “50 árvores”**. Número de árvores, profundidade e demais parâmetros não estão completamente especificados (grifo 14).

Não é uma CNN end-to-end com saída final pela AlexNet: o classificador final declarado é Random Forest. Tampouco há classificação de subtipos ou diagnóstico diferencial multiclasse com outras dermatoses demonstrado.

## RQ7. Como a capacidade de generalização dos modelos é avaliada, especialmente quando são utilizados conjuntos de dados diferentes daqueles empregados no treinamento?

A evidência se limita à **avaliação interna 80/20** descrita. Não há teste em dataset externo reservado, instituição independente, outro país, dispositivo distinto ou estudo prospectivo de campo (grifo 15).

Reunir imagens de hospitais e internet não equivale a validação externa: não se demonstra que uma fonte tenha sido reservada exclusivamente para teste. Não são esclarecidas separação por paciente, origem, duplicatas ou imagens derivadas. Isso impede afastar dependência entre conjuntos; não demonstra, por si só, que vazamento ocorreu.

A Tabela 7 é comparação com métricas de estudos anteriores, sem reimplementação comum documentada e envolvendo tarefas/modalidades diferentes. **Comparação de números publicados não testa o modelo proposto em outra base** (grifo 20).

Alegações de robustez, diagnóstico sem contato e tempo real excedem a evidência de validação apresentada. Não há medidas de desempenho externo, equidade por grupo ou tempo de execução que sustentem implantação clínica a partir deste artigo (grifo 22).

## RQ8. O artigo foi publicado em que tipo de veículo de publicação? (revista, conferência)

**Revista científica.** Artigo **Original Research** em *SN Computer Science*, **2024, volume 5, artigo 737**, Springer Nature. DOI **10.1007/s42979-024-03053-3**. Recebido em 18 de maio de 2024 e aceito em 13 de junho de 2024. O PDF tem 17 páginas; 737 é identificador do artigo, não página inicial (p. 1; grifo 1).

## Cuidados para a extração

Preservar as divergências **220/450 imagens; 150×70/256×300; FC6/FC7; população Firefly 25/2; F-score GLCM e sensibilidade/especificidade**. Distinguir ganho interno dos atributos híbridos de alegações não isoladas sobre segmentação, generalização e uso clínico. Não confundir este artigo com outro trabalho dos autores cujo título começa por *Deep Semantic Segmentation Assisted...*.

# Trechos e notas para o Zotero

Cada número corresponde a uma anotação no PDF. Os trechos textuais abaixo são literais, com quebras de linha/hifenização de fim de linha normalizadas. Nas tabelas, os valores são transcritos na ordem das colunas; suas escalas são explicadas em cada nota. Os comentários podem ser copiados diretamente para o Zotero.

## 01. Veículo e desenho

**Página 1 · Cabeçalho**

**Trecho grifado:**

> https\://doi.org/10.1007/s42979-024-03053-3

**Comentário:**

RQ8 — Artigo original de pesquisa em revista: SN Computer Science (2024), volume 5, artigo 737. DOI 10.1007/s42979-024-03053-3. Experimento computacional de classificação binária, não ensaio clínico. PDF com 17 páginas; 737 é número do artigo.

## 02. Fontes e 220 imagens

**Página 5 · Data Acquisition and Pre-processing**

**Trecho grifado:**

> In this work, a set of 220 images were collected from the different primary as well as secondary sources including hospital visits, online leprosy classification datasets etc.

**Comentário:**

RQ2 — Mistura de fontes primárias (visitas a hospitais) e secundárias (bases/sites online), com 220 imagens declaradas. Não há identificação completa das bases, pacientes únicos, proporção por fonte ou contagem da classe normal. A disponibilidade é mediante solicitação, não repositório público identificado.

## 03. Divergência: 450 imagens

**Página 5 · Data Acquisition and Pre-processing**

**Trecho grifado:**

> The input images were later processed for annotations, thus giving rise to a sufficiently large 450 images representing the leprosy image samples.

**Comentário:**

RQ2/RQ3 — Após mencionar 220 imagens, o texto informa 450 imagens de hanseníase após processamento para anotações. Não explica como a anotação altera a contagem, nem quantos controles normais compõem o total. Não assumir aumento de dados, recortes ou número de pacientes. Outras seções voltam a citar 220; denominador final e contagens por split permanecem ambíguos.

## 04. Diversidade sem estratificação

**Página 5 · Data Acquisition and Pre-processing**

**Trecho grifado:**

> the data were selected from the patients of different skin colors, skin and lesion gradients

**Comentário:**

RQ2/RQ5 — Diversidade de cores de pele e locais anatômicos é alegada, mas não há escala de tons, distribuição por grupo ou métricas estratificadas. Não há idade, sexo, número de pacientes, distribuição por país ou confirmação diagnóstica sistemática suficientemente descritos. Afiliações indianas não definem a procedência de toda a base mista.

## 05. Pré-processamento

**Página 13 · Results and Discussion**

**Trecho grifado:**

> histogram equalization and two-dimensional median filtering. In addition, we performed Z-score normalization over the filtered input images

**Comentário:**

RQ1/RQ3 — Conversão RGB para tons de cinza, equalização de histograma, filtro mediano 2D e normalização Z-score. Página 5 chama a equalização de adaptativa. Não se esclarece se os parâmetros de normalização foram ajustados somente no treino; normalização não garante ausência de overfitting.

## 06. Dimensões de entrada

**Página 5 · Data Acquisition and Pre-processing**

**Trecho grifado:**

> We resized overall input images in the dimension of 150 × 70.

**Comentário:**

RQ1/RQ3 — 150×70 na aquisição e na entrada da AlexNet/Tabela 4. Página 13 informa ROI redimensionada para 256×300 antes da extração; não esclarece a passagem entre dimensões. Preservar ambas as descrições, sem inventar etapas para reconciliá-las.

## 07. Segmentação proposta

**Página 5 · Heuristic FFCM Driven ROI Segmentation**

**Trecho grifado:**

> Firefly driven Fuzzy C-Means (FFCM) clustering method to perform automatic ROI segmentation.

**Comentário:**

RQ1/RQ6 — Fuzzy C-Means com otimização de centroides por Firefly para segmentar ROI. Página 13: dois clusters (fundo e lesão), fuzzificação 2, máximo de 100 iterações, objetivo Rosenbrock. Não há avaliação quantitativa de segmentação com Dice/IoU ou comparação contra máscaras de referência; exemplos visuais não demonstram por si só acurácia de segmentação.

## 08. Firefly: população 25

**Página 8 · Firefly Algorithm Based FCM Centroid Optimization**

**Trecho grifado:**

> To implement Firefly, we assigned number of populations as 25 (n=25), while the number of iterations (say, stopping criteria) was fixed at 100.

**Comentário:**

RQ1/RQ3 — Aqui são declarados 25 fireflies, 100 iterações, beta=1 e g=1. Na página 13 são declarados população 2 e coeficiente de atração base 2. Divergência que limita reprodução; não escolher silenciosamente uma configuração.

## 09. Firefly: população 2

**Página 13 · Results and Discussion**

**Trecho grifado:**

> the total number of Fireflies (say, population) was fixed as 2, while light absorption coefficient and attraction coefficient base values were defined as 1 and 2, respectively.

**Comentário:**

RQ1/RQ3 — Configuração dos resultados: população 2, absorção 1, atração base 2, limites −10/10, mutação 0,2, damping 0,98 e faixa de mutação 1. Método da página 8 informa população 25 e beta=1. Registrar inconsistência de implementação.

## 10. Máscara e ROI RGB

**Página 8 · Segmentação e recuperação da cor**

**Trecho grifado:**

> we multiplied segmented binary image (i.e., lesion ROI) with corresponding RGB channel pixels

**Comentário:**

RQ1 — Máscara binária multiplicada pelos canais RGB para recuperar a ROI em cor, seguida de extração GLCM e AlexNet. Tabelas 2–3 mostram exemplos de máscaras/ROIs. Não há contagens de máscaras de referência, Dice, IoU ou análise de erro de segmentação.

## 11. Atributos texturais

**Página 10 · GLCM Based Statistical Feature Extraction**

**Trecho grifado:**

> Contrast, Energy, Entropy, Homogenity, Correlation, Variance, Mean and Standard Deviation

**Comentário:**

RQ1/RQ6 — Conjunto GLCM/descritivo inclui contraste, energia, entropia, homogeneidade, correlação, variância, média e desvio-padrão (Eq. 22). Outros trechos resumem somente cinco atributos. Não estão integralmente definidos níveis de cinza, distâncias, direções e dimensionamento final da representação.

## 12. FC6 na metodologia

**Página 12 · FC Layers**

**Trecho grifado:**

> we considered FC6 feature vector as the final deep model’s feature (vector) to perform further learning and classification.

**Comentário:**

RQ1/RQ6 — Metodologia/Eq. 23 usa FC6 de AlexNet, com 4096 atributos, concatenado ao vetor GLCM. Resultados da página 13 dizem FC7. Não assumir equivalência da camada extraída. O texto também alterna números de camadas; Figura 1/Tabela 4 favorecem cinco convolucionais, mas não resolvem todos os detalhes.

## 13. FC7 nos resultados

**Página 13 · Results and Discussion**

**Trecho grifado:**

> Here, we obtained 4096-dimensional feature at FC7.

**Comentário:**

RQ3/RQ6 — Resultados declaram FC7, diferindo da FC6 na metodologia/Eq. 23 e Tabela 4. ADAM, 200 épocas e 100 iterações são mencionados, sem relação clara entre esses dois últimos valores. Pré-treinamento é descrito genericamente como transfer learning, sem identificação inequívoca de checkpoint/base prévia ou protocolo de congelamento.

## 14. Parâmetro m do Random Forest

**Página 12 · Random Forest Classifier**

**Trecho grifado:**

> In the deployed tree-structure, every tree retrieves distinct vote (1-Leprosy, 0-Normal)

**Comentário:**

RQ6 — Random Forest é o classificador final, com votação 1=hanseníase e 0=normal, treinado com amostras bootstrap. m=50 é descrito no contexto de split/variáveis por nó; não o reclassificar como 50 árvores. Número de árvores, profundidade e outros hiperparâmetros não ficam suficientemente especificados.

## 15. Divisão interna 80/20

**Página 12 · Random Forest Classifier**

**Trecho grifado:**

> we considered 80% of the samples for the training, while remaining 20% were used for inner cross-validation

**Comentário:**

RQ3/RQ7 — Partição interna 80% treino e 20% denominada inner cross-validation. Não informa k folds, repetições, semente ou divisão por paciente/fonte. Descrever como divisão interna relatada, não como k-fold/nested CV confirmada. Sem total reconciliado e sem contagens por classe, não calcular tamanho definitivo dos splits. Ausência de detalhamento impede excluir dependência entre imagens, mas não prova vazamento.

## 16. GLCM: métricas reportadas

**Página 14 · Intra-Model Assessment**

**Trecho grifado:**

> accuracy of 92.7%, precision of 89.5%, recall of 92.1% and F-score of 0.9402.

**Comentário:**

RQ3/RQ4 — GLCM + Random Forest: acurácia 92,7%, precisão 89,5%, recall 92,1%, F-score 0,9402, conforme Tabela 6/texto. Pela fórmula da Tabela 5 aplicada a P=0,895 e R=0,921, F1≈0,9078, não 0,9402. A tabela diz average, mas não explica agregação; faltam dados para reconciliar. Preservar valor reportado com ressalva, sem corrigi-lo silenciosamente.

## 17. Híbrido: métricas reportadas

**Página 14 · Intra-Model Assessment**

**Trecho grifado:**

> accuracy 96.6%, precision 99.7%, recall of 95.8% and F-score of 0.9771.

**Comentário:**

RQ3/RQ4 — GLCM+AlexNet+Random Forest: acurácia 96,6%, precisão 99,7%, recall 95,8%, F1 0,9771. Ganho de acurácia contra GLCM interno: 3,9 pontos percentuais. Não há IC, teste de significância, contagens TP/TN/FP/FN ou descrição das repetições por trás de average. Não confundir com GLCM 88,51% da literatura.

## 18. Sensibilidade e especificidade no texto

**Página 3 · Introduction — síntese dos resultados**

**Trecho grifado:**

> classification accuracy of 96.6%, while maintaining average sensitivity and specificity of 95.7% and 95.9%, respectively.

**Comentário:**

RQ4 — Introdução informa sensibilidade 95,7% e especificidade 95,9%; Tabela 6 usa recall 95,8% e não tabula especificidade. Para uma mesma matriz binária, acurácia deve ficar entre sensibilidade e especificidade; 96,6% não se reconcilia com esse par. Como a agregação das médias não é descrita, registrar divergência sem reconstruir matriz de confusão.

## 19. Controle interno da comparação

**Página 14 · Intra-Model Assessment**

**Trecho grifado:**

> the classifier employed was the Random Forest algorithm, applied as common classifier with both features.

**Comentário:**

RQ3/RQ6 — Comparação interna: GLCM versus híbrido GLCM+AlexNet, com mesmo classificador e pré-processamento declarado. Não há linha interna de AlexNet isolado ou comparação FCM sem Firefly/sem segmentação. Assim, não isola quantitativamente o ganho de cada componente, apesar das alegações de superioridade.

## 20. Comparação com literatura

**Página 14 · Inter-Model Assessment**

**Trecho grifado:**

> The relative performance of the different approaches is given in Table 7.

**Comentário:**

RQ3/RQ7 — Tabela 7 compara resultados de trabalhos prévios; não documenta reimplementação e teste comum em base independente. Mistura modalidades/tarefas, incluindo blocos histopatológicos de bacilos de Lo et al. Não é validação externa do modelo proposto. A linha Lo combina acurácia 73,8% e recall 93,5%, enquanto a própria revisão na p. 3 associa 73,8% a sensibilidade 70,7%; a comparação requer cautela.

## 21. Acesso aos dados

**Página 16 · Data Availability**

**Trecho grifado:**

> The dataset generated and analyzed during the current study are available from the corresponding author on reasonable request.

**Comentário:**

RQ2 — Disponibilidade mediante solicitação ao autor correspondente. Não há repositório público identificado nem lista completa das fontes. O procedimento de rotulagem/confirmação diagnóstica e o vínculo entre imagens de um mesmo paciente não são suficientemente descritos.

## 22. Alegação de uso em tempo real

**Página 1 · Resumo — conclusão**

**Trecho grifado:**

> automated and touchless real-time leprosy diagnosis.

**Comentário:**

RQ3/RQ7 — Aplicação automática, sem contato e em tempo real é alegada; não há benchmark de latência, avaliação prospectiva, comparação entre dispositivos ou validação externa demonstrada. Métricas internas não comprovam prontidão clínica. Não há resultados por tons de pele, região ou subtipo de hanseníase.
