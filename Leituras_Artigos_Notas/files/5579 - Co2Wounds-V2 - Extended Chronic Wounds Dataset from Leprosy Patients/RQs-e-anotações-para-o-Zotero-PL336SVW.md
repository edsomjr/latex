---
tags: []
parent: 'Co2Wounds-V2: Extended Chronic Wounds Dataset from Leprosy Patients'
collections:
    - TCC_Leituras
$version: 204
$libraryID: 2
$itemKey: PL336SVW

---
# RQs e anotações para o Zotero

**Artigo:** Karen Sanchez; Carlos Hinojosa; Olinto Mieles; Chen Zhao; Bernard Ghanem; Henry Arguello. *CO2Wounds-V2: Extended Chronic Wounds Dataset from Leprosy Patients*. 2024 IEEE International Conference on Image Processing (ICIP), IEEE, páginas 69–75. **DOI:** 10.1109/ICIP51287.2024.10647641.

**Fonte e escopo:** análise do PDF fornecido, sete páginas, sem auditoria dos repositórios externos ou do código. As oito RQs reproduzem os enunciados fornecidos pelo usuário. As referências de página usam a posição no PDF; correspondência com a paginação impressa: **1→69, 2→70, 3→71, 4→72, 5→73, 6→74, 7→75**.

**Tipo de estudo e enquadramento:** apresentação de dataset com experimentos de referência (*baselines*) de **segmentação semântica de feridas crônicas em pacientes com hanseníase**. A tarefa distingue pixels de ferida e fundo. Não é estudo de diagnóstico de hanseníase, classificação entre doenças, estadiamento de gravidade ou avaliação de eficácia do tratamento. Para a revisão, enquadrar como **segmentação/acompanhamento de feridas associadas à hanseníase**, preservando essa distinção.

## RQ1 — Quais técnicas de visão computacional são utilizadas para identificar manifestações dermatológicas associadas à hanseníase?

**Resposta:** segmentação semântica binária de imagens RGB, gerando máscaras de **ferida versus fundo**, usando redes profundas implementadas em PyTorch/Segmentation Models PyTorch (SMP). São avaliadas U-Net, FPN, DeepLabV3+ e, conforme a Tabela 1, também DeepLabV3. A tarefa delimita úlceras crônicas em pacientes já identificados como pessoas com hanseníase; não decide se o paciente tem a doença.

O preparo do dataset inclui remoção de duplicatas e imagens sem feridas, além de recorte para proporção **4:3**. A redação sobre “blurring images where the edges of the ulcer are difficult to detect” é ambígua; não permite registrar com segurança aumento por desfoque como técnica implementada. Não localizei resolução final de entrada das redes, normalização, política de aumento de dados ou outras transformações detalhadas no PDF.

Os contornos de **607 imagens** foram delineados usando **CVAT**, produzindo anotações COCO e máscaras binárias. A Figura 1 também mostra caixas delimitadoras, mas a avaliação experimental deste artigo é de segmentação, não de um detector de objetos. Os encoders usam pesos pré-treinados no ImageNet, conforme declaração dos autores.

A plataforma de coleta, apresentada anteriormente em \[19], permite visualizar segmentação e medidas de **área/perímetro** ao longo do tempo. Essas funcionalidades não equivalem a resultados de erro de área/perímetro ou eficácia clínica medidos para os baselines deste artigo.

**Evidências:** páginas 1–4, seções 2.1, 2.2.1–2.2.3 e 3.2; Figuras 1–2; anotações 01, 03 e 06–09, 14–15.

## RQ2 — Quais conjuntos de dados e populações são utilizados no desenvolvimento e na avaliação desses modelos?

**Resposta:** **CO2Wounds-V2**, atualização do CO2Wounds inicial de **164 imagens**. A versão V2 é declarada como contendo **764 imagens RGB de 96 pacientes com hanseníase**. Não somar as 164 da versão anterior às 764 da versão V2.

| Característica        | Informação do artigo                                                                     |
| --------------------- | ---------------------------------------------------------------------------------------- |
| Local                 | Sanatorio de Contratación ESE, Colômbia; equipe do programa de controle de hanseníase    |
| Pacientes             | 96                                                                                       |
| Sexo, conforme relato | 18 mulheres e 78 homens                                                                  |
| Idade                 | Média de 75,5 anos; desvio-padrão de 9,9                                                 |
| Período de coleta     | Novembro de 2021 a agosto de 2023, descrito como 1 ano e 9 meses                         |
| Aquisição             | Profissionais de saúde com câmeras de smartphones durante sessões de cuidado das feridas |
| Local anatômico       | Úlceras crônicas nos membros inferiores; imagens focadas na ferida, sem rosto            |
| Treinamento           | 485 imagens, com anotações                                                               |
| Validação             | 122 imagens, com anotações                                                               |
| Teste                 | 157 imagens, descritas como **sem rótulos**                                              |
| Formatos              | RGB; anotações COCO e máscaras binárias de ferida/fundo nos conjuntos rotulados          |


Há imagens da mesma ferida em momentos distintos na plataforma. **Não localizei o número de feridas únicas**, distribuição de imagens por paciente ou detalhamento de separação dos pacientes entre subconjuntos. Imagens, feridas e pacientes são unidades diferentes.

**Inconsistência numérica:** resumo/descrição/conclusão e soma dos splits indicam **764** imagens; a curadoria e a anotação indicam **746**. A diferença é de 18 imagens. O total rotulado de **607 = 485 + 122** é consistente. Entretanto, **746 − 607 = 139**, não os 157 do teste declarado. Registrar ambas as contagens e sua origem, sem corrigir a divergência silenciosamente.

**Disponibilidade declarada:** dataset público no Mendeley Data, versão 2, DOI **10.17632/s2w7rjwz49.2**, sob licença **CC BY-NC-ND**, segundo o artigo. Código de avaliação indicado no GitHub. Endereços transcritos, sem verificação externa nesta análise:

*   Dataset: https\://data.mendeley.com/datasets/s2w7rjwz49/2
*   Código: https\://github.com/simatec-uis/CO2Wounds-V2

O PDF remete a instruções de download em material suplementar, que não está incluído nas sete páginas fornecidas. Não foi realizada auditoria do conteúdo baixável ou da licença online atual.

O artigo relata consentimento informado, anonimização e aprovação pelos comitês do Sanatorio de Contratación ESE (Act 05–21) e da Universidad Industrial de Santander (Act No. 19-13/11/20). Esses elementos são relatos dos autores, não verificação independente.

**Evidências:** páginas 1–5, seções 2 e 5; anotações 02–11.

## RQ3 — Quais métodos, procedimentos são utilizados para avaliar o desempenho desses modelos e quais resultados são reportados?

**Resposta:** benchmark interno de segmentação, com partições declaradas de **485 treino / 122 validação / 157 teste**. Os modelos são treinados por **100 épocas**, com otimizador **Adam** e encoders pré-treinados no ImageNet. O artigo usa PyTorch/SMP e métricas de segmentação, além de seis exemplos qualitativos de validação na Figura 2.

**Cuidado com o conjunto de avaliação:** o split de teste é explicitamente descrito como **não rotulado**. A Figura 2 é de validação, mas o texto não liga inequivocamente todas as métricas da Tabela 1 a esse conjunto. Portanto, registrar os resultados como **benchmark interno com subconjunto quantitativo não explicitado com clareza**, sem afirmar que são resultados obtidos nas 157 imagens de teste. O PDF não descreve um servidor de avaliação ou máscaras de teste ocultas utilizadas para esses números.

Não localizei validação cruzada, múltiplas execuções, sementes, desvios-padrão de desempenho, intervalos de confiança ou testes de significância. Também faltam detalhes de learning rate, batch size, função de perda, variante exata de alguns encoders, seleção de checkpoint e configuração completa de agregação das métricas. Há código indicado, mas não auditado nesta leitura.

**Resultados de destaque:** maior mIoU **70,13%** com U-Net/SegFormer; maior F1 **79,44%** e maior accuracy por pixel **98,65%** com U-Net/ResNeXt-50. As 12 configurações são transcritas na RQ4. A diferença de mIoU entre essas duas U-Nets é de **0,19 ponto percentual**, sem evidência de significância estatística apresentada.

A plataforma admite acompanhamento longitudinal. Não há descrição de divisão por paciente/ferida, de modo que a independência das imagens entre splits não pode ser confirmada. A remoção de duplicatas não resolve necessariamente a correlação entre fotografias distintas da mesma ferida. Isso é uma limitação do relato, **não comprovação de vazamento**.

**Evidências:** páginas 2, 4–5; seções 3.1–3.3 e Tabela 1; anotações 02–05, 07–09 e 12–30.

## RQ4 — Quais métricas são utilizadas para avaliar o desempenho desses modelos e quais resultados são reportados?

**Resposta:** **mIoU, F1, accuracy, precision e recall**, todos para **segmentação por pixel**, calculados com SMP. Não são métricas de diagnóstico de hanseníase em pacientes. Não localizei AUC ROC, especificidade, métricas de fronteira, erros de área/perímetro ou resultados clínicos como endpoints dos baselines.

Valores da **Tabela 1, página 5 do PDF / página impressa 73**, em porcentagem:

| Arquitetura | Encoder      | mIoU      | F1        | Accuracy  | Precision | Recall    |
| ----------- | ------------ | --------- | --------- | --------- | --------- | --------- |
| DeepLabV3   | ResNeXt-50   | 68,48     | 77,86     | 98,58     | **85,81** | 78,20     |
| DeepLabV3+  | ResNeXt-50   | 68,23     | 78,04     | 98,51     | 81,61     | 81,69     |
| U-Net       | ResNeXt-50   | 69,94     | **79,44** | **98,65** | 84,35     | 80,31     |
| FPN         | ResNeXt-50   | 68,99     | 78,36     | 98,53     | 82,94     | 81,17     |
| DeepLabV3+  | ResNet-101   | 66,88     | 76,55     | 98,40     | 83,04     | 79,02     |
| U-Net       | ResNet-101   | 66,96     | 76,61     | 98,28     | 80,87     | 81,10     |
| FPN         | ResNet-101   | 66,81     | 76,52     | 98,45     | 81,78     | 79,61     |
| DeepLabV3+  | EfficientNet | 66,98     | 76,78     | 98,49     | 79,88     | 81,86     |
| U-Net       | EfficientNet | 67,71     | 77,20     | 98,51     | 83,29     | 77,80     |
| FPN         | EfficientNet | 67,49     | 76,84     | 98,59     | 82,63     | 80,34     |
| U-Net       | SegFormer    | **70,13** | 79,26     | 98,59     | 84,70     | 81,99     |
| FPN         | SegFormer    | 69,90     | 79,36     | 98,56     | 82,02     | **84,35** |


**Negrito nesta tabela:** maior valor numérico de cada coluna, identificado nesta leitura, independentemente dos destaques tipográficos do PDF.

**Interpretação:**

*   Não existe uma configuração que maximize todas as métricas. U-Net lidera mIoU e F1 com **encoders diferentes**.
*   Accuracy próxima de 98,6% conta pixels de fundo e ferida; pode ser favorecida pela quantidade de fundo. Não significa diagnóstico de hanseníase com 98,6% de acerto.
*   Recall por pixel não é sensibilidade para detectar pacientes com hanseníase.
*   Os modos de redução/agregação entre classes e imagens não são suficientemente especificados. F1 tabulado pode diferir da média harmônica calculada diretamente sobre precision/recall já agregados; a diferença isolada não demonstra erro.
*   Não há resultados por paciente, tom de pele ou grupos demográficos, nem intervalos que permitam quantificar a incerteza dos rankings.

**Evidências:** página 4, seção 3.1; página 5, Tabela 1; anotações 12–13 e 19–30.

## RQ5 — Como o desempenho dos modelos varia entre diferentes grupos ou tons de pele?

**Resposta:** **não é possível determinar pelo artigo**. Há caracterização da população por sexo, idade e local de coleta, mas não há análise de desempenho estratificada por sexo/idade, tom de pele ou outro grupo. Não localizei Fitzpatrick/Monk, distribuição por tom, métricas de equidade ou comparação quantitativa entre tons.

As imagens ilustrativas e a origem colombiana não permitem inferir a composição de tons de pele nem generalizar desempenho entre grupos. A população é predominantemente masculina e idosa segundo os dados apresentados, mas não há resultado comparativo que mostre o efeito dessas características.

**Registro sugerido:** “População descrita: 96 pacientes, 18 mulheres/78 homens, idade 75,5 ± 9,9 anos, Colômbia; desempenho por grupo/tom de pele não reportado.”

**Evidências:** página 2, seção 2.1, e páginas 4–5, avaliação; anotação 04. A ausência de análise não foi transformada em grifo afirmativo inexistente.

## RQ6 — Quais modelos e abordagens de inteligência artificial são utilizados para identificar manifestações dermatológicas associadas à hanseníase?

**Resposta:** aprendizado profundo supervisionado para segmentação semântica, utilizando arquiteturas **U-Net, FPN, DeepLabV3+ e DeepLabV3** com encoders pré-treinados. A Tabela 1 contém **12 configurações**:

*   ResNeXt-50: DeepLabV3, DeepLabV3+, U-Net e FPN.
*   ResNet-101: DeepLabV3+, U-Net e FPN.
*   EfficientNet: DeepLabV3+, U-Net e FPN.
*   SegFormer: U-Net e FPN, listado como **encoder** no artigo.

A seção 3.2 enumera três arquiteturas (FPN, U-Net, DeepLabV3+), mas a tabela inclui também DeepLabV3. Registrar a tabela completa sem omitir essa linha. Os pesos são descritos como pré-treinados no ImageNet; não tratar ImageNet como teste externo de hanseníase.

O trabalho estabelece baselines para um dataset, em vez de propor um classificador diagnóstico novo. O uso de SegFormer na coluna Encoder deve ser preservado como configuração reportada, sem inferir uma variante não especificada ou avaliação de SegFormer isolado. Não foi identificada explicabilidade por mapas de saliência, nem comparação com avaliação diagnóstica humana.

**Evidências:** páginas 4–5, seção 3.2 e Tabela 1; anotações 14–15 e 19–30.

## RQ7 — Como a capacidade de generalização dos modelos é avaliada, especialmente quando são utilizados conjuntos de dados diferentes daqueles empregados no treinamento?

**Resposta:** **não localizei validação externa/cross-dataset**. Os experimentos apresentados usam o CO2Wounds-V2, de um único centro colombiano, com partições internas. A existência de split de teste sem rótulos não comprova teste quantitativo externo nem resultado em outra população.

A introdução discute queda de desempenho entre centros/populações como motivação, com referências a trabalhos anteriores. Isso não é um experimento de transferência de domínio conduzido neste artigo. Imagens obtidas com smartphones e variação de aparência tornam o dataset potencialmente útil para pesquisa, mas não demonstram generalização entre dispositivos, hospitais, tons de pele ou etiologias de feridas.

Não há comparação de treino em CO2Wounds-V2 e teste em feridas diabéticas ou outro dataset, nem validação prospectiva de benefício clínico. Também não está explicitada separação por paciente ou ferida, importante porque existem imagens longitudinais correlacionadas.

**Registro sugerido:** “Benchmark interno; conjunto quantitativo não explicitado com clareza; teste disponibilizado sem rótulos; validação externa/cross-dataset não localizada.”

**Evidências:** páginas 1–2 e 4–5; anotações 03, 05, 16–18. Disponibilizar dados/código facilita avaliações futuras, mas não significa que essas avaliações já ocorreram.

## RQ8 — O artigo foi publicado em que tipo de veículo de publicação? (revista, conferência)

**Resposta:** **conferência** — *2024 IEEE International Conference on Image Processing (ICIP)*, IEEE, páginas **69–75**, ano **2024**. DOI **10.1109/ICIP51287.2024.10647641**. O evento e o DOI constam na margem editorial da primeira página; o rodapé também indica “ICIP 2024”.

A referência \[19], publicada em *Computers in Biology and Medicine* em 2023, descreve trabalho anterior relacionado à plataforma. Ela não é o veículo do presente artigo.

**Evidência:** página 1 e paginação impressa 69–75; anotação 31.

## Síntese para a ficha de extração

*   **Tarefa:** segmentação de feridas crônicas de pacientes com hanseníase; não diagnóstico da doença.
*   **Dataset/população:** total declarado 764 imagens, 96 pacientes, Colômbia; curadoria cita 746, divergência preservada.
*   **Splits:** 485/122/157; 607 imagens rotuladas no treino/validação; teste sem rótulos.
*   **Melhores resultados por métrica:** mIoU 70,13% (U-Net/SegFormer); F1 79,44% e accuracy por pixel 98,65% (U-Net/ResNeXt-50).
*   **Tons de pele:** não avaliados quantitativamente. **Generalização externa:** não localizada.

# Trechos e notas para o Zotero

Cada número corresponde a uma anotação no PDF. Os trechos textuais abaixo são literais, com quebras de linha/hifenização de fim de linha normalizadas. A última entrada é uma marcação de área na margem editorial vertical, com transcrição do nome do evento e DOI. Nas linhas de tabela, a ordem dos valores é mIoU, F1, Accuracy, Precision e Recall, todos em %. Os comentários podem ser copiados diretamente para o Zotero.

## 01. Tipo de estudo e tarefa

**Página 1 · Resumo**

**Trecho grifado:**

> This paper introduces the CO2Wounds-V2 dataset, an extended collection of RGB wound images from leprosy patients with their corresponding semantic segmentation annotations, aiming to enhance the development and testing of image-processing algorithms in the medical field.

**Comentário:**

Tipo de estudo: apresentação de dataset com avaliação experimental de baselines. RQ1/RQ6 — Segmentação semântica de feridas crônicas em pacientes com hanseníase. Não é diagnóstico/classificação da hanseníase, diferenciação entre doenças ou classificação de gravidade. Os resultados avaliam delimitação de ferida versus fundo, não sensibilidade diagnóstica de hanseníase.

## 02. Tamanho e divisão declarada

**Página 2 · 2.1. Dataset description**

**Trecho grifado:**

> In this paper, we present the latest version, which includes 764 RGB images, divided as follows: 485 for training, 122 for validation, and 157 for testing.

**Comentário:**

RQ2/RQ3 — Total declarado: 764 imagens RGB; 485 treinamento, 122 validação, 157 teste (soma 764). A curadoria/anotação menciona 746 imagens, em divergência. A versão inicial tinha 164 imagens; não somar 164 a 764. Não confundir imagens com pacientes ou feridas distintas.

## 03. Rótulos e teste sem anotações

**Página 2 · 2.1**

**Trecho grifado:**

> The first two sets of this new dataset contain, in addition to the RGB images, their wound annotation labels in COCO format, and binary semantic segmentation masks (wound and background), while the testing split is a collection of unlabeled images.

**Comentário:**

RQ1/RQ2/RQ3 — Treino e validação contêm anotações COCO e máscaras binárias de ferida/fundo. O split de teste é descrito como não rotulado. Assim, não atribuir automaticamente as métricas da Tabela 1 ao teste de 157 imagens. O artigo mostra exemplos da validação, mas não explicita de modo inequívoco o subconjunto usado para todas as métricas tabuladas.

## 04. População e aquisição

**Página 2 · 2.1**

**Trecho grifado:**

> The images in this dataset were captured by the Leprosy Program control team from the Sanatorio de Contratación ESE in Colombia during routine wound healing sessions. For 1 year and 9 months from November 2021 to August 2023, images were collected from 96 consenting patients including 18 females and 78 males by medical staff, through smartphone cameras. The average age of the participants in this study is 75.5 years old, with a standard deviation of 9.9 years.

**Comentário:**

RQ2/RQ5 — 96 pacientes com hanseníase, no Sanatorio de Contratación ESE, Colômbia; 18 mulheres e 78 homens; idade média 75,5 anos (DP 9,9). Coleta por profissionais com smartphones, de novembro/2021 a agosto/2023. Não são informados tons de pele, classificação Fitzpatrick/Monk ou desempenho por sexo/idade. País e composição demográfica não permitem inferir tons de pele.

## 05. Imagens longitudinais de uma mesma ferida

**Página 2 · 2.2.1. Data collection**

**Trecho grifado:**

> The wound is the fundamental module of the platform, from within each wound module, medical staff can upload images at different stages and times of the lesion.

**Comentário:**

RQ2/RQ3/RQ7 — A plataforma permite imagens longitudinais da mesma ferida. Não localizei número de feridas únicas nem descrição de particionamento por paciente/ferida. Fotos repetidas ao longo do tempo podem ser correlacionadas; a ausência de agrupamento documentado limita avaliar independência do holdout, mas não prova vazamento efetivo.

## 06. Plataforma anterior e medidas

**Página 2 · 2.2.1**

**Trecho grifado:**

> The nurse will then be able to see within the platform a visual comparison of the original and the segmented wound with the metrics of area and perimeter obtained by the algorithm.

**Comentário:**

RQ1/RQ6 — A plataforma já apresentada em \[19] calcula segmentação, área e perímetro para acompanhamento. Neste artigo, a contribuição principal é o dataset e seu benchmark. Não foram localizados erros quantitativos de área/perímetro ou avaliação de desfechos clínicos para os baselines atuais; não confundir funcionalidades da plataforma com métricas comprovadas neste experimento.

## 07. Curadoria

**Página 2 · 2.2.2. Data curation**

**Trecho grifado:**

> This step included deleting duplicated images, images that do not contain wounds, and blurring images where the edges of the ulcer are difficult to detect.

**Comentário:**

RQ1/RQ2/RQ3 — Curadoria menciona exclusão de duplicatas e imagens sem feridas. A expressão blurring images where the edges of the ulcer are difficult to detect é ambígua; não registrar isso como aumento por desfoque implementado. A remoção de duplicatas não demonstra separação de todas as imagens do mesmo paciente/ferida entre os splits.

## 08. Total divergente e recorte

**Página 2 · 2.2.2**

**Trecho grifado:**

> After that, 746 photographs remained, and all of them were then cropped to a 4:3 aspect ratio.

**Comentário:**

RQ1/RQ2 — Recorte das imagens para proporção 4:3. O total após curadoria é 746 aqui, enquanto resumo/descrição/conclusão e soma dos splits indicam 764. Registrar a divergência de 18 imagens; não corrigir para 764 silenciosamente. Não são informadas aqui resolução de entrada das redes, normalização ou aumento de dados.

## 09. Anotação manual e quantidade rotulada

**Página 2 · 2.2.3. Annotation**

**Trecho grifado:**

> With the curated 746 images, we meticulously delineated the wound outlines on 607 of them through the Computer Vision Annotation Tool to form the training and validation sets.

**Comentário:**

RQ1/RQ2/RQ3 — Contornos de feridas delineados no CVAT em 607 imagens, correspondentes a 485+122 de treino/validação; anotações em COCO e imagens. Se o total fosse 746, restariam 139 sem anotação, diferente do teste declarado de 157. O artigo não detalha número/qualificação dos anotadores, concordância interobservador ou revisão independente das máscaras.

## 10. Local anatômico e privacidade

**Página 3 · 2.3.2. Beneficence**

**Trecho grifado:**

> Health professionals acquire photographs of chronic ulcers present in the lower extremities, focusing only on the area in which the ulcer occurs, without photographing the patient’s face at any time.

**Comentário:**

RQ2 — Fotografias de úlceras crônicas nos membros inferiores, focadas na região da ferida, sem rosto. O conjunto representa feridas em pacientes com hanseníase, não necessariamente todo o espectro de manifestações cutâneas usadas para diagnosticar a doença.

## 11. Disponibilidade e licença declarada

**Página 4 · 2.4. License**

**Trecho grifado:**

> The authors make data publicly available according to open data standards and license datasets under the Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND) license

**Comentário:**

RQ2 — Dataset descrito como público no Mendeley Data, versão 2, com licença CC BY-NC-ND. DOI do dataset: 10.17632/s2w7rjwz49.2. Código de avaliação indicado: https\://github.com/simatec-uis/CO2Wounds-V2. Esta nota transcreve disponibilidade/licença declaradas no artigo, sem auditoria do repositório ou da versão online atual.

## 12. Métricas por pixel

**Página 4 · 3.1. Metrics**

**Trecho grifado:**

> Accuracy measures the proportion of correctly classified pixels across the entire dataset. Precision assesses the ability of the model to accurately predict positive pixels, while recall focuses on the capability of the model to identify all relevant pixels in the ground truth.

**Comentário:**

RQ4 — Accuracy, precision e recall são métricas de segmentação por pixel, acompanhadas de mIoU e F1. Accuracy próxima de 98,6% não é acurácia diagnóstica de hanseníase. Pode ser influenciada pela proporção de fundo; observar também mIoU/F1. O artigo não explicita suficientemente a redução/agregação entre imagens e classes.

## 13. Biblioteca de métricas

**Página 4 · 3.1**

**Trecho grifado:**

> The reported metrics were computed using the implementation provided by SMP library

**Comentário:**

RQ3/RQ4 — Métricas calculadas com Segmentation Models PyTorch (SMP). Não localizei especificação completa do modo de agregação, limiar de binarização ou tratamento de classes/imagens sem pixels positivos. F1 tabulado não precisa coincidir com a média harmônica dos valores agregados de precision/recall; não declarar erro apenas por essa diferença.

## 14. Treinamento e encoders

**Página 4 · 3.2. Baseline Performance**

**Trecho grifado:**

> All the networks were trained during 100 epochs using the Adam optimizer. Different encoders with Imagenet pre-trained weights were used to evaluate the architecture’s performance on our proposed dataset, including ResNeXt-50, ResNet-101, EfficientNet, and SegFormer.

**Comentário:**

RQ3/RQ6 — Treinamento de 100 épocas, Adam, encoders com pesos pré-treinados no ImageNet: ResNeXt-50, ResNet-101, EfficientNet e SegFormer, conforme o artigo. Não localizei learning rate, batch size, função de perda, sementes/repetições ou detalhes completos das variantes. ImageNet é fonte de pré-treinamento, não teste externo de feridas.

## 15. Arquiteturas de segmentação

**Página 4 · 3.2**

**Trecho grifado:**

> For this purpose, we use PyTorch \[22] alongside the Segmentation Models PyTorch Library (SMP) \[21] for performing wound semantic segmentation on our dataset.

**Comentário:**

RQ1/RQ6 — Arquiteturas explicitadas na metodologia: FPN, U-Net e DeepLabV3+. A Tabela 1 também inclui DeepLabV3 com ResNeXt-50. Preservar essa diferença de enumeração e distinguir arquitetura de segmentação de encoder. SegFormer é listado na coluna Encoder; não aparece como detector/classificador independente.

## 16. Conjunto dos exemplos qualitativos

**Página 4 · Legenda da Figura 2**

**Trecho grifado:**

> Random samples from the validation set of our CO2Wounds-V2 dataset (Column 1), ground truth segmentation masks (Column 2), and segmentation results using U-Net architecture (Column 3).

**Comentário:**

RQ3/RQ4 — A Figura 2 mostra seis exemplos do conjunto de validação, máscaras de referência e predições U-Net. São resultados qualitativos internos, sem validação clínica ou teste entre datasets. Essa legenda não basta para afirmar que toda a Tabela 1 foi calculada na validação, pois o texto não amarra explicitamente o split das métricas.

## 17. Objetivo de benchmark

**Página 5 · 3.3. Results and Discussions**

**Trecho grifado:**

> As this paper primarily focuses on introducing and providing a benchmark dataset, we anticipate that future researchers will build upon our work to further enhance the segmentation results.

**Comentário:**

RQ3/RQ7 — O foco declarado é apresentação de dataset e baselines para futuras pesquisas. Não localizei experimento com outro dataset, outro centro clínico, outra população ou teste prospectivo de benefício clínico. Expectativa de uso futuro não comprova generalização externa.

## 18. Generalização discutida, não testada externamente

**Página 1 · 1. Introduction**

**Trecho grifado:**

> This typical overfitting of deep learning segmentation methods to specific data domains \[16] suggests lower performance when tested on data from different clinical centers or populations, due to substantial differences in wound features, etiology, and image acquisition protocols.

**Comentário:**

RQ7 — Mudança de domínio entre centros/populações é discutida como motivação, apoiada em trabalhos anteriores. Não é resultado de teste externo executado neste artigo. Os baselines relatados usam CO2Wounds-V2; não foi localizada validação cross-dataset.

## 19. DeepLabV3 / ResNeXt-50

**Página 5 · Tabela 1**

**Trecho grifado:**

> DeepLabV3 ResNeXt-50 68.48 77.86 98.58 85.81 78.20

**Comentário:**

RQ3/RQ4/RQ6 — DeepLabV3 com encoder ResNeXt-50: mIoU 68.48%; F1 77.86%; accuracy por pixel 98.58%; precision 85.81%; recall 78.20%, conforme Tabela 1. Métricas de segmentação de ferida/fundo, não de diagnóstico de hanseníase. Maior precision da tabela (85,81%). Esta arquitetura aparece na tabela, embora a lista de três arquiteturas da seção 3.2 mencione DeepLabV3+.

## 20. DeepLabV3+ / ResNeXt-50

**Página 5 · Tabela 1**

**Trecho grifado:**

> DeepLabV3+ ResNeXt-50 68.23 78.04 98.51 81.61 81.69

**Comentário:**

RQ3/RQ4/RQ6 — DeepLabV3+ com encoder ResNeXt-50: mIoU 68.23%; F1 78.04%; accuracy por pixel 98.51%; precision 81.61%; recall 81.69%, conforme Tabela 1. Métricas de segmentação de ferida/fundo, não de diagnóstico de hanseníase.

## 21. U-Net / ResNeXt-50

**Página 5 · Tabela 1**

**Trecho grifado:**

> U-Net ResNeXt-50 69.94 79.44 98.65 84.35 80.31

**Comentário:**

RQ3/RQ4/RQ6 — U-Net com encoder ResNeXt-50: mIoU 69.94%; F1 79.44%; accuracy por pixel 98.65%; precision 84.35%; recall 80.31%, conforme Tabela 1. Métricas de segmentação de ferida/fundo, não de diagnóstico de hanseníase. Maior F1 (79,44%) e maior accuracy (98,65%) da tabela; o maior mIoU pertence a U-Net/SegFormer. Não há uma única configuração vencedora em todas as métricas.

## 22. FPN / ResNeXt-50

**Página 5 · Tabela 1**

**Trecho grifado:**

> FPN ResNeXt-50 68.99 78.36 98.53 82.94 81.17

**Comentário:**

RQ3/RQ4/RQ6 — FPN com encoder ResNeXt-50: mIoU 68.99%; F1 78.36%; accuracy por pixel 98.53%; precision 82.94%; recall 81.17%, conforme Tabela 1. Métricas de segmentação de ferida/fundo, não de diagnóstico de hanseníase.

## 23. DeepLabV3+ / ResNet-101

**Página 5 · Tabela 1**

**Trecho grifado:**

> DeepLabV3+ ResNet-101 66.88 76.55 98.40 83.04 79.02

**Comentário:**

RQ3/RQ4/RQ6 — DeepLabV3+ com encoder ResNet-101: mIoU 66.88%; F1 76.55%; accuracy por pixel 98.40%; precision 83.04%; recall 79.02%, conforme Tabela 1. Métricas de segmentação de ferida/fundo, não de diagnóstico de hanseníase.

## 24. U-Net / ResNet-101

**Página 5 · Tabela 1**

**Trecho grifado:**

> U-Net ResNet-101 66.96 76.61 98.28 80.87 81.10

**Comentário:**

RQ3/RQ4/RQ6 — U-Net com encoder ResNet-101: mIoU 66.96%; F1 76.61%; accuracy por pixel 98.28%; precision 80.87%; recall 81.10%, conforme Tabela 1. Métricas de segmentação de ferida/fundo, não de diagnóstico de hanseníase.

## 25. FPN / ResNet-101

**Página 5 · Tabela 1**

**Trecho grifado:**

> FPN ResNet-101 66.81 76.52 98.45 81.78 79.61

**Comentário:**

RQ3/RQ4/RQ6 — FPN com encoder ResNet-101: mIoU 66.81%; F1 76.52%; accuracy por pixel 98.45%; precision 81.78%; recall 79.61%, conforme Tabela 1. Métricas de segmentação de ferida/fundo, não de diagnóstico de hanseníase.

## 26. DeepLabV3+ / EfficientNet

**Página 5 · Tabela 1**

**Trecho grifado:**

> DeepLabV3+ EfficientNet 66.98 76.78 98.49 79.88 81.86

**Comentário:**

RQ3/RQ4/RQ6 — DeepLabV3+ com encoder EfficientNet: mIoU 66.98%; F1 76.78%; accuracy por pixel 98.49%; precision 79.88%; recall 81.86%, conforme Tabela 1. Métricas de segmentação de ferida/fundo, não de diagnóstico de hanseníase.

## 27. U-Net / EfficientNet

**Página 5 · Tabela 1**

**Trecho grifado:**

> U-Net EfficientNet 67.71 77.20 98.51 83.29 77.80

**Comentário:**

RQ3/RQ4/RQ6 — U-Net com encoder EfficientNet: mIoU 67.71%; F1 77.20%; accuracy por pixel 98.51%; precision 83.29%; recall 77.80%, conforme Tabela 1. Métricas de segmentação de ferida/fundo, não de diagnóstico de hanseníase.

## 28. FPN / EfficientNet

**Página 5 · Tabela 1**

**Trecho grifado:**

> FPN EfficientNet 67.49 76.84 98.59 82.63 80.34

**Comentário:**

RQ3/RQ4/RQ6 — FPN com encoder EfficientNet: mIoU 67.49%; F1 76.84%; accuracy por pixel 98.59%; precision 82.63%; recall 80.34%, conforme Tabela 1. Métricas de segmentação de ferida/fundo, não de diagnóstico de hanseníase.

## 29. U-Net / SegFormer

**Página 5 · Tabela 1**

**Trecho grifado:**

> U-Net SegFormer 70.13 79.26 98.59 84.70 81.99

**Comentário:**

RQ3/RQ4/RQ6 — U-Net com encoder SegFormer: mIoU 70.13%; F1 79.26%; accuracy por pixel 98.59%; precision 84.70%; recall 81.99%, conforme Tabela 1. Métricas de segmentação de ferida/fundo, não de diagnóstico de hanseníase. Maior mIoU (70,13%) da tabela. O F1 máximo é 79,44% em U-Net/ResNeXt-50. Sem repetições/intervalos reportados, a diferença de 0,19 ponto percentual de mIoU não comprova superioridade estatística.

## 30. FPN / SegFormer

**Página 5 · Tabela 1**

**Trecho grifado:**

> FPN SegFormer 69.90 79.36 98.56 82.02 84.35

**Comentário:**

RQ3/RQ4/RQ6 — FPN com encoder SegFormer: mIoU 69.90%; F1 79.36%; accuracy por pixel 98.56%; precision 82.02%; recall 84.35%, conforme Tabela 1. Métricas de segmentação de ferida/fundo, não de diagnóstico de hanseníase. Maior recall da tabela (84,35%). Não converter recall por pixel em sensibilidade para diagnosticar pacientes.

## 31. Veículo de publicação

**Página 1 · Margem editorial e rodapé**

**Rótulos da área marcada:**

> 2024 IEEE International Conference on Image Processing (ICIP) DOI: 10.1109/ICIP51287.2024.10647641

**Comentário:**

RQ8 — Conferência: 2024 IEEE International Conference on Image Processing (ICIP), IEEE, páginas 69–75. DOI 10.1109/ICIP51287.2024.10647641. Não é artigo de revista. A referência ao estudo anterior em Computers in Biology and Medicine corresponde à referência \[19], não ao veículo deste artigo.
