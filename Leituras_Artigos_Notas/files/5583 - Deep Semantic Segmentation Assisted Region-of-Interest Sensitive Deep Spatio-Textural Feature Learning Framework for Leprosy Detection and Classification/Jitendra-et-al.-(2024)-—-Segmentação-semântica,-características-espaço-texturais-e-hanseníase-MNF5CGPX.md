---
tags: []
parent: 'Deep Semantic Segmentation Assisted Region-of-Interest Sensitive Deep Spatio-Textural Feature Learning Framework for Leprosy Detection and Classification'
collections:
    - TCC_Leituras
$version: 286
$libraryID: 2
$itemKey: MNF5CGPX

---
# Jitendra et al. (2024) — Segmentação semântica, características espaço-texturais e hanseníase

**Artigo:** R. Jitendra; Jay B. Simha; Shinu Abhi; Vineet K. Chadha. *Deep Semantic Segmentation Assisted Region-of-Interest Sensitive Deep Spatio-Textural Feature Learning Framework for Leprosy Detection and Classification*. SN Computer Science, volume 5, artigo 742, 2024. **DOI:** 10.1007/s42979-024-03054-2.

**Fonte:** PDF fornecido, 16 páginas, com numeração impressa correspondente à posição no arquivo. Esta análise se limita ao artigo; não inclui auditoria do código ou solicitação dos dados aos autores. As oito perguntas abaixo são as RQs fornecidas pelo usuário. As “RQ1–RQ4” citadas pelos autores nas páginas 13–14 pertencem à organização interna do artigo e não devem ser confundidas com estas perguntas.

**Tipo de estudo:** pesquisa experimental computacional, com proposta de pipeline de visão computacional e comparação de classificadores. **Tarefa final:** classificação binária de imagem como hanseníase versus normal. Segmentação de ROI é etapa intermediária; não há classificação de gravidade, PB/MB ou diagnóstico diferencial multiclasse demonstrado.

## RQ1 — Quais técnicas de visão computacional são utilizadas para identificar manifestações dermatológicas associadas à hanseníase?

**Resposta:** pipeline de pré-processamento, segmentação semântica, extração de características híbridas, fusão e classificação:

1.  **Pré-processamento:** equalização de histograma/intensidade, ajuste adaptativo de contraste e normalização z-score. Redimensionamento inicial para **400 × 496 pixels** e conversão para cinza com **RGB2GRAY**.
2.  **Segmentação:** **U-Net** distingue ROI e fundo. O artigo descreve convoluções, pooling/up-convolutions, conexões entre caminhos e perda com ponderação de pixels/bordas. A máscara é combinada com a imagem original para recuperar a ROI em RGB. Há variação terminológica entre “multiplication” e “convolution”; não é fornecida implementação suficiente para resolver todos os detalhes.
3.  **Textura:** **GLCM** para características estatísticas/espaço-texturais da ROI.
4.  **Características profundas:** **ResNet101**, com entrada **224 × 224 × 3** e normalização pela equação `x/127,5 − 1`, que mapeia \[0,255] para \[−1,1] caso essa seja a faixa de entrada.
5.  **Fusão:** concatenação horizontal dos vetores GLCM e ResNet101, seguida de Random Forest.

Na página 12, a lista de oito características é **contraste, energia, homogeneidade, correlação, média, desvio-padrão, curtose e assimetria**. A conclusão, página 15, fala em **sete** e lista entropia, energia, homogeneidade, correlação, média, desvio-padrão e variância. Essas especificações divergem; não combinar as listas como se fossem uma única descrição comprovada.

**Aumento:** o artigo menciona aumento/re-amostragem com diferentes orientações e campos de visão, mas não fornece todas as transformações, parâmetros ou contagens por operação. Não atribuir Fuzzy C-Means/Firefly a este artigo: a segmentação proposta aqui é U-Net.

**Limites:** exemplos visuais de máscaras são apresentados nas Tabelas 2–3, mas não localizei Dice/IoU nem avaliação quantitativa isolada da segmentação. Não há técnica de explicabilidade validada identificada.

**Evidências:** páginas 4–10 e 12, Proposed System e Results and Discussion; anotações 05–13 e 18.

## RQ2 — Quais conjuntos de dados e populações são utilizados no desenvolvimento e na avaliação desses modelos?

**Resposta:** coleção própria, sem nome público específico, formada por imagens obtidas com câmera convencional em hospitais/instituições ligadas à hanseníase e imagens de repositórios online. O artigo não identifica suficientemente todas as instituições, repositórios, datas ou contribuições de cada fonte.

| Elemento                          | Informação disponível                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Amostra inicial                   | **220 imagens** referentes a casos de hanseníase                                                                   |
| Após aumento/re-amostragem        | **450 imagens relacionadas à hanseníase**, conforme redação da página 4                                            |
| Classe normal                     | Incluída, mas **quantidade não informada claramente**                                                              |
| Número de pacientes/lesões únicas | Não localizado                                                                                                     |
| População                         | Homens e mulheres, sem contagens; seleção alegada de diferentes cores de pele                                      |
| Regiões corporais                 | Coxa, dedos, nariz/lateral do nariz, face, membros, palmas, costas, entre outras                                   |
| País da coorte                    | Não suficientemente especificado para toda a coleção; afiliações indianas não definem a origem de todas as imagens |
| Referência da segmentação         | Imagens e mapas correspondentes; produção/validação das máscaras não detalhada                                     |
| Acesso                            | Mediante solicitação razoável ao autor correspondente                                                              |


**Não registrar 220 ou 450 como pacientes.** Também não apresentar 450 como tamanho final inequívoco das duas classes: a redação relata 450 imagens relacionadas à hanseníase e depois a inclusão de normais, sem número destas. Imagens aumentadas não são observações clínicas independentes.

Não localizei distribuição etária, contagens por sexo/tom, número de lesões por paciente, confirmação diagnóstica individual detalhada, concordância dos anotadores ou protocolo de deduplicação. Não foi localizado link público para baixar a coleção final. A disponibilidade por solicitação está na página 15.

**Evidências:** páginas 4, 7 e 15; anotações 02–05, 09 e 20.

## RQ3 — Quais métodos, procedimentos são utilizados para avaliar o desempenho desses modelos e quais resultados são reportados?

**Resposta:** comparação interna de duas representações (**GLCM** e **GLCM + ResNet101**) com seis classificadores (**NB, k-NN, SVM, DT, ANN e RF**), totalizando 12 configurações na Tabela 5. A Tabela 6 compara valores atribuídos a trabalhos anteriores, sem demonstração de reavaliação uniforme em um mesmo protocolo.

**Divisão:** a página 11 declara **70% para treino e 30% como “out-of-bag data for further cross-validation”**. Essa descrição não esclarece se houve holdout convencional, estimativa OOB por bootstrap das árvores ou outro esquema. Não há número de folds; portanto, **não registrar como k-fold confirmado**. Tampouco há contagens exatas dos subconjuntos ou divisão por paciente/fonte.

**Treinamento U-Net:** Adam, learning rate inicial **0,0001**, **200 épocas**, batch size **8**, softmax por pixel e perda de entropia cruzada com pesos. Os detalhes completos de treinamento/validação do ResNet101 e hiperparâmetros dos classificadores não são fornecidos. Para ANN, a página 13 menciona Levenberg–Marquardt.

**Ambiente:** MATLAB 2021b, CPU Intel i5 a 3,2 GHz, 8 GB de RAM. Isso não constitui medição de latência ou demonstração de funcionamento clínico em tempo real.

**Resultados:** maior accuracy interna com híbrido + RF: **97,24%**, precision **99,69%**, recall **95,82%**, F **0,98** nas tabelas. O resumo usa **97,20%** e F **97,80%**. Registrar ambas as apresentações, sem substituição silenciosa. RF somente com GLCM tem accuracy **95,63%**; diferença calculada de **1,61 ponto percentual** a favor da fusão para RF. O ganho não é uniforme: DT cai de 95,52% para 95,45%, e ANN de 95,59% para 95,19%.

**Limitações de validação:** não localizei repetições independentes, sementes, intervalos de confiança ou testes estatísticos. Não fica clara a separação antes do aumento, o agrupamento de variantes da mesma imagem nem a independência das etapas U-Net/ResNet em relação à avaliação final. Essas lacunas **não provam vazamento**, mas impedem verificar sua prevenção. Retirar fundo da imagem não demonstra, por si só, balanceamento entre classes de pacientes/imagens.

**Evidências:** páginas 7, 11–14; anotações 09–10, 14–17, 19 e 21–32.

## RQ4 — Quais métricas são utilizadas para avaliar o desempenho desses modelos e quais resultados são reportados?

**Resposta:** accuracy, precision, recall e F-score/F-measure, definidos a partir de TP/TN/FP/FN na Tabela 4. São métricas da **classificação por imagem**, não qualidade de máscaras. Não localizei contagens brutas da matriz de confusão, AUC, especificidade como resultado separado, Dice/IoU, intervalos de confiança ou resultados por tom de pele.

**Tabela 5 — transcrição fiel dos valores publicados.** Accuracy é percentual. Nas 11 primeiras linhas, precision/recall/F são decimais; na última, precision e recall aparecem como 99,69 e 95,82, em escala percentual, enquanto F permanece 0,98.

| Características  | Classificador | Accuracy (%) | Precision (como publicada) | Recall (como publicado) | F-measure |
| ---------------- | ------------- | ------------ | -------------------------- | ----------------------- | --------- |
| GLCM             | NB            | 93,20        | 0,91                       | 0,98                    | 0,88      |
| GLCM             | k-NN          | 92,51        | 0,91                       | 0,99                    | 0,94      |
| GLCM             | SVM           | 91,96        | 0,73                       | 0,99                    | 0,88      |
| GLCM             | DT            | 95,52        | 0,84                       | 0,88                    | 0,93      |
| GLCM             | ANN           | 95,59        | 0,93                       | 0,98                    | 0,94      |
| GLCM             | RF            | 95,63        | 0,93                       | 0,98                    | 0,95      |
| GLCM + ResNet101 | NB            | 94,57        | 0,91                       | 0,98                    | 0,93      |
| GLCM + ResNet101 | k-NN          | 95,03        | 0,87                       | 0,99                    | 0,93      |
| GLCM + ResNet101 | SVM           | 94,28        | 0,91                       | 0,93                    | 0,92      |
| GLCM + ResNet101 | DT            | 95,45        | 0,93                       | 0,98                    | 0,93      |
| GLCM + ResNet101 | ANN           | 95,19        | 0,91                       | 0,99                    | 0,96      |
| GLCM + ResNet101 | RF            | **97,24**    | **99,69**                  | **95,82**               | **0,98**  |


O negrito identifica a configuração final selecionada, não o máximo de cada coluna. Por exemplo, valores decimais 0,99 de recall correspondem a 99%, maiores que o recall de 95,82% do RF híbrido.

**Divergências e cuidados:**

*   **Resumo vs tabelas:** accuracy 97,20% versus 97,24%; F 97,80% versus 0,98/98%. Não tratar F=0,98 como 0,98%.
*   **F1 versus P/R:** GLCM+NB tem P=0,91, R=0,98 e F=0,88; a média harmônica direta seria aproximadamente 0,944. GLCM+DT tem P=0,84, R=0,88 e F=0,93, acima de ambos; a média harmônica direta seria aproximadamente 0,860. Não são resultados consistentes com a aplicação direta da fórmula da Tabela 4 aos valores mostrados. O artigo não explica agregações ou diferenças de cálculo que permitam reconciliá-los. Preservar os valores publicados com ressalva.
*   **Híbrido+k-NN:** o texto da página 12 cita F=0,938; a tabela mostra 0,93. Não usar precisão adicional sem identificar a fonte.
*   **Comparação externa:** a Tabela 6 reúne resultados de literatura, incluindo imagens de bacilos em lâminas. Não é uma competição controlada entre métodos no mesmo dataset nem teste externo do modelo proposto.

**Evidências:** resumo, Tabelas 4–6, páginas 12–15; anotações 16–17 e 21–32.

## RQ5 — Como o desempenho dos modelos varia entre diferentes grupos ou tons de pele?

**Resposta:** **não é possível quantificar pelo artigo**. Os autores afirmam selecionar imagens de diferentes cores de pele e regiões corporais, mas não fornecem contagens por tom, classificação Fitzpatrick/Monk, métricas por grupo, análise de equidade ou comparação estatística.

A normalização de contraste/cor é uma etapa de processamento; não demonstra que diferenças de desempenho entre tons foram eliminadas. A diversidade de imagens alegada também não comprova representatividade da população. Não inferir tons de pele pelas afiliações, pelo contexto indiano ou pelas ilustrações.

**Registro sugerido:** “Diversidade de cor de pele declarada qualitativamente; desempenho entre grupos/tons de pele não reportado.”

**Evidências:** página 4, Data Acquisition and Pre-Processing; avaliação nas páginas 12–14; anotação 03.

## RQ6 — Quais modelos e abordagens de inteligência artificial são utilizados para identificar manifestações dermatológicas associadas à hanseníase?

**Resposta:** abordagem híbrida de segmentação profunda, características manuais de textura e características profundas, seguida de aprendizado supervisionado:

*   **U-Net:** segmentação da ROI.
*   **GLCM:** vetor de características estatísticas/espaço-texturais.
*   **ResNet101:** características profundas da ROI RGB.
*   **Fusão:** concatenação dos vetores.
*   **Classificador final:** Random Forest; comparação com Naive Bayes, k-NN, SVM, Decision Tree e ANN.

Não é uma única CNN de ponta a ponta para a tarefa final. O RF realiza a classificação binária após extração/fusão. A origem dos pesos de ResNet101 não é informada com clareza suficiente para afirmar pré-treinamento no ImageNet. Não há ajuste completo documentado para todos os classificadores.

**Inconsistências de especificação:** na página 3 aparece **ResNet50**, embora o resumo, as seções detalhadas e as tabelas usem **ResNet101**. Adotar ResNet101 como modelo predominante reportado e registrar a discrepância. A lista de características GLCM também varia entre método/resultados e conclusão (oito versus sete, com nomes diferentes). As descrições arquiteturais não foram verificadas contra código.

**Evidências:** páginas 3, 6–13 e 15; anotações 08, 11–13, 18 e 21–32.

## RQ7 — Como a capacidade de generalização dos modelos é avaliada, especialmente quando são utilizados conjuntos de dados diferentes daqueles empregados no treinamento?

**Resposta:** não localizei **avaliação externa/cross-dataset**, centro reservado para teste, avaliação por país/tom de pele ou estudo prospectivo clínico. A avaliação descrita é interna, com o esquema 70%/30% denominado pelos autores como OOB/cross-validation, sem detalhes suficientes para caracterizar precisamente o procedimento.

Reunir imagens de hospitais e fontes online em uma coleção não equivale a treinar em uma fonte e testar em outra. A Tabela 6 compara resultados relatados por outros trabalhos; isso não demonstra que o modelo proposto generaliza para os respectivos datasets.

Aumento, uso de ROI e ensemble são estratégias que podem motivar hipóteses de robustez, mas não substituem validação externa. A quantidade de normais, o número de pacientes, a independência das imagens e a separação de versões aumentadas não estão suficientemente descritos. A ausência de repetições e incerteza estatística limita a avaliação de estabilidade.

**Registro sugerido:** “Avaliação interna com descrição ambígua de 70% treino/30% OOB; validação externa/cross-dataset não localizada.” Não registrar as alegações de uso em tempo real como benchmark medido de implantação: o artigo apresenta ambiente computacional, mas não latência clínica validada.

**Evidências:** páginas 4, 11–14; anotações 02, 05, 14 e 19.

## RQ8 — O artigo foi publicado em que tipo de veículo de publicação? (revista, conferência)

**Resposta:** **revista/periódico** — *SN Computer Science*, volume **5**, artigo **742**, ano **2024**, Springer Nature. O cabeçalho indica **Original Research**, recebido em 18 de maio de 2024 e aceito em 13 de junho de 2024. DOI **10.1007/s42979-024-03054-2**. Não é conferência nem revisão de literatura.

**Evidência:** página 1; anotação 33.

## Síntese para extração

**Pipeline:** U-Net → ROI RGB → GLCM + ResNet101 → concatenação → Random Forest. **Dataset:** 220 imagens iniciais de hanseníase, 450 após aumento segundo o texto; classe normal e total de pacientes não quantificados. **Resultado principal da tabela:** accuracy 97,24%, precision 99,69%, recall 95,82%, F=0,98, com divergências de relato preservadas. **Tons de pele:** sem avaliação estratificada. **Teste externo:** não localizado. **Veículo:** periódico.

# Trechos e notas para o Zotero

Cada número corresponde a uma anotação no PDF. Os trechos textuais abaixo são literais, com quebras de linha/hifenização de fim de linha normalizadas. Nas linhas da Tabela 5, o grifo seleciona classificador e valores; o título da anotação identifica o grupo de características. A ordem é Accuracy (%), Precision, Recall e F-Measure. A escala original foi preservada. Os comentários podem ser copiados diretamente para o Zotero.

## 01. Tarefa e classes

**Página 3 · Introdução**

**Trecho grifado:**

> Here, RF algorithm classified each input image as “Leprosy Detected” or “Normal” and labelled them as 1 and 0, respectively.

**Comentário:**

Tipo de estudo: pesquisa experimental computacional. RQ1/RQ6 — Classificação binária por imagem: hanseníase detectada (1) versus normal (0), usando Random Forest após segmentação e extração de características. Não é classificação de subtipos PB/MB, gravidade ou diagnóstico diferencial entre múltiplas dermatoses.

## 02. Origem dos dados

**Página 4 · Proposed System — A. Data Acquisition and Pre-Processing**

**Trecho grifado:**

> The primary samples were collected from the different hospitals and leprosy related institutions involved in diagnosis, treatment and rehabilitations. In addition, online repositories providing snippet of the leprosy and allied spatio-textural diversities were also taken into consideration.

**Comentário:**

RQ2/RQ7 — Coleta primária por câmera convencional em hospitais/instituições de hanseníase, acrescida de imagens de repositórios online. Não localizei nomes de todos os centros/fontes, distribuição por origem, número de pacientes, período de coleta ou protocolo completo de confirmação diagnóstica. Mistura de fontes não equivale a teste externo entre datasets.

## 03. Diversidade de cor alegada

**Página 4 · Proposed System — A**

**Trecho grifado:**

> Similarly, the data were selected from the patients of different skin colors, skin and lesion gradients.

**Comentário:**

RQ2/RQ5 — Seleção alegada de pacientes com diferentes cores de pele e gradientes de pele/lesão. Não são apresentados grupos Fitzpatrick/Monk, contagens por tom, métricas estratificadas ou comparação estatística entre tons. Diversidade declarada não demonstra desempenho equivalente entre grupos.

## 04. Amostra inicial e aumento

**Página 4 · Proposed System — A**

**Trecho grifado:**

> The initial data sampling encompassed a total of 220 images pertaining to the different leprosy cases.

**Comentário:**

RQ2 — 220 imagens iniciais referentes a casos de hanseníase. Não são 220 pacientes nem 220 lesões únicas. O texto seguinte informa aumento/re-amostragem para 450 imagens relacionadas à hanseníase e inclusão de imagens normais, sem quantificar estas últimas ou esclarecer o total final das duas classes.

## 05. Aumento e classe normal

**Página 4 · Proposed System — A**

**Trecho grifado:**

> Thus, a total of 450 leprosy related images were obtained. In reference to the two-class classification problem (Normal Image and Leprosy Detected), we also considered normal skin images as well, which was collected from the different body parts of the patients pertaining to both male as well as female genders.

**Comentário:**

RQ1/RQ2/RQ3 — Após aumento/re-amostragem, o texto relata 450 imagens relacionadas à hanseníase; também inclui pele normal de homens e mulheres, sem informar sua contagem. Não registrar 450 como total final inequívoco das duas classes. Transformações geram variantes, não novos pacientes. Não fica claro se o aumento ocorreu apenas após separar os conjuntos de avaliação.

## 06. Redimensionamento e cinza

**Página 5 · Proposed System — A**

**Trecho grifado:**

> To ensure better ROI segmentation, the input images were processed for resizing by applying Matlab resizing function, which retained the input images in the dimension of \[400 × 496] pixels. The input images were converted into equivalent gray scale images by applying RGB2GRAY transformation function.

**Comentário:**

RQ1 — Redimensionamento para 400 × 496 e conversão RGB2GRAY antes da segmentação. O pré-processamento também descreve equalização de histograma/intensidade, ajuste adaptativo de contraste e normalização z-score. A entrada do ResNet101 é posteriormente redimensionada para 224 × 224 × 3; são etapas diferentes, não dimensões intercambiáveis.

## 07. Normalização

**Página 6 · Proposed System — A/B**

**Trecho grifado:**

> distributions mean as zero and standard deviation as 1.

**Comentário:**

RQ1 — Normalização z-score, pela expressão (x−média)/desvio-padrão apresentada na equação 5. É pré-processamento, não evidência de controle de viés por tom de pele. Não são explicitados todos os detalhes de estimação dos parâmetros entre treino e avaliação.

## 08. Segmentação U-Net

**Página 6 · B. Semantic Segmentation**

**Trecho grifado:**

> in this work, a novel fully convolutional network driven UNet architecture is designed for ROI segmentation over input leprosy images.

**Comentário:**

RQ1/RQ6 — U-Net segmenta ROI versus fundo; em seguida a máscara é combinada com a imagem original para preservar a ROI em RGB. Não é Fuzzy C-Means/Firefly: esses métodos pertencem a outro trabalho. As Tabelas 2–3 mostram exemplos; não localizei Dice/IoU ou avaliação quantitativa própria da segmentação.

## 09. Mapas de referência e treinamento

**Página 7 · UNet Training for ROI Segmentation**

**Trecho grifado:**

> To perform ROI segmentation, the proposed method applied the input images and corresponding segmentation maps to train the network.

**Comentário:**

RQ2/RQ3 — Treinamento supervisionado da U-Net usa imagens e mapas de segmentação correspondentes. Não localizei descrição suficiente de quem produziu as máscaras, critérios de anotação, concordância entre anotadores ou splits próprios para treinar/avaliar a segmentação. A independência da etapa de segmentação em relação ao teste de classificação não é demonstrada pelo relato.

## 10. Lote e perda

**Página 7 · UNet Training for ROI Segmentation**

**Trecho grifado:**

> To ensure optimal leverage between the computational costs and accuracy the batch size of 8 was taken into consideration.

**Comentário:**

RQ3 — Batch size 8 para U-Net. O texto descreve Adam, softmax por pixel e entropia cruzada com ponderação de pixels/bordas. Na página 11, learning rate inicial 0,0001 e 200 épocas. Esses parâmetros se referem à U-Net, não devem ser atribuídos automaticamente ao RF ou a todas as redes.

## 11. Entrada do ResNet101

**Página 10 · ResNet101 Deep Residual Feature Extraction**

**Trecho grifado:**

> For ResNet101 realization, the deployed deep network resized the pre-processed image and hence each image was resized to the dimension of 224 × 224 × 3.

**Comentário:**

RQ1/RQ6 — ResNet101 recebe ROI em RGB a 224 × 224 × 3. A equação 21 normaliza x/127,5−1 (correspondente a \[−1,1] se x estiver em \[0,255]). O artigo não informa de modo suficiente a origem dos pesos pré-treinados ou o protocolo completo de treinamento/fine-tuning do ResNet; não presumir ImageNet.

## 12. Oito características e divergência na conclusão

**Página 12 · Results and Discussion**

**Trecho grifado:**

> generated a total of eight features including contrast, energy, homogeneity, correlation, mean, standard deviation, kurtosis and skewness.

**Comentário:**

RQ1/RQ6 — Esta seção lista oito características GLCM: contraste, energia, homogeneidade, correlação, média, desvio-padrão, curtose e assimetria. A conclusão (p.15) fala em sete e lista entropia/variância, diferindo desta relação. Preservar a divergência; não fundir as listas como se fossem uma especificação única inequívoca.

## 13. Fusão e classificação

**Página 10 · D. Feature Fusion**

**Trecho grifado:**

> The obtained composite feature vector (23) was the fed as input to the random forest ensemble algorithm to perform binary classification, which classifies each input image into two classes “Leprosy” or “Normal Lesion”,

**Comentário:**

RQ1/RQ6 — Concatenação horizontal dos vetores GLCM e ResNet101 (fusão no nível de características), seguida de Random Forest para classificação binária. O papel do ResNet101 é extrair características; o classificador final selecionado é RF. Número de árvores, profundidade e demais hiperparâmetros não são especificados suficientemente.

## 14. Divisão 70/30 e uso ambíguo de out-of-bag

**Página 11 · E. Random Forest Ensemble Classification**

**Trecho grifado:**

> The proposed method 70% data samples were applied as training set, while 30% were used as the out-of-bag data for further cross-validation during classification.

**Comentário:**

RQ3/RQ7 — O artigo descreve 70% treino e 30% como out-of-bag para cross-validation. Não esclarece se é holdout, avaliação OOB por bootstrap de árvores ou outro esquema; não informa número de folds. Não registrar como k-fold confirmado. Faltam contagens exatas, separação por paciente/fonte e controle de variantes aumentadas entre conjuntos.

## 15. Hiperparâmetros U-Net

**Página 11 · Results and Discussion**

**Trecho grifado:**

> UNet deep network was applied with ADAM non-linear optimization function where the initial learning rate was assigned as 0.0001. In addition, the total number of epochs were assigned as 200.

**Comentário:**

RQ3/RQ6 — U-Net: Adam, learning rate inicial 0,0001, 200 épocas; lote 8 na p.7. Não são fornecidas repetições, intervalos de confiança ou testes estatísticos. A alegação de mitigação de desequilíbrio pela retirada de fundo não demonstra balanceamento entre as classes de pacientes/imagens.

## 16. Métricas de classificação

**Página 12 · Results and Discussion**

**Trecho grifado:**

> statistical performance parameters including leprosy prediction accuracy, precision, recall and F-score.

**Comentário:**

RQ4 — Accuracy, precision, recall e F-score, definidos a partir de TP/TN/FP/FN na Tabela 4. Não localizei contagens brutas da matriz, AUC, especificidade como resultado separado, Dice/IoU da segmentação ou intervalos de confiança. Diferenciar avaliação de classificação por imagem das máscaras de ROI.

## 17. Resultados do resumo

**Página 1 · Resumo**

**Trecho grifado:**

> The simulation results revealed that the proposed model exhibits accuracy and F-Measure of 97.20% and 97.80%, respectively.

**Comentário:**

RQ3/RQ4 — Resumo: accuracy 97,20% e F-measure 97,80%. Tabelas 5–6 e conclusão usam accuracy 97,24% e F=0,98/98%. São apresentações distintas; não substituir silenciosamente os números do resumo pelos da tabela. Precision 99,69% e recall 95,82% aparecem nas tabelas/resultados.

## 18. ResNet50 versus ResNet101

**Página 3 · Introdução**

**Trecho grifado:**

> we applied a well-known residual network named ResNet50 to extract ROI-specific features from the input images.

**Comentário:**

RQ1/RQ6 — Este trecho menciona ResNet50, enquanto resumo, metodologia detalhada, tabelas e conclusão descrevem ResNet101. Registrar como inconsistência textual, adotando ResNet101 como modelo predominante relatado, sem afirmar verificação da implementação.

## 19. Comparação com literatura não é teste externo

**Página 13 · Inter-Model Assessment**

**Trecho grifado:**

> In inter-model assessment, we focus to assess whether the proposed model yields superior over the other state-of-art leprosy detection and classification systems.

**Comentário:**

RQ3/RQ7 — A Tabela 6 compara resultados atribuídos a estudos anteriores, incluindo modalidades e protocolos diferentes. Não foi identificado treinamento em um dataset e teste independente em outro, nem reavaliação uniforme dos baselines externos. Não usar esse ranking como demonstração de generalização cross-dataset.

## 20. Acesso aos dados

**Página 15 · Data Availability**

**Trecho grifado:**

> The dataset generated and analyzed during the current study are available from the corresponding author on reasonable request.

**Comentário:**

RQ2 — Dados disponíveis mediante solicitação razoável ao autor correspondente. Não é um dataset publicamente baixável identificado por link no PDF. Número de pacientes, contagem da classe normal e composição demográfica continuam não informados de forma suficiente.

## 21. GLCM / NB

**Página 12 · Tabela 5**

**Trecho grifado:**

> NB 93.20 0.91 0.98 0.88

**Comentário:**

RQ3/RQ4/RQ6 — GLCM com NB: accuracy 93.20%; precision 0.91; recall 0.98; F-measure 0.88, transcritos da Tabela 5. Precision, recall e F estão apresentados em escala decimal. Não converter a accuracy para fração sem identificar a mudança de escala. F1 e P/R não têm protocolo de agregação explicitado. P=0,91 e R=0,98 dariam F1 direto de aproximadamente 0,944, não 0,88. O relato não esclarece a divergência.

## 22. GLCM / k-NN

**Página 12 · Tabela 5**

**Trecho grifado:**

> k-NN 92.51 0.91 0.99 0.94

**Comentário:**

RQ3/RQ4/RQ6 — GLCM com k-NN: accuracy 92.51%; precision 0.91; recall 0.99; F-measure 0.94, transcritos da Tabela 5. Precision, recall e F estão apresentados em escala decimal. Não converter a accuracy para fração sem identificar a mudança de escala. F1 e P/R não têm protocolo de agregação explicitado.

## 23. GLCM / SVM

**Página 12 · Tabela 5**

**Trecho grifado:**

> SVM 91.96 0.73 0.99 0.88

**Comentário:**

RQ3/RQ4/RQ6 — GLCM com SVM: accuracy 91.96%; precision 0.73; recall 0.99; F-measure 0.88, transcritos da Tabela 5. Precision, recall e F estão apresentados em escala decimal. Não converter a accuracy para fração sem identificar a mudança de escala. F1 e P/R não têm protocolo de agregação explicitado.

## 24. GLCM / DT

**Página 12 · Tabela 5**

**Trecho grifado:**

> DT 95.52 0.84 0.88 0.93

**Comentário:**

RQ3/RQ4/RQ6 — GLCM com DT: accuracy 95.52%; precision 0.84; recall 0.88; F-measure 0.93, transcritos da Tabela 5. Precision, recall e F estão apresentados em escala decimal. Não converter a accuracy para fração sem identificar a mudança de escala. F1 e P/R não têm protocolo de agregação explicitado. Atenção: F=0,93 excede tanto P=0,84 quanto R=0,88; não corresponde à média harmônica direta desses valores (aproximadamente 0,86). Verificar erro de relato ou diferença de cálculo, sem corrigir silenciosamente.

## 25. GLCM / ANN

**Página 12 · Tabela 5**

**Trecho grifado:**

> ANN 95.59 0.93 0.98 0.94

**Comentário:**

RQ3/RQ4/RQ6 — GLCM com ANN: accuracy 95.59%; precision 0.93; recall 0.98; F-measure 0.94, transcritos da Tabela 5. Precision, recall e F estão apresentados em escala decimal. Não converter a accuracy para fração sem identificar a mudança de escala. F1 e P/R não têm protocolo de agregação explicitado.

## 26. GLCM / RF

**Página 12 · Tabela 5**

**Trecho grifado:**

> RF 95.63 0.93 0.98 0.95

**Comentário:**

RQ3/RQ4/RQ6 — GLCM com RF: accuracy 95.63%; precision 0.93; recall 0.98; F-measure 0.95, transcritos da Tabela 5. Precision, recall e F estão apresentados em escala decimal. Não converter a accuracy para fração sem identificar a mudança de escala. F1 e P/R não têm protocolo de agregação explicitado.

## 27. GLCM + ResNet101 / NB

**Página 12 · Tabela 5**

**Trecho grifado:**

> NB 94.57 0.91 0.98 0.93

**Comentário:**

RQ3/RQ4/RQ6 — GLCM + ResNet101 com NB: accuracy 94.57%; precision 0.91; recall 0.98; F-measure 0.93, transcritos da Tabela 5. Precision, recall e F estão apresentados em escala decimal. Não converter a accuracy para fração sem identificar a mudança de escala. F1 e P/R não têm protocolo de agregação explicitado.

## 28. GLCM + ResNet101 / k-NN

**Página 12 · Tabela 5**

**Trecho grifado:**

> k-NN 95.03 0.87 0.99 0.93

**Comentário:**

RQ3/RQ4/RQ6 — GLCM + ResNet101 com k-NN: accuracy 95.03%; precision 0.87; recall 0.99; F-measure 0.93, transcritos da Tabela 5. Precision, recall e F estão apresentados em escala decimal. Não converter a accuracy para fração sem identificar a mudança de escala. F1 e P/R não têm protocolo de agregação explicitado.

## 29. GLCM + ResNet101 / SVM

**Página 12 · Tabela 5**

**Trecho grifado:**

> SVM 94.28 0.91 0.93 0.92

**Comentário:**

RQ3/RQ4/RQ6 — GLCM + ResNet101 com SVM: accuracy 94.28%; precision 0.91; recall 0.93; F-measure 0.92, transcritos da Tabela 5. Precision, recall e F estão apresentados em escala decimal. Não converter a accuracy para fração sem identificar a mudança de escala. F1 e P/R não têm protocolo de agregação explicitado.

## 30. GLCM + ResNet101 / DT

**Página 12 · Tabela 5**

**Trecho grifado:**

> DT 95.45 0.93 0.98 0.93

**Comentário:**

RQ3/RQ4/RQ6 — GLCM + ResNet101 com DT: accuracy 95.45%; precision 0.93; recall 0.98; F-measure 0.93, transcritos da Tabela 5. Precision, recall e F estão apresentados em escala decimal. Não converter a accuracy para fração sem identificar a mudança de escala. F1 e P/R não têm protocolo de agregação explicitado. A accuracy é inferior à da mesma técnica usando somente GLCM; o ganho de fusão não é uniforme para todos os classificadores.

## 31. GLCM + ResNet101 / ANN

**Página 12 · Tabela 5**

**Trecho grifado:**

> ANN 95.19 0.91 0.99 0.96

**Comentário:**

RQ3/RQ4/RQ6 — GLCM + ResNet101 com ANN: accuracy 95.19%; precision 0.91; recall 0.99; F-measure 0.96, transcritos da Tabela 5. Precision, recall e F estão apresentados em escala decimal. Não converter a accuracy para fração sem identificar a mudança de escala. F1 e P/R não têm protocolo de agregação explicitado. A accuracy é inferior à da mesma técnica usando somente GLCM; o ganho de fusão não é uniforme para todos os classificadores.

## 32. GLCM + ResNet101 / RF

**Página 12 · Tabela 5**

**Trecho grifado:**

> RF 97.24 99.69 95.82 0.98

**Comentário:**

RQ3/RQ4/RQ6 — GLCM + ResNet101 com RF: accuracy 97.24%; precision 99.69; recall 95.82; F-measure 0.98, transcritos da Tabela 5. Esta linha usa precision/recall em escala percentual (99,69%/95,82%), diferente das demais linhas decimais. F=0,98 equivale a 98%. É o maior valor de accuracy da comparação interna. O resumo informa 97,20%/97,80% para accuracy/F; preservar a diferença.

## 33. Veículo de publicação

**Página 1 · Cabeçalho editorial**

**Trecho grifado:**

> SN Computer Science (2024) 5:742

**Comentário:**

RQ8 — Artigo original em periódico: SN Computer Science, volume 5, artigo 742, 2024, Springer Nature. DOI 10.1007/s42979-024-03054-2. Não é conferência. As RQ1–RQ4 citadas pelos próprios autores nas páginas 13–14 não são os enunciados das oito RQs desta revisão.
