---
tags: []
parent: 'Independent assessment of the WHO Skin Neglected Tropical Diseases application for leprosy detection'
collections:
    - TCC_Leituras
$version: 305
$libraryID: 2
$itemKey: 9G2Q4H2K

---
# Deps et al. (2026) — RQs e anotações

**Título:** *Independent assessment of the WHO Skin Neglected Tropical Diseases application for leprosy detection*.\
**Primeira autora:** Patrícia Deps.\
**Publicação:** *Revista Panamericana de Salud Pública / Pan American Journal of Public Health*, 2026;50:e40.\
**DOI:** 10.26633/RPSP.2026.40.\
**Registro OPAS:** https\://iris.paho.org/handle/10665.2/71104 (data registrada: 16/04/2026).\
**PDF analisado:** https\://iris.paho.org/bitstreams/4fb0c2ef-3958-4132-856c-f4ad2135109d/download.

O arquivo fornecido pelo usuário era uma página HTML do repositório, com metadados e resumos. O PDF completo vinculado nessa página foi obtido da OPAS para esta análise. As páginas citadas abaixo correspondem às oito páginas do PDF, não ao HTML.

**Tipo de estudo:** pesquisa original de validação analítica externa e retrospectiva de um classificador pré-treinado. Não desenvolve um novo modelo. Avalia exclusivamente o **segundo estágio (classificador de NTDs)**, pela versão desktop; não o fluxo completo do aplicativo móvel.

Foram preparados **20 grifos com comentários** e as oito RQs abaixo. O HTML original foi preservado. As anotações estão na cópia PDF, sem inserção direta no banco de dados do Zotero. O último bloco deste documento contém os trechos exatos grifados, páginas e comentários.

## RQ1. Quais técnicas de visão computacional são utilizadas para identificar manifestações dermatológicas associadas à hanseníase?

A ferramenta usa **classificação de imagens clínicas por redes neurais convolucionais (CNNs)**. O aplicativo beta tem dois classificadores em cascata: o primeiro funciona como triagem de condições dermatológicas gerais; o segundo atribui probabilidades a **12 categorias de NTDs cutâneas**. Todas as análises deste artigo se referem ao segundo estágio (p. 2; grifos 2–3).

As imagens de teste foram anonimizadas por **recorte manual e mascaramento seletivo** de identificadores, preservando a lesão. Rótulos e metadados foram mantidos separadamente e não fornecidos como entrada ao modelo. Esse recorte tem finalidade de privacidade; não é evidência de segmentação automática de ROI. Não são descritos parâmetros técnicos de redimensionamento, normalização, aumento de dados ou extração de atributos do modelo avaliado (p. 2–3; grifo 8).

O texto sugere **segmentação focada na lesão e inclusão de contexto multimodal/do paciente** como trabalhos futuros. Essas técnicas não foram implementadas nesta avaliação. Também não há aplicação de Grad-CAM, LIME ou SHAP (p. 5; grifo 18).

## RQ2. Quais conjuntos de dados e populações são utilizados no desenvolvimento e na avaliação desses modelos?

Foi construída uma base externa com **439 imagens clínicas anonimizadas de 208 casos confirmados**, coletadas por especialistas entre **1996 e 2024**. Alguns casos contribuíram com múltiplas fotografias de lesões ou locais anatômicos. **A unidade de análise é a imagem**, não o paciente. Após excluir **16 imagens por erros de processamento**, foram analisadas **423** (p. 2–4; grifos 4–6):

| Subconjunto | Imagens analisadas | Conteúdo                                                         |
| ----------- | ------------------ | ---------------------------------------------------------------- |
| 1           | 367                | Lesões clássicas de hanseníase                                   |
| 2           | 56                 | Reações e apresentações raras/atípicas relacionadas à hanseníase |
| **Total**   | **423**            | Somente casos positivos; sem grupo não hanseníase                |


A base abrange formas indeterminada, tuberculoide, borderline/dimorfa e lepromatosa/virchowiana. O subconjunto 2 inclui reações tipos 1/2 e apresentações como fenômeno de Lúcio e lesões semelhantes a eritema multiforme, sem avaliação separada de cada subtipo. Não é informado quantos pacientes únicos permanecem após as exclusões.

O padrão de referência foi diagnóstico por clínicos experientes segundo critérios da OMS. Exames como histopatologia, PCR para *M. leprae*, sorologia anti-PGL-1 ou ultrassom de nervos podiam apoiar o diagnóstico quando indicados, mas o registro histórico é incompleto. **Não afirmar que todos os casos foram confirmados laboratorialmente ou por PCR** (p. 3; grifo 9).

Há metadados disponíveis para **418 imagens: 362/367 no subconjunto 1 e 56/56 no subconjunto 2**. Isso explica os denominadores da Tabela 1; não é inconsistência com o total de imagens analisadas. Ainda existem valores ausentes dentro desses registros.

**Tabela 1 — contagens de registros de imagens, não pacientes únicos:**

| Característica       | Clássicas, n=362 | Reacionais/atípicas, n=56 |
| -------------------- | ---------------- | ------------------------- |
| Masculino            | 206 (56,9%)      | 51 (91,1%)                |
| Feminino             | 118 (32,6%)      | 5 (8,9%)                  |
| Sexo ausente         | 38 (10,5%)       | 0                         |
| Adultos              | 315 (87,0%)      | 55 (98,2%)                |
| Adolescentes         | 40 (11,0%)       | 0                         |
| Crianças             | 6 (1,7%)         | 1 (1,8%)                  |
| Faixa etária ausente | 1 (0,3%)         | 0                         |
| Fitzpatrick II       | 4 (1,1%)         | 4 (7,1%)                  |
| Fitzpatrick III      | 190 (52,5%)      | 36 (64,3%)                |
| Fitzpatrick IV       | 67 (18,5%)       | 5 (8,9%)                  |
| Fitzpatrick V        | 60 (16,6%)       | 0                         |
| Fitzpatrick VI       | 41 (11,3%)       | 4 (7,1%)                  |
| Fototipo ausente     | 0                | 7 (12,5%)                 |


Fototipo I não foi observado entre registros com informação. Sexo e fototipo não foram inferidos das fotos. Os 5 registros totalmente ausentes do subconjunto 1 não entram no denominador 362 (grifo 7).

A descrição não permite determinar a distribuição completa por país/centro de origem ou câmera; afiliações dos autores não substituem essa informação. Os dados são de acesso controlado e disponíveis **mediante solicitação razoável ao autor correspondente**, sem repositório público de imagens informado (p. 6; grifo 19).

## RQ3. Quais métodos, procedimentos são utilizados para avaliar o desempenho desses modelos e quais resultados são reportados?

É uma **validação externa retrospectiva**, utilizando base declarada independente do treinamento e da validação interna. Não há nova divisão treino/teste, retreinamento ou ajuste dos pesos pelos avaliadores. O teste fornece imagens sem seus rótulos/metadados, e compara as sugestões com os diagnósticos confirmados (p. 2–4; grifos 1 e 8–10).

O desfecho primário é **sensibilidade Top-5**, ou seja, presença de “leprosy” em qualquer uma das cinco primeiras sugestões. Foram avaliados também **Top-1 a Top-5** e diferenças entre os dois subconjuntos. A análise usou R 4.2.1, frequências e percentuais. Não são apresentados intervalos de confiança, testes de significância ou ajuste estatístico para múltiplas imagens do mesmo paciente.

A análise qualitativa examina inconsistências intrapaciente e erros em lesões necróticas, inflamatórias e infiltrativas. Foram observadas imagens semelhantes do mesmo caso com saídas divergentes; os exemplos não equivalem a taxas quantitativas por morfologia (p. 4; grifo 14).

A sensibilidade Top-5 foi **84,9% global**, **87,2% nas clássicas** e **69,6% nas reacionais/atípicas**. Entretanto, o aplicativo móvel normalmente exibe **quatro** sugestões e o estudo acessou **cinco** pela versão desktop. Os resultados não medem o fluxo móvel completo nem o desempenho da cascata incluindo a primeira triagem (grifo 3).

As 16 exclusões correspondem a aproximadamente **3,6% das 439 imagens iniciais** (cálculo). Os resultados são condicionais às 423 imagens processadas; causas e distribuição dos erros não são detalhadas. Não houve avaliação prospectiva de fluxo clínico, impacto assistencial ou comparação direta com profissionais (grifos 6, 16–17).

## RQ4. Quais métricas são utilizadas para avaliar o desempenho desses modelos e quais resultados são reportados?

**Sensibilidade/recall Top-5 (Tabela 2 e resultados, p. 4):**

| Grupo               | Hanseníase presente no Top-5 | Recall    |
| ------------------- | ---------------------------- | --------- |
| Clássicas           | 320/367                      | 87,2%     |
| Reacionais/atípicas | 39/56                        | 69,6%     |
| **Total**           | **359/423**                  | **84,9%** |


A diferença descritiva entre subconjuntos é **17,6 pontos percentuais**, sem teste de significância reportado. Por subtração, 64 imagens processadas não tiveram hanseníase no Top-5: 47 clássicas e 17 reacionais/atípicas. Essas são contagens derivadas dos números publicados, não uma matriz completa com negativos.

**Sensibilidade cumulativa Top-N (Tabela 3, p. 4; grifos 12–13):**

| Grupo               | Top-1 | Top-2 | Top-3 | Top-4 | Top-5 |
| ------------------- | ----- | ----- | ----- | ----- | ----- |
| Clássicas           | 46,9% | 63,5% | 73,8% | 80,1% | 87,2% |
| Reacionais/atípicas | 30,4% | 46,4% | 58,9% | 62,5% | 69,6% |


Top-N significa inclusão **até** a posição N, e não acerto exclusivamente naquela posição. **84,9% não é acurácia global nem acerto Top-1.** Top-4 é a medida correspondente ao número de sugestões exibidas rotineiramente no app, ainda sem constituir teste direto do aplicativo móvel.

Como todos os casos são de hanseníase, não é possível estimar **especificidade, falsos positivos, precisão/PPV ou discriminação contra mimetizadores**. Não são reportados AUC ou F1. No subconjunto 2, o acerto é presença do rótulo hanseníase, não reconhecimento do tipo de reação. O escore de qualidade do app citado na introdução (4,02/5) vem de outro estudo e não é resultado diagnóstico desta avaliação (grifos 10–11 e 15).

## RQ5. Como o desempenho dos modelos varia entre diferentes grupos ou tons de pele?

Há diferença medida entre **apresentações clínicas**: Top-5 de 87,2% nas clássicas e 69,6% nas reacionais/atípicas; Top-1 de 46,9% versus 30,4%. Isso não é uma comparação de tons de pele.

A Tabela 1 descreve Fitzpatrick II–VI, sexo e idade, mas **não fornece desempenho estratificado por fototipo, sexo, faixa etária ou país**. A composição dos subconjuntos também difere, de modo que não é possível atribuir causalmente o menor recall a fototipo ou outro atributo específico.

A observação qualitativa de melhor identificação de lesões hiperpigmentadas não demonstra maior desempenho em pessoas de pele escura: pigmentação da lesão e fototipo do indivíduo são variáveis distintas. Não há sensibilidade isolada para cada forma do espectro de Ridley–Jopling, tipo de reação ou método de confirmação (p. 3–5; grifos 7, 11–14).

## RQ6. Quais modelos e abordagens de inteligência artificial são utilizados para identificar manifestações dermatológicas associadas à hanseníase?

O modelo avaliado é o **classificador CNN pré-treinado de NTDs**, segundo estágio da ferramenta beta da OMS, desenvolvida em colaboração com **UniversalDoctor e Belle.ai**. O classificador distribui probabilidades entre 12 NTDs, incluindo hanseníase, e retorna um ranking (p. 2; grifos 2–3).

Não há desenvolvimento de nova arquitetura neste trabalho. O artigo não identifica suficientemente backbone, checkpoint, hiperparâmetros, tamanho/composição da base original de treino ou versão exata para reproduzir o sistema. Não atribuir ResNet, EfficientNet, AlexNet ou outra arquitetura nominal sem informação.

O teste usa apenas imagens. Contexto do paciente, entrada multimodal e segmentação são propostas futuras. A declaração de uso de ChatGPT refere-se à **edição linguística do manuscrito**, não a um modelo diagnóstico avaliado (p. 5–6).

## RQ7. Como a capacidade de generalização dos modelos é avaliada, especialmente quando são utilizados conjuntos de dados diferentes daqueles empregados no treinamento?

**Este artigo apresenta validação externa:** os autores declaram que a base independente não participou do treinamento nem da validação interna do modelo pré-treinado. Imagens históricas com diferentes apresentações e condições de aquisição são usadas para medir recall externo (p. 2; grifo 1).

A conclusão tem limites claros: base composta apenas de positivos, exclusão de falhas de processamento, análise por imagem com dependência intrapaciente, ausência de comparação direta com humanos e teste no desktop exclusivamente do segundo estágio. A independência é declarada no artigo; não é possível auditar sobreposição com o treinamento a partir de uma descrição pública completa dessa base original.

Não foi realizada implantação prospectiva, nem medida de comportamento dos usuários, impacto clínico, generalização entre dispositivos/centros ou desempenho em outras doenças. O estudo reconhece essas limitações e propõe incorporar não hanseníase/mimetizadores e realizar avaliações de campo. Assim, demonstra generalização analítica limitada à **detecção Top-N de hanseníase em uma base externa de casos positivos**, sem provar desempenho diagnóstico completo em uma população de triagem (p. 5; grifos 15–17).

## RQ8. O artigo foi publicado em que tipo de veículo de publicação? (revista, conferência)

**Revista científica**, como **Original Research**: *Revista Panamericana de Salud Pública / Pan American Journal of Public Health*, **2026;50:e40**, DOI **10.26633/RPSP.2026.40**. O registro da OPAS informa **16 de abril de 2026**; o PDF registra aceite da versão revisada em **12 de fevereiro de 2026**. Não é conferência. São oito páginas; e40 é o identificador do artigo (grifo 20).

# Trechos e notas para o Zotero

Cada número corresponde a uma anotação no PDF. Os trechos textuais abaixo são literais, com quebras de linha/hifenização de fim de linha normalizadas. Nas tabelas, os valores são transcritos na ordem das colunas; suas escalas são explicadas em cada nota. Os comentários podem ser copiados diretamente para o Zotero.

## 01. Validação externa

**Página 2 · Methods — Study Design**

**Trecho grifado:**

> using an independently curated data set that had not been used during training or internal validation

**Comentário:**

RQ3/RQ7 — Validação analítica externa de modelo pré-treinado. Autores declaram base independente, sem uso no treino/validação interna. Não há novo treinamento nem ajuste do modelo neste estudo. Avaliação retrospectiva de imagens, não implantação prospectiva em campo.

## 02. Arquitetura e estágio avaliado

**Página 2 · Introduction — descrição do aplicativo**

**Trecho grifado:**

> Both models are built on convolutional neural network architectures.

**Comentário:**

RQ1/RQ6 — Aplicativo beta com dois classificadores CNN em cascata, desenvolvidos com UniversalDoctor e Belle.ai: triagem geral e classificador de 12 NTDs. O estudo avalia exclusivamente o segundo estágio. Não há backbone, pesos, hiperparâmetros ou versão/checkpoint suficientemente identificados para reprodução integral.

## 03. Top-5 no desktop versus quatro saídas no app

**Página 2 · Introduction — interface e saídas**

**Trecho grifado:**

> Although the app displays four diagnostic suggestions in routine use, the underlying classifier generates five ranked outputs

**Comentário:**

RQ3/RQ4/RQ7 — A interface móvel exibe quatro sugestões; a versão desktop permite cinco e foi usada nesta avaliação. O desfecho Top-5 não corresponde diretamente ao desempenho visível na interface de quatro diagnósticos. Não mede o desempenho end-to-end dos dois estágios em cascata.

## 04. Período e coleta

**Página 2 · Image Acquisition and Data Security**

**Trecho grifado:**

> Clinical images were collected between 1996 and 2024 by leprosy experts.

**Comentário:**

RQ2 — Imagens clínicas históricas coletadas por especialistas entre 1996 e 2024. Não há distribuição detalhada por dispositivo, período ou local de origem. Afiliações dos autores não estabelecem a procedência de cada imagem. Variação de aquisição ao longo de décadas é limitação reconhecida.

## 05. Imagens versus pacientes

**Página 3 · External Validation Data Set**

**Trecho grifado:**

> The external data set comprised 439 anonymized clinical images from 208 confirmed leprosy cases.

**Comentário:**

RQ2/RQ3 — Base inicial: 439 imagens de 208 casos confirmados, alguns com múltiplas imagens. Unidade de análise é a imagem; não confundir 423 imagens analisadas com 423 pacientes. Não é informado quantos pacientes únicos permanecem após as exclusões.

## 06. Exclusões

**Página 3 · External Validation Data Set**

**Trecho grifado:**

> 16 images with processing errors were excluded, resulting in 423 images divided into two subsets

**Comentário:**

RQ2/RQ3 — 16 exclusões por erros de processamento (3,6% de 439, cálculo), restando 423 imagens: 367 clássicas e 56 reacionais/atípicas. Sensibilidade reportada é condicional às imagens processadas; não representa taxa de sucesso operacional sobre todos os envios. O texto não detalha causas/distribuição dos erros.

## 07. Metadados disponíveis

**Página 3 · External Validation Data Set**

**Trecho grifado:**

> Demographic and phenotypic metadata were available for 418 of the 423 images (Subset 1: 362/367; Subset 2: 56/56)

**Comentário:**

RQ2/RQ5 — A Tabela 1 tem denominadores 362 e 56 porque cinco imagens clássicas não têm registro de metadados. Isso não contradiz 367/56 da avaliação. Além disso, há variáveis ausentes dentro dos 418 registros; sexo/fototipo não foram inferidos das fotografias.

## 08. Entrada sem rótulos e metadados

**Página 3 · Image Acquisition and Data Security**

**Trecho grifado:**

> For model testing, images were provided without labels or metadata, which were stored separately

**Comentário:**

RQ1/RQ3 — Teste com imagens sem rótulos ou metadados de entrada, mantidos separadamente. Recorte manual e mascaramento foram usados para anonimização, preservando a lesão. Não confundir isso com segmentação automática de ROI. Não há pipeline técnico de redimensionamento/normalização/augmentação descrito para esta avaliação.

## 09. Padrão de referência

**Página 3 · Diagnostic Confirmation**

**Trecho grifado:**

> diagnoses were established by experienced clinicians following WHO criteria

**Comentário:**

RQ2/RQ3 — Diagnósticos confirmados por clínicos experientes segundo sinais cardinais da OMS. Histopatologia, PCR, sorologia anti-PGL-1 e ultrassom de nervos podiam apoiar quando indicados; o registro histórico não permite contabilizar métodos por caso. Não afirmar que todos tiveram confirmação laboratorial ou por PCR.

## 10. Definição da métrica

**Página 3 · Outcome Measures and Evaluation Approach**

**Trecho grifado:**

> The primary outcome was Top-5 sensitivity (recall), defined as the proportion of images in which leprosy appeared among the model’s five highest-ranked diagnostic predictions

**Comentário:**

RQ3/RQ4 — Desfecho é presença de hanseníase em qualquer uma das cinco primeiras posições. Não é acurácia global, precisão/PPV ou proporção de diagnóstico correto em primeiro lugar. Top-N é cumulativo até N, não frequência exclusiva naquela posição.

## 11. Sensibilidade Top-5 e denominadores

**Página 4 · Quantitative Analysis**

**Trecho grifado:**

> Top-5 predictions in 84.9% (359/423) of images. Sensitivity was 87.2% (320/367) for classical presentations and 69.6% (39/56) for reactional or atypical presentations

**Comentário:**

RQ3/RQ4/RQ5 — Top-5: total 359/423=84,9%; clássicas 320/367=87,2%; reacionais/atípicas 39/56=69,6%. Diferença descritiva de 17,6 pontos percentuais. Não há IC ou teste de significância reportado. Subconjunto 2 mede presença do rótulo hanseníase, não reconhecimento correto do tipo de reação.

## 12. Clássicas: Top-1 a Top-5

**Página 4 · Tabela 3**

**Trecho grifado:**

> Subset 1 46.9% 63.5% 73.8% 80.1% 87.2%

**Comentário:**

RQ4 — 367 imagens clássicas: recall cumulativo Top-1 46,9%, Top-2 63,5%, Top-3 73,8%, Top-4 80,1%, Top-5 87,2%. Top-4 é a aproximação ao número de sugestões exibidas no app, mas teste foi desktop e não valida o fluxo móvel completo.

## 13. Reacionais/atípicas: Top-1 a Top-5

**Página 4 · Tabela 3**

**Trecho grifado:**

> Subset 2 30.4% 46.4% 58.9% 62.5% 69.6%

**Comentário:**

RQ4/RQ5 — 56 imagens reacionais/atípicas: Top-1 30,4%, Top-2 46,4%, Top-3 58,9%, Top-4 62,5%, Top-5 69,6%. Desempenho inferior às clássicas em todos os N, sem análise isolada por tipo de reação, subtipo clínico ou fototipo.

## 14. Inconsistência entre imagens do mesmo paciente

**Página 4 · Qualitative Error Patterns and Intrapatient Inconsistencies**

**Trecho grifado:**

> images from the same patient produced inconsistent diagnostic outputs.

**Comentário:**

RQ3/RQ7 — Análise qualitativa identifica resultados divergentes em imagens do mesmo paciente. Lesões necróticas, infiltrativas e inflamatórias foram problemáticas. Não há taxa numérica por morfologia, ajuste estatístico de dependência intrapaciente ou avaliação humana comparativa. Figura 2B ilustra lesão hiperpigmentada, não prova equidade por fototipo.

## 15. Ausência de controles negativos

**Página 5 · Discussion — limitations**

**Trecho grifado:**

> the data set included only confirmed leprosy cases, preventing the calculation of specificity or false-positive rates.

**Comentário:**

RQ3/RQ4/RQ7 — Base apenas de casos positivos: não permite estimar especificidade, taxa de falsos positivos, PPV/precisão ou desempenho de diagnóstico diferencial contra mimetizadores. A sensibilidade elevada não demonstra discriminação de não hanseníase. Não há AUC ou F1 reportados.

## 16. Avaliação retrospectiva, não implantação

**Página 5 · Discussion — limitations**

**Trecho grifado:**

> because this was not a prospective implementation study, the authors did not assess real-world workflow integration, user behavior, clinical impact, or field performance.

**Comentário:**

RQ3/RQ7 — Não mede impacto clínico, uso por profissionais, integração ao fluxo ou desempenho prospectivo. Teste foi no desktop. Generalização demonstrada é analítica em base externa de positivos, não prontidão para uso autônomo em campo.

## 17. Sem comparação direta com humanos

**Página 5 · Discussion — limitations**

**Trecho grifado:**

> this study did not include direct comparisons with human raters

**Comentário:**

RQ3/RQ4 — Percentuais de desempenho humano citados na discussão vêm de literatura diferente, não de um braço comparativo deste estudo. Não concluir superioridade aos clínicos pela comparação indireta de acurácia humana com sensibilidade Top-5 da IA.

## 18. Segmentação e contexto como futuro

**Página 5 · Discussion**

**Trecho grifado:**

> approaches such as lesion-focused segmentation and the incorporation of patient-level or multimodal context may improve robustness

**Comentário:**

RQ1/RQ6 — Segmentação e contexto multimodal/do paciente são propostas de aprimoramento. Não são técnicas implementadas ou treinadas nesta avaliação. Não há Grad-CAM, LIME ou SHAP aplicados neste estudo.

## 19. Acesso aos dados

**Página 6 · Data availability statement**

**Trecho grifado:**

> The data supporting the findings of this study are available from the corresponding author upon reasonable request.

**Comentário:**

RQ2 — Dados mediante solicitação, com acesso controlado e anonimização descritos; não é um dataset aberto para download. O estudo registra acordo institucional UFES–OMS e aprovação ética.

## 20. Veículo e ano

**Página 1 · Suggested citation**

**Trecho grifado:**

> Rev Panam Salud Publica. 2026;50:e40.

**Comentário:**

RQ8 — Pesquisa original publicada em revista: Revista Panamericana de Salud Pública / Pan American Journal of Public Health, 2026, volume 50, e40. DOI 10.26633/RPSP.2026.40. Não é conferência. O registro da OPAS informa 16/04/2026; PDF de oito páginas.
