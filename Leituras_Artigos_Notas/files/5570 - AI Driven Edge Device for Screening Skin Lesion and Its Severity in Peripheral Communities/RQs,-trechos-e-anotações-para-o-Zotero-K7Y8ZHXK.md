---
tags: []
parent: 'AI Driven Edge Device for Screening Skin Lesion and Its Severity in Peripheral Communities'
collections:
    - TCC_Leituras
$version: 197
$libraryID: 2
$itemKey: K7Y8ZHXK

---
# RQs, trechos e anotações para o Zotero

**Artigo:** Chathura N. Jaikishore; Venkanna Udutalapally; Debanjan Das. *AI Driven Edge Device for Screening Skin Lesion and Its Severity in Peripheral Communities*. 2021 IEEE 18th India Council International Conference (INDICON), IEEE, 2021. **DOI:** 10.1109/INDICON52576.2021.9691666.

**Fonte e escopo:** PDF fornecido, seis páginas. As páginas indicadas são as posições no PDF, que não apresenta numeração impressa convencional. Análise limitada ao artigo, sem auditoria externa do dataset, código ou aplicativo. Os enunciados das oito RQs foram fornecidos pelo usuário. Resultados publicados, cálculos desta leitura e informações não localizadas são identificados separadamente.

**Tipo de estudo:** pesquisa experimental computacional com comparação de CNNs e desenvolvimento de protótipo Android. O sistema classifica imagens em quatro classes e propõe um segundo classificador de gravidade. Não é revisão nem validação clínica prospectiva realizada em comunidades periféricas.

## RQ1 — Quais técnicas de visão computacional são utilizadas para identificar manifestações dermatológicas associadas à hanseníase?

**Resposta:** classificação de imagens por CNNs com transferência de aprendizado e ajuste de camadas finais. **SkinLesion Net**, baseado em MobileNetV2, distingue eczema, sarampo, hanseníase e pele saudável; **SeverityNet**, também baseado em MobileNetV2, classifica gravidade em *mild/severe*. O estudo descreve classificação por imagem, não detecção com caixas delimitadoras nem segmentação por máscara.

O pré-processamento inclui redimensionamento para **224 × 224 × 3** e reescala para normalização. O aumento envolve zoom, deslocamentos horizontal/vertical e rotação de **45°**. O fator da normalização, faixas completas das transformações e parâmetros de preservação da proporção não são suficientemente detalhados. Não localizei remoção de pelos, segmentação de ROI ou técnica específica de explicabilidade aplicada ao modelo proposto; métodos de segmentação citados na revisão de literatura não devem ser atribuídos à implementação.

As características são aprendidas pelas CNNs pré-treinadas em **ImageNet**, com flatten, batch normalization, camadas densas de 512 e 128 unidades, dropout e regularização L2. Há softmax para as quatro classes; para SeverityNet, os autores descrevem duas saídas e ativação sigmoid.

**Limitação essencial:** o treinamento de SeverityNet é descrito apenas com eczema e sarampo. Assim, o artigo não demonstra classificação validada da gravidade da hanseníase, apesar de exibi-la no protótipo.

**Evidências:** páginas 1–3 e 5, seções I, III.A–B e IV.B–D; anotações 01–02, 04–11, 15 e 22.

## RQ2 — Quais conjuntos de dados e populações são utilizados no desenvolvimento e na avaliação desses modelos?

**Resposta:** conjunto montado pelos autores a partir de **DermNet NZ**, **CNN-image-dataset** e outras imagens obtidas por **web scraping**. A referência \[16] aponta para um conjunto no IEEE DataPort. O artigo afirma que as imagens são certificadas por médicos, mas não apresenta procedimento detalhado de confirmação diagnóstica, rotulagem ou concordância entre avaliadores.

A **Tabela III, página 4**, informa:

| Classe                        | Imagens   | Treinamento | Teste   |
| ----------------------------- | --------- | ----------- | ------- |
| Measles (sarampo)             | 51        | 41          | 10      |
| Eczema                        | 1.235     | 988         | 247     |
| Leprosy (hanseníase)          | 157       | 126         | 31      |
| Normal Skin                   | 81        | 65          | 16      |
| **Total calculado da tabela** | **1.524** | **1.220**   | **304** |


**Unidade:** imagens; não pacientes, lesões únicas ou anotações de bounding boxes. Não localizei número de pacientes, distribuição etária/sexo, país de origem de cada imagem, tom de pelRe ou separação por identidade de paciente. A motivação indiana e as afiliações dos autores não comprovam população exclusivamente indiana. Não há recrutamento de uma coorte em comunidades periféricas descrito.

**Divergência de contagens:** o parágrafo abaixo da tabela declara **159 imagens de sarampo e 51 de hanseníase**, além de 1.235 de eczema e 81 de pele saudável. Essa série soma **1.526**, não 1.524. Não corrigir a divergência silenciosamente: usar a tabela como série identificada, com a ressalva do texto conflitante.

**Dataset de gravidade:** página 5: **45 imagens de eczema + 45 de sarampo = 90 imagens**, antes do aumento. Não há hanseníase na descrição desse treinamento, nem contagens por mild/severe, critério clínico operacional dos rótulos ou tamanho efetivo do teste correspondente à acurácia de 91%.

**Aumento:** os autores relatam 47–48 novas imagens por época e associam isso à razão entre imagens de treino e batch size. Entretanto, **1.220/32 = 38,125**; **1.524/32 = 47,625**. A descrição é inconsistente/ambígua e não estabelece um total final aumentado reproduzível.

**Fontes transcritas do artigo, não auditadas:** DermNet NZ (referência \[15]) e IEEE DataPort, *Image dataset for various skin conditions and rashes* (referência \[16]). A disponibilidade e a composição exata da coleção final dos autores não são estabelecidas por essas referências.

**Evidências:** páginas 2, 4–6, Tabela III e seções III.A, IV.A–B; anotações 03, 06 e 12–15.

## RQ3 — Quais métodos, procedimentos são utilizados para avaliar o desempenho desses modelos e quais resultados são reportados?

**Resposta:** holdout de aproximadamente **80% para treinamento e 20% para teste**, com **1.220/304 imagens**. São comparadas quatro arquiteturas ajustadas, usando métricas agregadas, curvas de acurácia/perda e matrizes de confusão. O treinamento descrito usa **Adamax**, learning rate **0,0001**, lote **32** e categorical cross-entropy; SeverityNet usa binary cross-entropy. A Figura 4 mostra cinco épocas, mas não documenta por si só todos os regimes de treino dos modelos.

Não localizei conjunto de validação separado, validação cruzada, repetições, sementes, intervalos de confiança ou testes de significância. A escolha do lote após experimentação é mencionada, sem protocolo completo de ajuste. Tampouco são descritas deduplicação das imagens web e separação por paciente/fonte. Essas lacunas limitam avaliar independência do teste e estabilidade dos resultados; não provam, por si só, vazamento efetivo.

O **resultado publicado para SkinLesion Net** é acurácia de teste **94,32%**, F1 **93,02%**, precision **93,53%** e recall **92,76%**. São métricas gerais das quatro classes. Para **SeverityNet**, os autores declaram **91% de acurácia**, sem matriz própria ou protocolo suficiente de avaliação da gravidade. A Figura 1 sugere 80%/20% também nessa etapa, mas não fornece as contagens que sustentam os 91%.

**Problemas de consistência:**

*   O relato de **22 erros em 304 imagens** corresponde a **92,76% de acurácia**, e não aos 94% afirmados na frase nem aos 94,32% da tabela.
*   A Figura 7(a) apresenta suporte de **12** na linha rotulada Leprosy, enquanto a Tabela III declara **31** imagens de hanseníase no teste.
*   O texto afirma melhor desempenho em todas as métricas, mas a Tabela II dá maior precision ao VGG16 e maior F1 ao InceptionV3.

A apresentação de telas do aplicativo é demonstração do protótipo, não teste clínico ou estudo externo em comunidades periféricas.

**Evidências:** páginas 2–5, Tabela II, Figuras 1, 4 e 7; anotações 03, 06, 09–10 e 15–23.

## RQ4 — Quais métricas são utilizadas para avaliar o desempenho desses modelos e quais resultados são reportados?

**Resposta:** **accuracy, precision, recall/sensibilidade e F1-score**, além de perdas de treino/teste e matrizes de confusão. O artigo apresenta fórmulas de custo de convolução e menciona tamanho do modelo. Não localizei AUC, especificidade como resultado separado, métricas por tom de pele, intervalos de confiança ou valores medidos de latência/FPS. A agregação multiclasse de precision/recall/F1 (macro, micro ou ponderada) não é explicitada.

Valores da **Tabela II, página 4**, preservados como publicados:

| Modelo ajustado | Accuracy treino (%) | Accuracy teste (%) | Perda treino | Perda teste | F1 (%) | Precision (%) | Recall (%) |
| --------------- | ------------------- | ------------------ | ------------ | ----------- | ------ | ------------- | ---------- |
| VGG16           | 82,35               | 81,58              | 0,5667       | 0,4679      | 88,98  | 97,62         | 82,23      |
| InceptionV3     | 85,70               | 91,12              | 1,2074       | 0,9682      | 93,26  | 94,58         | 92,43      |
| Xception        | 90,60               | 93,42              | 0,2834       | 0,1797      | 92,71  | 93,70         | 92,10      |
| SkinLesion Net  | 83,96               | 94,32              | 1,1308       | 0,8601      | 93,02  | 93,53         | 92,76      |


**SeverityNet:** acurácia declarada de **91%**. Não atribuir esse número à gravidade de hanseníase: o treinamento de gravidade descrito usa eczema e sarampo.

**Hanseníase especificamente:** não localizei tabela textual de métricas por doença. A Figura 7(a), com True Label no eixo vertical e Predicted Label no horizontal, mostra linha Leprosy **\[2, 7, 0, 3]**, nas colunas Eczema, Leprosy, Measles e Normal Skin. A partir dos valores visíveis, é possível obter:

| Cálculo local da Figura 7(a) para Leprosy | Valor          |
| ----------------------------------------- | -------------- |
| Verdadeiros positivos                     | 7              |
| Falsos positivos                          | 2 + 1 + 0 = 3  |
| Falsos negativos                          | 2 + 0 + 3 = 5  |
| Precision calculada                       | 7/10 = 70,00%  |
| Recall calculado                          | 7/12 = 58,33%  |
| F1 calculado                              | 14/22 = 63,64% |


**Esses cálculos são desta leitura, não métricas explicitamente reportadas pelos autores.** O suporte da linha é 12, incompatível com as 31 imagens de teste da Tabela III. Por isso, não tratá-los como estimativa validada do conjunto de teste descrito, nem substituir as métricas publicadas. A célula de eczema está arredondada como `2.4e+02`, impedindo reconstruir com certeza o total exato da matriz. Os elementos fora da diagonal somam 22, coerentes com o relato de erros, mas não com a acurácia declarada.

**Eficiência:** tamanho aproximado **14 MB** para SkinLesion Net. A expressão “virtually no latency” não é acompanhada de benchmark, modelo do telefone ou tempo em milissegundos. Custo teórico e tamanho do arquivo não equivalem a latência clínica medida.

**Evidências:** páginas 1 e 3–5; Tabela II e Figura 7(a); anotações 16–21 e 23.

## RQ5 — Como o desempenho dos modelos varia entre diferentes grupos ou tons de pele?

**Resposta:** **não é possível determinar pelo artigo**. Não localizei classificação de tom de pele (Fitzpatrick/Monk), contagens de grupos populacionais, métricas estratificadas, análise de equidade ou comparação entre tons. As imagens ilustrativas não permitem caracterizar a população completa nem inferir diferenças de desempenho.

A referência a comunidades periféricas e à prevalência das doenças na Índia caracteriza a motivação da aplicação, não uma análise quantitativa por população. **Registrar: “não informado/não avaliado no artigo”.** Não há trecho afirmativo que sustente comparação entre tons; por isso, não foi criado grifo que simule evidência inexistente.

**Base da ausência identificada:** leitura das seções de dataset e resultados, páginas 4–5, e conclusão, página 6. A anotação 12 registra a limitação da caracterização populacional.

## RQ6 — Quais modelos e abordagens de inteligência artificial são utilizados para identificar manifestações dermatológicas associadas à hanseníase?

**Resposta:** quatro CNNs pré-treinadas são ajustadas e comparadas: **MobileNetV2, VGG16, InceptionV3 e Xception**. O MobileNetV2 modificado recebe o nome **SkinLesion Net** e é escolhido para classificar quatro classes, incluindo hanseníase. **SeverityNet** é outro MobileNetV2 ajustado para classificação binária mild/severe. Trata-se de transferência de aprendizado e fine-tuning supervisionado.

A arquitetura relatada inclui flatten, batch normalization, camadas densas, dropout e L2. SkinLesion Net usa quatro saídas/softmax e categorical cross-entropy; SeverityNet, duas saídas/sigmoid e binary cross-entropy. O texto da metodologia não especifica integralmente todos os coeficientes e parâmetros.

Os modelos são convertidos para **TensorFlow Lite (**`.tflite`) e incorporados em aplicativo Android desenvolvido no Android Studio, com Java. O fluxo principal descrito é doença seguida de gravidade, embora outro trecho diga execução simultânea; essa diferença não é esclarecida.

**Restrição central:** a descrição de SeverityNet inclui só **90 imagens de eczema/sarampo**. A tela que apresenta gravidade de hanseníase não demonstra treinamento ou avaliação específica dessa tarefa. Não classificar o artigo como evidência validada de estadiamento clínico de hanseníase.

**Evidências:** páginas 1–3 e 5–6; anotações 01–02, 07–11, 15 e 19–22.

## RQ7 — Como a capacidade de generalização dos modelos é avaliada, especialmente quando são utilizados conjuntos de dados diferentes daqueles empregados no treinamento?

**Resposta:** a avaliação descrita é **interna**, com holdout da coleção reunida pelos autores. **Não localizei teste em dataset externo independente, treinamento em uma fonte e teste reservado em outra, validação entre instituições, avaliação por país/tom de pele ou estudo prospectivo em campo.**

Reunir imagens de várias fontes na mesma coleção não equivale a validação cross-dataset. O pré-treinamento no ImageNet também não é teste externo de hanseníase. O aumento de dados busca robustez, mas não demonstra transferência entre populações ou equipamentos. Sem separação explicitada por paciente/fonte e sem auditoria de duplicatas, a independência das amostras de teste permanece incerta.

O aplicativo e suas telas mostram viabilidade de implementação, mas não fornecem tamanho de amostra ou protocolo de avaliação em comunidades periféricas. A alegação de funcionamento independentemente da qualidade da imagem não vem acompanhada de experimento controlado de qualidade, iluminação, dispositivo ou tom de pele.

**Classificação para extração:** “holdout interno; validação externa/cross-dataset não localizada”. O grau de generalização de SeverityNet para hanseníase é especialmente incerto, porque a doença não aparece no dataset de gravidade descrito.

**Evidências:** páginas 2, 4–6; anotações 03, 12, 15 e 21–22.

## RQ8 — O artigo foi publicado em que tipo de veículo de publicação? (revista, conferência)

**Resposta:** **conferência** — *2021 IEEE 18th India Council International Conference (INDICON)*, IEEE, 2021. DOI **10.1109/INDICON52576.2021.9691666**. A identificação consta na margem editorial vertical da primeira página. Não é artigo de revista.

**Evidência:** página 1; anotação 24.

## Cuidados para registrar este estudo na revisão

*   Usar **157 imagens de hanseníase, 126/31 treino/teste**, identificando a Tabela III e registrando o texto divergente de 51 imagens.
*   Registrar **94,32%** como acurácia global **publicada** do SkinLesion Net; preservar separadamente o cálculo **92,76%** decorrente de 22 erros/304.
*   Não atribuir as métricas globais à hanseníase nem tratar os cálculos da matriz inconsistente como resultado validado.
*   Registrar **91% para gravidade como alegação geral**, sem evidência específica de hanseníase.
*   Tons de pele: **não avaliados quantitativamente**. Teste externo: **não localizado**.

# Trechos e notas para o Zotero

Cada número corresponde a uma anotação no PDF. Os trechos textuais abaixo são literais, com quebras de linha/hifenização de fim de linha normalizadas. Nas linhas de tabela, barras verticais separam as células, preservando os valores; os nomes dos modelos são reunidos quando quebrados em duas linhas. As duas últimas entradas são marcações de área na matriz e na margem editorial vertical, com transcrição dos rótulos visíveis. Os comentários podem ser copiados diretamente para o Zotero.

## 01. Tipo de estudo e classes

**Página 1 · Resumo**

**Trecho grifado:**

> A dataset consisting of four classes - Eczema, Measles, Leprosy, and Healthy Normal Skin is chosen in this proposed work.

**Comentário:**

Tipo de estudo: pesquisa experimental computacional com protótipo Android. RQ1/RQ6 — Classificação de imagens em eczema, sarampo, hanseníase e pele saudável. Não é revisão nem classificador binário exclusivo de hanseníase; resultados gerais não são desempenho específico dessa doença.

## 02. Gravidade por classificação

**Página 1 · I. Introduction**

**Trecho grifado:**

> This paper classifies the severity of a disease using a deep learning approach rather than using the image segmentation technique.

**Comentário:**

RQ1/RQ6 — A gravidade é tratada como classificação por CNN, não por segmentação de área lesionada. O estudo não apresenta máscara de lesão nem medida quantitativa de extensão como saída principal; não confundir uso da palavra detection com detecção de objetos por bounding boxes.

## 03. Divisão de treinamento e teste

**Página 2 · III.A. Pre-processing**

**Trecho grifado:**

> The dataset is distributed with 80% of images devoted to training and 20% of images to the testing dataset. Based on this distribution, 1220 images are used for training and 304 images for testing.

**Comentário:**

RQ2/RQ3/RQ7 — Holdout de aproximadamente 80%/20%: 1.220 imagens de treinamento e 304 de teste. Não localizei conjunto separado de validação, validação cruzada, repetições, sementes, intervalos de confiança nem separação por paciente ou por fonte. Não há descrição suficiente de deduplicação das imagens web. A divisão por imagem não comprova independência entre pacientes.

## 04. Redimensionamento

**Página 2 · III.A**

**Trecho grifado:**

> All the images are resized to 224 × 224 × 3 (default dimensions for pre-trained models) to standardize the images.

**Comentário:**

RQ1 — Entrada padronizada em 224 × 224 × 3, compatível com imagens de três canais. O texto não detalha preservação de proporção/padding, recorte de ROI ou segmentação específica de hanseníase.

## 05. Aumento e normalização

**Página 2 · III.A**

**Trecho grifado:**

> The dataset is augmented and up-sampled using the following parameters: 1) Re-scaling to normalize the image, 2) Zoom In and Zoom Out, 3) Width Shift, 4) Height Shift, 5) Rotation angle of 45°.

**Comentário:**

RQ1/RQ3 — Reescala para normalização; zoom de aproximação/afastamento; deslocamentos horizontal/vertical; rotação de 45°. São transformações de imagens para treinamento, não novos pacientes nem validação externa. Não são informados aqui todos os parâmetros/faixas das transformações ou fator exato da normalização.

## 06. Número de imagens aumentadas

**Página 2 · III.A**

**Trecho grifado:**

> In the proposed work, approximately 47-48 new images are added per epoch, thus up-sampling the dataset for training.

**Comentário:**

RQ1/RQ2/RQ3 — Os autores declaram 47–48 novas imagens por época e associam esse número à razão entre imagens de treino e batch size. Porém, com 1.220 imagens de treino e lote 32, a razão é 38,125; 1.524/32 é 47,625. Há inconsistência ou ambiguidade na descrição. Não converter essa afirmação em tamanho final comprovado do dataset.

## 07. Pré-treinamento e transferência

**Página 2 · II. Literature Survey and Background Work**

**Trecho grifado:**

> These models were pre-trained using images from ImageNet. This proposed work explores four CNN architectures that were pre-trained by transfer learning and fine-tuning a few layers.

**Comentário:**

RQ1/RQ6 — Transfer learning a partir de CNNs pré-treinadas no ImageNet e ajuste de camadas finais. Os modelos comparados são MobileNetV2, VGG16, InceptionV3 e Xception. ImageNet é origem de pré-treinamento, não dataset externo de teste de hanseníase.

## 08. Camadas adicionadas

**Página 3 · III.B. Transfer Learning and Fine Tuning**

**Trecho grifado:**

> A block of fully connected Dense Layer of size 512 and a Dropout Layer are concatenated. The next block comprises a fully connected Dense Layer of size 128 with L2 regularisation.

**Comentário:**

RQ1/RQ6 — Fine-tuning com camadas densas de 512 e 128 unidades, dropout e regularização L2; o parágrafo também descreve flatten e batch normalization. SkinLesion Net termina em quatro saídas/softmax. A especificação não inclui todos os coeficientes e detalhes necessários à reprodução.

## 09. Otimizador

**Página 3 · III.B**

**Trecho grifado:**

> Adamax optimiser is used to optimise the algorithm with a 0.0001 learning rate.

**Comentário:**

RQ3/RQ6 — Otimizador Adamax e learning rate 0,0001. O texto apresenta escolha experimental do lote, mas não descreve uma busca sistemática de hiperparâmetros com validação separada.

## 10. Lote e perda

**Página 3 · III.B**

**Trecho grifado:**

> The batch size is chosen as 32 after experimenting using different sizes. Categorical cross-entropy serves as the loss function.

**Comentário:**

RQ3/RQ6 — Lote 32 e categorical cross-entropy para classificação das quatro classes. A Figura 4 apresenta curvas de cinco épocas; não assumir que isso documenta todo o protocolo de todos os modelos. Não localizei repetição independente ou teste de significância.

## 11. Arquitetura de gravidade

**Página 3 · III.B**

**Trecho grifado:**

> Only the final layers are fine-tuned to grade whether the disease is Severe or Mild.

**Comentário:**

RQ1/RQ6 — SeverityNet é classificador binário mild/severe. O texto descreve transferência de características, camada densa com duas saídas, sigmoid e binary cross-entropy. Não informa critério clínico operacional suficiente para os rótulos de gravidade nem concordância entre avaliadores.

## 12. Origem das imagens

**Página 4 · IV.A. Dataset**

**Trecho grifado:**

> The dataset is collected from various open sources in the proposed work consisting of dermatological images certified by doctors. The sources include DermNet NZ, CNN-image-dataset, and other web scraped images

**Comentário:**

RQ2 — Imagens reunidas de fontes abertas, incluindo DermNet NZ, CNN-image-dataset e web scraping. A referência \[16] aponta para IEEE DataPort. Os autores afirmam certificação por médicos, mas não detalham processo de rotulagem, número de avaliadores ou confirmação diagnóstica individual. Não há coorte recrutada descrita, número de pacientes ou composição populacional suficiente. Contexto indiano não comprova que as imagens sejam de pacientes indianos.

## 13. Contagem de hanseníase na tabela

**Página 4 · Tabela III**

**Trecho grifado:**

> Leprosy | 157 | 126 | 31

**Comentário:**

RQ2 — A Tabela III informa hanseníase: 157 imagens, sendo 126 para treinamento e 31 para teste. São imagens, não pacientes nem lesões únicas. A tabela completa soma 1.524 imagens e 1.220/304 para treino/teste. O parágrafo abaixo traz 51 para hanseníase e 159 para sarampo, em divergência com a tabela. Registrar a origem de cada contagem.

## 14. Inconsistência nas contagens

**Página 4 · IV.A. Dataset**

**Trecho grifado:**

> The final data set is imbalanced with 159 images for Measles, 51 images for Leprosy, 1235 images for Eczema, and 81 images for Healthy Skin, tabulated in Table III.

**Comentário:**

RQ2/RQ3 — Divergência interna: este texto declara sarampo 159 e hanseníase 51; a Tabela III informa sarampo 51 e hanseníase 157. Além da troca aparente, há diferença 159/157. As contagens deste parágrafo somam 1.526, não 1.524. Para extração, manter a tabela como série identificada e preservar a contradição, sem corrigir silenciosamente.

## 15. Dataset de gravidade não inclui hanseníase na descrição

**Página 5 · IV.B. Skin Lesion and Severity Detection**

**Trecho grifado:**

> The SkinLesion Net uses 1524 images while SeverityNet is trained on 45 images of Eczema and Measles each. The data augmentation and pre-processing are applied on the 90 images to up-sample the data.

**Comentário:**

RQ2/RQ3/RQ6 — SeverityNet: 45 imagens de eczema e 45 de sarampo, total 90 antes de aumento. Hanseníase não aparece na descrição do treinamento de gravidade. Não são informadas contagens mild/severe, critérios de rotulagem ou tamanho efetivo do teste que produziu os 91%. A Figura 1 sugere divisão 80%/20% também para gravidade, mas o protocolo dessa amostra permanece insuficientemente descrito.

## 16. Resultado principal do SkinLesion Net

**Página 4 · Tabela II**

**Trecho grifado:**

> SkinLesion Net | 83.96 | 94.32 | 1.1308 | 0.8601 | 93.02 | 93.53 | 92.76

**Comentário:**

RQ3/RQ4/RQ6 — SkinLesion Net: accuracy treino 83,96%; teste 94,32%; perdas 1,1308/0,8601; F1 93,02%; precision 93,53%; recall 92,76%. São resultados globais, não exclusivos de hanseníase. A agregação multiclasse (macro/micro/weighted) não é explicitada. Há divergências com os erros relatados e a matriz da Figura 7.

## 17. Alegação de superioridade contradita pela tabela

**Página 4 · III.C. Performance Metrics**

**Trecho grifado:**

> It is observed from Table II that the SkinLesion Net provides the best performance in terms of Accuracy, Precision, Recall, and F1-Score

**Comentário:**

RQ3/RQ4 — A tabela dá ao SkinLesion Net a maior acurácia de teste (94,32%) e recall (92,76%), mas não a maior precision nem F1. VGG16 apresenta precision 97,62% e InceptionV3 F1 93,26%, acima de 93,53% e 93,02% do SkinLesion Net. A alegação de melhor desempenho em todas as métricas não é sustentada pela própria Tabela II.

## 18. Número de erros e acurácia

**Página 5 · IV.C. Results and Discussions**

**Trecho grifado:**

> Out of 304 test images, only 22 images are misclassified, achieving 94% accuracy.

**Comentário:**

RQ3/RQ4 — Inconsistência aritmética: 22 erros em 304 imagens implicam 282 acertos e accuracy de 92,76%, não 94% nem 94,32%. Os erros fora da diagonal da Figura 7(a) somam 22. Não substituir o valor publicado silenciosamente: registrar 94,32% como valor da tabela e 92,76% como cálculo a partir desta frase.

## 19. Acurácia de gravidade

**Página 5 · IV.C**

**Trecho grifado:**

> The SeverityNet proved to achieve 91% accuracy to assess the severity of the predicted disease.

**Comentário:**

RQ3/RQ4 — Accuracy de 91% para SeverityNet é declarada, mas sem tabela/matriz específica de gravidade nem detalhamento suficiente do teste ou de métricas por doença. O treinamento de gravidade descrito usa eczema e sarampo. Não registrar 91% como acurácia demonstrada de gravidade da hanseníase.

## 20. Modelo leve e conversão

**Página 5 · IV.C**

**Trecho grifado:**

> The weights of the trained model are stored in the .tflite file.

**Comentário:**

RQ6 — Conversão/implantação via TensorFlow Lite no Android. SkinLesion Net é descrito como aproximadamente 14 MB; não confundir tamanho do modelo com memória total da aplicação ou evidência de desempenho clínico.

## 21. Latência alegada sem benchmark

**Página 5 · IV.D. Android Mobile Application**

**Trecho grifado:**

> Deep Learning models are compatible with this application since it executes two models simultaneously with virtually no latency.

**Comentário:**

RQ3/RQ4/RQ7 — A alegação de latência quase nula não vem acompanhada de tempo medido, FPS, modelo do smartphone ou benchmark de memória/energia. A seção IV.C descreve execução dos modelos um após outro, enquanto aqui aparece simultaneously. Registrar a inconsistência; não converter a afirmação em latência zero medida.

## 22. Gravidade de hanseníase no protótipo

**Página 5 · IV.D**

**Trecho grifado:**

> We can observe in Fig. 8b) and Fig. 8c) that Leprosy and Measles are detected, respectively, along with the seriousness.

**Comentário:**

RQ3/RQ6/RQ7 — O protótipo apresenta hanseníase e sarampo com gravidade, mas o dataset descrito para SeverityNet contém apenas eczema e sarampo. A tela não demonstra validação da gravidade de hanseníase. Não localizei teste externo, estudo prospectivo ou avaliação clínica em comunidades periféricas.

## 23. Matriz e resultado específico de hanseníase

**Página 5 · Figura 7(a)**

**Rótulos da área marcada:**

> Eczema | Leprosy | Measles | Normal Skin Linha Leprosy: 2 | 7 | 0 | 3

**Comentário:**

RQ3/RQ4 — Na Figura 7(a), eixo vertical True Label e horizontal Predicted Label: linha Leprosy = \[2,7,0,3], total 12; a Tabela III declara 31 imagens de hanseníase no teste. A matriz permite calcular localmente precision 7/10=70%, recall 7/12=58,33% e F1 14/22=63,64%, mas esses NÃO são resultados explicitamente reportados e a divergência de suportes impede tratá-los como estimativa validada do teste descrito. A célula de eczema usa notação arredondada 2.4e+02, limitando reconstituição do total exato.

## 24. Veículo de publicação

**Página 1 · Margem editorial vertical**

**Rótulos da área marcada:**

> 2021 IEEE 18th India Council International Conference (INDICON) DOI: 10.1109/INDICON52576.2021.9691666

**Comentário:**

RQ8 — Artigo de conferência: 2021 IEEE 18th India Council International Conference (INDICON), IEEE. DOI 10.1109/INDICON52576.2021.9691666. Não é artigo de revista. Metadados transcritos da margem editorial da primeira página.
