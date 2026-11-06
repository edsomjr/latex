---
tags: []
parent: 'Harnessing artificial intelligence for skin-related neglected tropical diseases (skin NTDs): opportunities, challenges and future directions'
collections:
    - TCC_Leituras
$version: 300
$libraryID: 2
$itemKey: EFBLFV4X

---
# Yotsu et al. (2025) — RQs e anotações

**Título:** *Harnessing artificial intelligence for skin-related neglected tropical diseases (skin NTDs): opportunities, challenges and future directions*.\
**Autores:** Rie R. Yotsu; Sebastine Oseghae Oiwoh; Hawah Mbali; Niraj Parajuli; Wendemagegn Enbiale; José A. Ruiz-Postigo.\
**Veículo:** *International Health*, 2025, volume 17, páginas 792–794.\
**Publicação antecipada:** 1º de julho de 2025.\
**DOI:** 10.1093/inthealth/ihaf068.\
**Fonte:** PDF fornecido, três páginas. PDF 1 = editorial 792; PDF 2 = 793; PDF 3 = 794.

**Tipo de publicação: EDITORIAL**, identificado na margem da primeira página. O texto discute oportunidades, desafios e recomendações e cita iniciativas existentes. Não é estudo experimental, validação de modelo próprio ou revisão sistemática; não descreve busca/seleção sistemática de literatura.

A cópia PDF contém **16 grifos com comentários**. O original foi preservado e não houve alteração direta do banco de dados do Zotero. Ao final estão os trechos grifados, suas páginas e comentários para consulta/cópia. As respostas distinguem informações citadas de outras fontes das propostas dos autores. As referências primárias não foram auditadas nesta extração.

## RQ1. Quais técnicas de visão computacional são utilizadas para identificar manifestações dermatológicas associadas à hanseníase?

O editorial descreve **classificação visual de imagens de pele**, reconhecimento de padrões e integração de informação textual e visual em ferramentas de apoio diagnóstico. Cita o classificador visual do **SkinNTDs da OMS**, a plataforma **VisualDx** e seu recurso móvel **DermExpert**, baseado em ML (p. 2; grifos 4 e 8).

O SkinNTDs é descrito como apoio à detecção/triagem de **12 NTDs cutâneas e 24 condições de pele comuns**. Esse é o escopo apresentado da ferramenta, não confirmação de que todas essas condições tenham sido avaliadas no estudo queniano citado. VisualDx integra conhecimento textual de especialistas e reconhecimento visual por imagens, *Sympticons* e ilustrações. O artigo não detalha os algoritmos ou a arquitetura dessa integração.

São propostas padronização de imagens para reduzir diferenças de **iluminação, resolução e representação de tons de pele**, análise de progressão/resposta ao tratamento e uso futuro de modalidades **multiespectrais ou térmicas**. Não são etapas implementadas/avaliadas neste editorial; não há parâmetros de pré-processamento, segmentação de ROI, dimensões de entrada ou aumento de dados. A referência sobre termografia trata de úlcera de Buruli, sem demonstração específica para hanseníase neste texto (grifos 12–13).

Interpretabilidade, justificativas e escores de confiança são recomendados, sem implementação de uma técnica de XAI específica ou avaliação de explicabilidade (grifo 14).

## RQ2. Quais conjuntos de dados e populações são utilizados no desenvolvimento e na avaliação desses modelos?

**Não há dataset ou população própria do editorial.** São citadas as seguintes fontes/iniciativas (p. 2):

| Fonte/iniciativa                           | Informação relatada                                                              | Limite da informação                                                                                              |
| ------------------------------------------ | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Avaliação preliminar do SkinNTDs no Quênia | **605 pacientes**, em **cinco condados**                                         | Não descreve distribuição por doença, idade, sexo, tom de pele, padrão de referência ou relação com o treinamento |
| Biblioteca fotográfica do SkinNTDs         | **Mais de 90%** das imagens de indivíduos com pele escura, Fitzpatrick **IV–VI** | Não informa tamanho total; não comprova composição dos 605 participantes ou do conjunto de treino                 |
| Biblioteca VisualDx                        | **Mais de 47.000 imagens médicas**, **28,5%** de pele escura                     | Biblioteca geral, não dataset específico de hanseníase; sem partições de treino/teste                             |
| Piloto na Costa do Marfim                  | Dados coletados prospectivamente em projeto de teledermatologia                  | Sem contagem de imagens/pacientes, classes, divisão dos dados ou métricas neste editorial                         |


A avaliação queniana é atribuída à **referência 9, relato/notícia da OMS de 2024**. O piloto da Costa do Marfim é o estudo **Yotsu et al. (2023), PLoS Neglected Tropical Diseases, 17(8):e0011230**, referência 11. São estudos/fontes separados, não uma única amostra do presente artigo (grifos 5–7 e 10).

O texto enfatiza imagens anotadas de qualidade e confirmação diagnóstica; o exemplo é **úlcera de Buruli positiva por PCR**. Não atribuir esse processo automaticamente aos casos de hanseníase (grifo 11). Também não tomar afiliações dos autores como locais de recrutamento.

## RQ3. Quais métodos, procedimentos são utilizados para avaliar o desempenho desses modelos e quais resultados são reportados?

O editorial **não executa avaliação própria**. Não apresenta treinamento, holdout, validação cruzada, teste independente ou comparação de modelos. Sua declaração de disponibilidade de dados é “Not applicable” (grifo 16).

A avaliação preliminar citada no Quênia, em 605 pacientes, apresentou **sensibilidade aproximada de 80%** e retorno positivo de profissionais da linha de frente quanto à usabilidade. O texto não detalha padrão de referência, número de positivos, distribuição de doenças, limiar de decisão, intervalos de confiança, instrumento/escore de usabilidade ou desenho estatístico. Portanto, não permite reproduzir a avaliação nem atribuir o percentual especificamente à hanseníase (grifo 5).

O piloto na Costa do Marfim é citado para ressaltar a importância de imagens anotadas e casos confirmados, sem resultados numéricos. **Coleta prospectiva dos dados não comprova, por si só, validação prospectiva de um modelo fixado**, nem teste em uma base externa independente (grifos 10–11).

A referência 8 é um estudo sobre o aplicativo como ferramenta de treinamento em Gana e Quênia; não confundir esse papel com a avaliação diagnóstica de 605 pacientes atribuída à referência 9. O editorial distingue triagem/apoio da confirmação diagnóstica e ressalta a necessidade de história clínica, exame físico e testes laboratoriais conforme o caso (grifo 9).

## RQ4. Quais métricas são utilizadas para avaliar o desempenho desses modelos e quais resultados são reportados?

A medida diagnóstica explicitamente quantificada é **sensibilidade aproximadamente 80%**, citada para a avaliação preliminar do SkinNTDs no Quênia. **Não é acurácia**, nem sensibilidade demonstrada separadamente para hanseníase. Faltam denominadores de casos positivos, valores por classe, limiar, intervalos de confiança e matriz de confusão (p. 2; grifo 5).

Não são apresentados valores de especificidade, precisão/valor preditivo positivo, F1, ROC-AUC ou acurácia por modelo. O retorno de usabilidade é descrito qualitativamente como positivo, sem escala ou escore. VisualDx/DermExpert e o piloto na Costa do Marfim não recebem métricas numéricas neste texto.

**Mais de 90% e 28,5% são percentuais de representação de pele escura nas respectivas bibliotecas**, não medidas de desempenho, e não podem ser comparados como taxas de acerto. Da mesma forma, 605 pacientes e mais de 47.000 imagens são contagens de fontes diferentes.

Escores de confiança são recomendados como recurso de transparência, mas não há valores, calibração ou relação demonstrada com a sensibilidade. Não registrar confiança como sinônimo de desempenho (grifos 6–7 e 14).

## RQ5. Como o desempenho dos modelos varia entre diferentes grupos ou tons de pele?

**Não há avaliação quantitativa estratificada neste editorial.** Os autores discutem que as apresentações variam por tom de pele e região geográfica e que sub-representação pode produzir diferenças de desempenho, mas não fornecem acurácia/sensibilidade por grupo ou magnitude dessas diferenças (p. 1–2).

O texto informa maior presença de pele escura na biblioteca do SkinNTDs (**>90%, Fitzpatrick IV–VI**) e **28,5%** na biblioteca VisualDx. Isso descreve representação, sem demonstrar equidade de desempenho ou generalização. Também não estabelece que ambas as fontes tenham critérios de classificação de tom de pele comparáveis, nem que os percentuais se refiram a participantes únicos.

Não há análise específica de hanseníase por tom de pele, etnia, sexo, idade ou região. A recomendação é avaliar ferramentas nos contextos de saúde de países de baixa/média renda e adaptá-las à diversidade populacional (grifos 6–7 e 15).

## RQ6. Quais modelos e abordagens de inteligência artificial são utilizados para identificar manifestações dermatológicas associadas à hanseníase?

O editorial cita **ML, deep learning, grandes modelos de linguagem e IA generativa** como famílias de tecnologias com possíveis aplicações. Não implementa ou compara nenhuma delas; não identifica uma CNN/backbone específico, pesos, arquitetura, hiperparâmetros ou esquema de treinamento (p. 1; grifo 2).

As ferramentas concretamente mencionadas são:

*   **SkinNTDs da OMS:** classificador visual para triagem/detecção de NTDs cutâneas e condições comuns.
*   **VisualDx:** apoio à construção de diagnósticos diferenciais, integrando conhecimento textual e reconhecimento visual.
*   **DermExpert:** recurso móvel da plataforma que utiliza ML para apoio diagnóstico em tempo real, sem benchmark de tempo ou desempenho apresentado.

O estudo anterior na Costa do Marfim é identificado na referência 11 como pesquisa de deep learning, mas o editorial não fornece sua arquitetura nem resultados isolados de hanseníase. LLMs, IA generativa, imagem multiespectral e térmica não devem ser registrados como modelos validados para hanseníase por este artigo (grifos 4, 8 e 10–12).

## RQ7. Como a capacidade de generalização dos modelos é avaliada, especialmente quando são utilizados conjuntos de dados diferentes daqueles empregados no treinamento?

**Não há avaliação externa própria nem protocolo cross-dataset apresentado.** O texto não informa os dados de treinamento das ferramentas nem sua relação com os casos da avaliação queniana; assim, não é possível classificar essa avaliação como validação externa independente apenas a partir deste editorial.

O piloto na Costa do Marfim utiliza dados prospectivamente coletados, mas não há detalhes suficientes para determinar separação entre treino/teste, independência dos pacientes ou validação em outra base. As iniciativas no Quênia e na Costa do Marfim não constituem uma comparação de um mesmo modelo entre dois países demonstrada neste artigo.

Os autores recomendam diversidade de dados, adaptação ao contexto, qualidade de imagens, transparência e avaliação nas condições reais dos sistemas de saúde de países de baixa/média renda. Não apresentam resultados entre dispositivos, tons de pele ou regiões, nem demonstram robustez de implantação (grifos 3, 10, 13 e 15).

## RQ8. O artigo foi publicado em que tipo de veículo de publicação? (revista, conferência)

**Revista científica**, na categoria **Editorial**. Publicado em *International Health*, **2025, volume 17, páginas 792–794**, pela Oxford University Press em nome da Royal Society of Tropical Medicine and Hygiene. Publicação antecipada em **1º de julho de 2025**. DOI **10.1093/inthealth/ihaf068**. Não é conferência nem estudo primário de validação (p. 1; grifo 1).

## Uso na revisão do TCC

O texto serve para contextualizar oportunidades, barreiras, diversidade, confirmação diagnóstica e implantação de IA para NTDs cutâneas. Se os critérios exigirem estudos primários de desenvolvimento/avaliação, identificá-lo como **editorial/contexto**. Os estudos citados precisam de extração própria para preencher resultados específicos de hanseníase; não contabilizar novamente seus participantes como amostra deste editorial.

# Trechos e notas para o Zotero

Cada número corresponde a uma anotação no PDF. Os trechos textuais abaixo são literais, com quebras de linha/hifenização de fim de linha normalizadas. Nas tabelas, os valores são transcritos na ordem das colunas; suas escalas são explicadas em cada nota. Os comentários podem ser copiados diretamente para o Zotero.

## 01. Veículo, ano e DOI

**Página 1 · Cabeçalho editorial**

**Trecho grifado:**

> https\://doi.org/10.1093/inthealth/ihaf068

**Comentário:**

RQ3/RQ8 — Editorial em International Health, 2025, volume 17, páginas 792–794; publicação antecipada em 1º de julho de 2025. DOI 10.1093/inthealth/ihaf068. A categoria EDITORIAL está na margem esquerda. Não é estudo experimental nem revisão sistemática; não há método de busca/seleção ou amostra própria.

## 02. Famílias de IA

**Página 1 · Discussão sobre oportunidades da IA**

**Trecho grifado:**

> AI encompasses a range of technologies, including machine learning (ML), deep learning (DL), large language models (LLMs) and generative AI

**Comentário:**

RQ6 — ML, deep learning, LLMs e IA generativa são apresentados como famílias tecnológicas com aplicações possíveis. Não são modelos implementados/comparados neste editorial. Não atribuir arquitetura CNN, backbone, pesos ou hiperparâmetros não especificados.

## 03. Limitação de dados

**Página 1 · Barreiras à aplicação de IA**

**Trecho grifado:**

> the limited number and the lack of high-quality skin image datasets to train ML, particularly from populations in low- and middle-income countries (LMICs)

**Comentário:**

RQ2/RQ7 — Escassez de bases de qualidade e de populações de países de baixa/média renda é apontada como barreira. Não há novo dataset nem contagens de treino/validação/teste neste artigo.

## 04. Escopo do classificador

**Página 2 · SkinNTDs app**

**Trecho grifado:**

> The WHO’s SkinNTDs app incorporates a visual classifier to support the detection and screening of 12 skin NTDs and 24 common skin conditions.

**Comentário:**

RQ1/RQ6 — O editorial descreve classificador visual do SkinNTDs da OMS para triagem/detecção de 12 NTDs cutâneas e 24 condições comuns. Isso é escopo descrito da ferramenta, não prova de que todas as 36 condições foram avaliadas no estudo citado. Não fornece arquitetura ou desempenho específico de hanseníase.

## 05. Amostra e sensibilidade citadas

**Página 2 · Avaliação preliminar no Quênia**

**Trecho grifado:**

> A preliminary study involving 605 patients across five counties in Kenya showed approximately 80% sensitivity

**Comentário:**

RQ2/RQ3/RQ4 — Evidência secundária: avaliação preliminar em 605 pacientes de cinco condados do Quênia, com sensibilidade aproximada de 80%. Referência 9 é notícia/relato OMS de 2024. Não é acurácia; o editorial não informa denominador de positivos, IC, métricas por doença, padrão de referência ou relação com dados de treinamento. Não atribuir 80% especificamente à hanseníase.

## 06. Representação de pele escura

**Página 2 · Biblioteca do SkinNTDs app**

**Trecho grifado:**

> > 90% of images in the app’s photo library belong to individuals with dark skin tones (Fitzpatrick IV–VI).

**Comentário:**

RQ2/RQ5 — Mais de 90% das imagens da biblioteca do aplicativo são de pele escura (Fitzpatrick IV–VI), segundo o editorial. Percentual de representação, não desempenho diagnóstico. Não é necessariamente proporção dos 605 pacientes nem composição do conjunto de treinamento; o tamanho da biblioteca não é informado aqui.

## 07. Tamanho e composição da biblioteca

**Página 2 · VisualDx**

**Trecho grifado:**

> With access to >47 000 high-quality medical images, including 28.5% depicting individuals with dark skin

**Comentário:**

RQ2/RQ5 — VisualDx: acesso a mais de 47.000 imagens médicas, 28,5% de pele escura. São números da biblioteca da plataforma, não de um dataset de hanseníase ou divisão de treino/teste relatada. Não informa desempenho por grupo nem demonstra comparabilidade com a biblioteca do aplicativo OMS.

## 08. Abordagem de apoio diagnóstico

**Página 2 · VisualDx e DermExpert**

**Trecho grifado:**

> The platform integrates text-based expert knowledge with visual pattern recognition using images, Sympticons and illustrations.

**Comentário:**

RQ1/RQ6 — Integra conhecimento textual de especialistas e reconhecimento visual, usando imagens, Sympticons e ilustrações. O texto acrescenta que DermExpert usa ML para apoio em tempo real. Não há descrição de uma arquitetura de fusão multimodal treinada pelos autores nem benchmark quantitativo de VisualDx/DermExpert.

## 09. Triagem e confirmação

**Página 2 · Limites do apoio diagnóstico**

**Trecho grifado:**

> AI can support screening and serve as a clinical decision support tool, but it cannot replace a confirmatory diagnosis.

**Comentário:**

RQ3/RQ7 — Autores distinguem triagem/apoio de diagnóstico confirmatório. O parágrafo ressalta história clínica, exame físico e testes laboratoriais. Não há evidência apresentada de substituição da confirmação clínica/laboratorial por uma fotografia ou escore de IA.

## 10. Dados prospectivamente coletados

**Página 2 · Estudo-piloto na Costa do Marfim**

**Trecho grifado:**

> A pilot study in Côte d’Ivoire explored the potential of AI-based tools for detecting skin NTDs using prospectively collected data from a teledermatology project.

**Comentário:**

RQ2/RQ3/RQ7 — Relato de estudo anterior (Yotsu et al., 2023; referência 11) com dados coletados prospectivamente em projeto de teledermatologia na Costa do Marfim. O editorial não informa tamanho, classes, particionamento ou métricas desse estudo. Coleta prospectiva não equivale, por si só, a validação prospectiva de modelo fixado nem a validação externa.

## 11. Qualidade dos rótulos

**Página 2 · Estudo-piloto na Costa do Marfim**

**Trecho grifado:**

> the inclusion of confirmed cases—such as polymerase chain reaction–positive Buruli ulcer—to enhance model accuracy and reliability.

**Comentário:**

RQ2/RQ3 — Defende imagens anotadas de qualidade e casos confirmados; exemplo explícito é úlcera de Buruli PCR-positiva. Não transferir esse padrão de referência automaticamente para hanseníase nem afirmar ganho numérico, pois o editorial não o apresenta.

## 12. Imagem multiespectral e térmica

**Página 2 · Modalidades emergentes**

**Trecho grifado:**

> Emerging technologies that combine different imaging modalities, such as multispectral or thermal imaging, may offer further improvements in disease detection.

**Comentário:**

RQ1/RQ6 — Imagem multiespectral/térmica é discutida como possibilidade futura, não experimento próprio. A referência 13 é sobre termografia de úlcera de Buruli; não é demonstração de desempenho para hanseníase.

## 13. Padronização de imagens

**Página 2 · Aplicações adicionais**

**Trecho grifado:**

> image standardization, reducing inconsistencies in lighting, resolution and skin tone representation

**Comentário:**

RQ1/RQ5/RQ7 — Padronização de iluminação, resolução e representação de tons de pele é proposta para melhorar qualidade e desempenho. Não há transformação, resolução-alvo, algoritmo de correção, aumento de dados ou experimento de robustez especificado.

## 14. Transparência e interpretabilidade

**Página 2 · Desafios**

**Trecho grifado:**

> AI models must be transparent and interpretable, providing confidence scores and rationales for their predictions to support clinical decision-making.

**Comentário:**

RQ1/RQ4/RQ6 — Recomendação de transparência, escores de confiança e justificativas. Não há Grad-CAM/LIME/SHAP implementado, métrica de explicabilidade, limiar operacional ou análise de calibração apresentada. Confiança não deve ser registrada como sensibilidade/acurácia.

## 15. Generalização e adaptação

**Página 2 · Diversidade e sistemas de saúde**

**Trecho grifado:**

> these tools must be evaluated within the realities of LMIC health systems and adapted to the diversity of affected populations.

**Comentário:**

RQ5/RQ7 — Recomenda avaliar em sistemas de saúde de países de baixa/média renda e populações diversas. Não apresenta avaliação externa própria, comparação entre tons de pele, países ou dispositivos. Menções a variações geográficas e de pigmentação são justificativas, não medidas de desempenho.

## 16. Sem dados próprios

**Página 2 · Declarações**

**Trecho grifado:**

> Data availability: Not applicable.

**Comentário:**

RQ2/RQ3 — Editorial sem dataset próprio disponibilizado, sem treinamento ou avaliação conduzidos neste texto. Os números de bibliotecas e a amostra queniana são informações citadas de outras fontes. Não combinar essas contagens como uma amostra única.
