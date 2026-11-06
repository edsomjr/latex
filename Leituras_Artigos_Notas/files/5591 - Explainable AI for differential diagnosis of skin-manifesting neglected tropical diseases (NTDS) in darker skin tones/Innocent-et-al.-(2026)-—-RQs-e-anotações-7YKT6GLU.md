---
tags: []
parent: 'Explainable AI for differential diagnosis of skin-manifesting neglected tropical diseases (NTDS) in darker skin tones'
collections:
    - TCC_Leituras
$version: 296
$libraryID: 2
$itemKey: 7YKT6GLU

---
# Innocent et al. (2026) — RQs e anotações

**Título:** *Explainable AI for differential diagnosis of skin-manifesting neglected tropical diseases (NTDS) in darker skin tones*.\
**Primeiro autor:** David Chinaecherem Innocent.\
**Veículo:** *BMC Artificial Intelligence*, 2026, volume 2, artigo 15.\
**DOI:** 10.1186/s44398-026-00033-w.\
**Fonte:** PDF fornecido pelo usuário, 11 páginas. Todas as referências de página abaixo usam a numeração do PDF.

**Tipo de estudo:** revisão narrativa estruturada com busca sistemática e síntese temática, sem metanálise. Não é estudo primário de treinamento ou validação de IA. Não gera nem analisa um dataset próprio. A evidência de dermatologia geral deve permanecer separada da evidência específica de hanseníase.

Foram preparadas **24 anotações**: 22 grifos textuais e duas marcações de área em tabelas, todos com comentários. A cópia preserva o conteúdo do original. As anotações estão incorporadas à cópia PDF, sem alteração direta do banco de dados do Zotero. Os trechos e campos das tabelas estão transcritos ao final com seus comentários.

## RQ1. Quais técnicas de visão computacional são utilizadas para identificar manifestações dermatológicas associadas à hanseníase?

A revisão descreve **CNNs** que extraem características de cor, textura e bordas de imagens clínicas; **mapas de saliência**, **Grad-CAM** e **mapas/mecanismos de atenção** para destacar regiões relacionadas às predições; e recursos complementares de visualização de decisões, confiança e incerteza (p. 5–7; anotações 7–8 e 11–15).

Para hanseníase, a Tabela 4 apresenta como oportunidade a **detecção de bordas da lesão e mudanças de textura**, em um cenário de diagnóstico diferencial com tinea, vitiligo e psoríase. A Tabela 6 retoma essa oportunidade. Isso é uma proposta conceitual, sem implementação ou resultados específicos neste artigo (p. 5 e 8; anotação 24).

A Figura 1 representa um fluxo conceitual de aquisição, pré-processamento, extração de características, classificação e interpretação. A Figura 2 é explicitamente uma ilustração conceitual de mapa de atenção: não demonstra uma saída de modelo desenvolvido ou validado pelos autores, nem a identificação confirmada de hanseníase na imagem ilustrada.

São recomendados pré-processamento robusto e controle de qualidade diante de variações de iluminação, resolução, movimento e câmera. Não há dimensões de entrada, normalização, aumento de dados, segmentação, parâmetros ou código de um pipeline próprio. Não tratar Grad-CAM como segmentação validada ou explicação causal, nem confiança elevada como garantia de acerto (p. 6–8; anotações 11–13 e 16).

## RQ2. Quais conjuntos de dados e populações são utilizados no desenvolvimento e na avaliação desses modelos?

**Não há dataset ou população própria.** A declaração de disponibilidade informa que nenhum dataset foi gerado ou analisado. A Tabela 3 resume bases de estudos citados, frequentemente com descrição incompleta (p. 4 e 9; anotações 21 e 23).

| Estudo citado na Tabela 3 | Dataset/amostra conforme a revisão                | Escopo e representação descritos                                 |
| ------------------------- | ------------------------------------------------- | ---------------------------------------------------------------- |
| Esteva et al. (2017)      | 129.450 imagens                                   | Câncer de pele; predominância de tons claros                     |
| Han et al. (2018)         | 49.567 imagens                                    | Onicomicose; sem estratificação por tom de pele                  |
| Groh et al. (2021)        | Fitzpatrick17k                                    | Dermatologia geral; tipos Fitzpatrick I–VI                       |
| Daneshjou et al. (2021)   | Diversos datasets clínicos, sem tamanho na tabela | Múltiplas doenças dermatológicas; grupos de tons de pele         |
| Du et al. (2022)          | Não especificado                                  | Estudo de mitigação de viés com grupos de tons de pele           |
| Munia & Imran (2025)      | Dados sintéticos + reais, sem tamanho na tabela   | Mitigação de viés; grupos raciais/de tons de pele                |
| Singh et al. (2024)       | Não especificado                                  | Múltiplas doenças de pele; representação pouco descrita          |
| Minyilu et al. (2025)     | Múltiplos datasets, sem contagem consolidada      | Revisão sobre NTDs; representação não consistentemente reportada |


Essas informações são **relatadas por Innocent et al.**, sem auditoria dos estudos originais nesta extração. Não somar as amostras como um conjunto único nem atribuir as bases de câncer/onicomicose à hanseníase. O artigo também referencia **eSkinHealth** na bibliografia, mas não fornece nesta revisão uma extração detalhada de seu tamanho, classes, participantes e desempenho específico de hanseníase.

A revisão enfatiza populações de pele mais escura e regiões endêmicas/países de renda baixa e média. Define operacionalmente tons mais escuros como **Fitzpatrick IV–VI**, mas algumas comparações citadas usam **V–VI versus I–III**. Não há distribuição própria por idade, sexo, país, etnia ou tom de pele. Fitzpatrick, raça e etnia não devem ser tratados como variáveis intercambiáveis (p. 2; anotação 4).

## RQ3. Quais métodos, procedimentos são utilizados para avaliar o desempenho desses modelos e quais resultados são reportados?

A contribuição é uma **revisão narrativa estruturada**, com busca de janeiro de 2015 a dezembro de 2025, critérios de seleção, busca manual e síntese temática, **sem agregação estatística**. Não há treinamento, holdout, validação cruzada ou teste externo executado pelos autores (p. 1–4; anotações 1–3 e 6).

Há inconsistências relevantes no protocolo relatado:

*   **Bases de busca:** resumo lista PubMed/MEDLINE, Scopus, AJOL e ScienceDirect; métodos e Tabela 1 listam PubMed/MEDLINE, Scopus, Web of Science e IEEE Xplore. As listas não devem ser unificadas como se todas estivessem confirmadas.
*   **Preprints:** métodos os descrevem como apoio contextual e Tabela 2 exclui preprints como evidência primária. Entretanto, Tabela 3 apresenta resultados de Munia & Imran (2025) e Daneshjou et al. (2021), cujas referências 10 e 22 são identificadas como preprints arXiv. A revisão não esclarece essa distinção de uso ou eventual versão publicada.
*   **Seleção e qualidade:** Tabela 1 informa registros recuperados e Tabela 3 apresenta oito entradas, mas não localizei fluxo completo de triagem, duplicatas, exclusões e total final reconciliado, nem descrição suficiente dos revisores ou avaliação formal tabulada de risco de viés/certeza da evidência. Não tomar as oito linhas como confirmação de todo o corpus.

Os resultados incluem altas taxas de desempenho em estudos de dermatologia geral, desempenho mais limitado para NTDs e desigualdades entre tons de pele. São relatos secundários de tarefas e fontes heterogêneas; não demonstram desempenho de um sistema próprio de diagnóstico diferencial de hanseníase. A revisão reconhece que essa heterogeneidade impede comparações quantitativas diretas (p. 9; anotações 19–20).

## RQ4. Quais métricas são utilizadas para avaliar o desempenho desses modelos e quais resultados são reportados?

A revisão menciona principalmente **acurácia**, **AUC**, **sensibilidade**, desempenho de localização e diferenças entre grupos. Também discute confiança e incerteza, sem um experimento de calibração ou avaliação quantitativa própria de explicabilidade.

| Resultado citado pela revisão                       | Local                            | Interpretação para a extração                                              |
| --------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------- |
| Acurácia frequentemente >85%                        | Resumo, p. 1                     | Dermatologia ampla; não resultado específico de hanseníase                 |
| Acurácia aproximadamente 91% em Esteva et al.       | Tabela 3, p. 4                   | Câncer de pele, conforme a revisão; evidência indireta                     |
| Acurácia moderada aproximadamente 70% em NTDs       | Introdução, p. 2; Tabela 3, p. 4 | Relato amplo; não estimativa isolada de hanseníase ou resultado próprio    |
| Redução de acurácia de até 15% em tons mais escuros | Tabelas 3 e 5, p. 4 e 6          | Atribuída a Daneshjou et al.; sem pares absolutos/denominadores detalhados |
| Diferenças de acurácia de 5% a mais de 20%          | Corpo do texto, p. 6             | Faixa entre tarefas/doenças; não efeito combinado                          |
| Acurácia ou AUC >85–90%; reduções de até 15–20%     | Conclusão, p. 9                  | Síntese narrativa de métricas distintas, sem denominador comum             |


Preservar as expressões percentuais usadas pelos autores: o artigo não esclarece de forma suficiente se as diferenças são **relativas ou em pontos percentuais**. Não converter uma interpretação na outra. Tampouco tratar AUC e acurácia como medidas equivalentes.

Não há tabela de métricas por classe de hanseníase, matriz de confusão própria, intervalos de confiança comparáveis, estimativa combinada ou análise estatística própria. Os benefícios atribuídos à XAI são principalmente interpretativos/conceituais; não há ensaio que quantifique aumento de acurácia ou redução de erros pela inclusão de Grad-CAM. Não há limiar operacional de confiança, ECE ou Brier score apresentado (anotações 9, 13 e 18–20).

## RQ5. Como o desempenho dos modelos varia entre diferentes grupos ou tons de pele?

Esta é uma questão central da revisão. Ela relata **menor desempenho em tons mais escuros**, associado à sub-representação nos datasets e à avaliação agregada que pode ocultar erros de subgrupos. O corpo do texto compara Fitzpatrick **V–VI com I–III**, enquanto a definição geral de pele mais escura abrange **IV–VI** (p. 2 e 6).

As diferenças citadas variam de **5% a mais de 20%**, com até **15%** nas tabelas que resumem Daneshjou et al. A conclusão utiliza **15–20%**. Esses números provêm da literatura de dermatologia geral e não estabelecem quanto o desempenho em hanseníase varia por tom de pele. Não há pares de resultados por grupo, tamanho de amostra por estrato ou intervalos de confiança suficientes para uma comparação independente nesta revisão.

Du et al. são descritos como reduzindo viés por métodos de disentanglement e Munia & Imran como melhorando desempenho em pele mais escura com dados/modelos de difusão, sem ganho numérico detalhado nas tabelas. São relatos secundários, não experimentos dos autores.

A recomendação é coletar dados mais inclusivos e estratificar rotineiramente resultados por tom de pele. **Não há resultado específico estratificado de hanseníase**, nem demonstração de que XAI por si só elimine a desigualdade (anotações 4, 9–10 e 20).

## RQ6. Quais modelos e abordagens de inteligência artificial são utilizados para identificar manifestações dermatológicas associadas à hanseníase?

A revisão aborda **CNNs/redes neurais profundas**, métodos de **atenção**, **deep learning multimodal**, aprendizagem com **disentanglement** para mitigação de viés e **modelos de difusão** para dados sintéticos. Discute XAI pós-hoc, sobretudo Grad-CAM e saliência, e atenção incorporada à arquitetura (p. 4–7).

Essas famílias aparecem em estudos de diferentes doenças e propósitos. Não se deve afirmar que todas foram aplicadas e validadas para hanseníase neste artigo. Não há arquitetura própria, checkpoint, pesos, hiperparâmetros ou comparação controlada entre modelos.

Para o diagnóstico diferencial de NTDs, os autores recomendam **classificação multiclasse**, considerando a coexistência de doenças com aparência semelhante. Hanseníase aparece junto de escabiose, bouba, leishmaniose cutânea e úlcera de Buruli, além dos respectivos mimetizadores. Isso é uma orientação metodológica, não um classificador novo com essas classes treinado nesta revisão (anotações 7, 12, 14 e 24).

## RQ7. Como a capacidade de generalização dos modelos é avaliada, especialmente quando são utilizados conjuntos de dados diferentes daqueles empregados no treinamento?

**Não é realizada validação externa própria nem reanálise cross-dataset.** A revisão discute limitações de generalização decorrentes de tons de pele, distribuição de doenças, qualidade de imagens, dispositivos e contextos clínicos diferentes. Não fornece um protocolo padronizado com pares de datasets de treino/teste externo e resultados específicos de hanseníase.

Recomenda avaliação entre grupos e classes de dispositivos, dados mais diversos, controle de qualidade e integração ao fluxo de profissionais de saúde. Execução offline/edge e uso em smartphones são considerações de implantação, sem benchmark próprio de latência, memória, robustez entre câmeras ou estudo prospectivo de campo (p. 8; anotações 16–17).

Os autores reconhecem que a escassez de estudos específicos de NTDs limita estimativas por doença e exige cautela na generalização. Dados de câncer de pele ou outras condições não comprovam generalização para hanseníase. Mapas de explicabilidade e confiança também não substituem teste externo (p. 9; anotação 20).

## RQ8. O artigo foi publicado em que tipo de veículo de publicação? (revista, conferência)

**Revista científica.** Publicado como **Review** em *BMC Artificial Intelligence*, **2026, volume 2, artigo 15**, DOI **10.1186/s44398-026-00033-w**. O PDF tem 11 páginas; 15 é o identificador do artigo. Não é artigo de conferência (p. 1; anotação 22).

## Uso na síntese da revisão

Este artigo contribui principalmente para contextualizar **XAI, equidade entre tons de pele, diagnóstico diferencial e lacunas de validação**. Se os critérios do TCC aceitarem apenas estudos primários, classificá-lo como literatura secundária/contextual. Evitar registrar os percentuais narrativos como resultados experimentais de hanseníase ou contabilizar novamente os estudos primários citados como amostras independentes desta revisão.

# Trechos e notas para o Zotero

Cada número corresponde a uma anotação no PDF. Os trechos textuais abaixo são literais, com quebras de linha/hifenização de fim de linha normalizadas. Nas tabelas, os valores são transcritos na ordem das colunas; suas escalas são explicadas em cada nota. Os comentários podem ser copiados diretamente para o Zotero.

## 01. Tipo de estudo

**Página 1 · Resumo — Methods**

**Trecho grifado:**

> A structured narrative review was conducted using systematic search methods

**Comentário:**

RQ3/RQ8 — Revisão narrativa estruturada com métodos de busca sistemáticos; não é experimento primário, validação de modelo próprio ou meta-análise. Não classificar automaticamente como revisão sistemática apenas por utilizar buscas sistemáticas.

## 02. Bases no resumo

**Página 1 · Resumo — Methods**

**Trecho grifado:**

> across PubMed/MEDLINE, Scopus, AJOL, and ScienceDirect.

**Comentário:**

RQ3 — Resumo lista PubMed/MEDLINE, Scopus, AJOL e ScienceDirect. Métodos e Tabela 1 listam PubMed/MEDLINE, Scopus, Web of Science e IEEE Xplore. Divergência de relato que limita a reprodução da busca; não escolher silenciosamente uma das listas.

## 03. Bases e período nos métodos

**Página 2 · Methods — Literature search strategy**

**Trecho grifado:**

> Searches were performed across four major bibliographic databases: PubMed/MEDLINE, Scopus, Web of Science, and IEEE Xplore

**Comentário:**

RQ3 — Bases dos métodos e Tabela 1, diferentes do resumo. Período declarado: janeiro de 2015 a dezembro de 2025. Há busca manual em referências. Não localizei fluxo completo de seleção, números finais reconciliados de estudos, avaliação formal do risco de viés ou detalhes suficientes dos revisores.

## 04. Definição operacional de tons de pele

**Página 2 · Introduction**

**Trecho grifado:**

> In this review, “darker skin tones” refer to Fitzpatrick skin types IV–VI

**Comentário:**

RQ2/RQ5 — Os autores operacionalizam pele mais escura como Fitzpatrick IV–VI. Em outros trechos, comparam V–VI com I–III. Preservar essas definições distintas e não tratar Fitzpatrick, raça e etnia como variáveis equivalentes. Não há amostra própria estratificada.

## 05. Uso declarado de literatura contextual

**Página 2 · Methods — Review design**

**Trecho grifado:**

> preprints and WHO reports were used as contextual and supporting literature

**Comentário:**

RQ3 — Preprints e relatórios OMS são declarados contextuais. Porém, Tabela 3 inclui Munia & Imran (2025) e Daneshjou et al. (2021) como estudos de resultados, cujas referências 10 e 22 são apresentadas como preprints arXiv. A Tabela 2 exclui preprints como evidência primária. Registrar a inconsistência no tratamento da evidência; não presumir verificação das versões publicadas.

## 06. Síntese sem agregação estatística

**Página 4 · Synthesis — continuação**

**Trecho grifado:**

> across thematic domains rather than statistically pooled.

**Comentário:**

RQ3/RQ4 — Síntese narrativa temática, sem metanálise. Percentuais citados não são estimativas combinadas nem métricas de um mesmo experimento. A heterogeneidade de doenças, bases e tarefas impede comparações diretas sem consultar os estudos originais.

## 07. Técnicas de visão computacional

**Página 5 · Current AI applications in skin disease diagnosis**

**Trecho grifado:**

> Convolutional neural networks (CNNs) have become the dominant architecture in skin disease classification due to their capacity to hierarchically extract discriminative visual features such as colour gradients, texture irregularities and lesion boundaries directly from raw images

**Comentário:**

RQ1/RQ6 — Revisão descreve CNNs extraindo cor, textura e bordas de imagens clínicas. São técnicas da literatura, não implementação própria. Não há resolução de entrada, normalização, aumento de dados ou segmentação com parâmetros reproduzíveis definidos para um novo modelo.

## 08. Fluxo conceitual

**Página 5 · Figura 1 — legenda**

**Trecho grifado:**

> Conceptual diagnostic pipeline for skin image analysis

**Comentário:**

RQ1/RQ3 — Figura 1 é conceitual: aquisição → pré-processamento → extração de características → classificação → interpretação. Não é arquitetura implementada/validada pelos autores; não inferir experimento ou especificações a partir dos ícones.

## 09. Desempenho por tom de pele

**Página 6 · Gaps in AI performance across skin tones**

**Trecho grifado:**

> with reported accuracy differentials ranging from 5% to over 20% depending on task complexity and disease category

**Comentário:**

RQ4/RQ5 — Revisão cita diferenças de acurácia de 5% a mais de 20%, em comparações de dermatologia geral (V–VI versus I–III). Não fornece pares completos de valores, denominadores, IC ou distinção inequívoca entre variação relativa e pontos percentuais. Não atribuir essa faixa especificamente à hanseníase nem tratá-la como efeito combinado.

## 10. Limitação de estratificação

**Página 6 · Gaps in AI performance across skin tones**

**Trecho grifado:**

> The lack of routine stratification by skin tone in model evaluation further perpetuates a false perception of generalizability

**Comentário:**

RQ5/RQ7 — Métricas agregadas podem esconder desigualdades. O texto recomenda estratificação por tom de pele, mas não executa reanálise dos dados nem apresenta desempenho próprio por grupo.

## 11. Mapas de saliência e limites

**Página 6 · Explainable AI techniques used in medical image analysis**

**Trecho grifado:**

> saliency outputs can be noisy, unstable, and sensitive to minor perturbations in input images

**Comentário:**

RQ1/RQ3 — Mapas de saliência são discutidos como explicações visuais, com limitações de estabilidade. Não há teste próprio de fidelidade, estabilidade, concordância com especialistas ou impacto diagnóstico de XAI.

## 12. Grad-CAM

**Página 6 · Explainable AI techniques used in medical image analysis**

**Trecho grifado:**

> Grad-CAM localises discriminative regions by weighting convolutional feature maps according to their contribution to a given class prediction

**Comentário:**

RQ1/RQ6 — Grad-CAM e mapas de atenção destacam regiões associadas à predição; não equivalem automaticamente a segmentação validada ou explicação causal. A revisão não implementa Grad-CAM nem mede melhora de acurácia decorrente de sua utilização.

## 13. Confiança e calibração

**Página 7 · Explainable AI — continuação**

**Trecho grifado:**

> confidence scores are often poorly calibrated, and high confidence does not necessarily equate to correctness

**Comentário:**

RQ1/RQ4 — Discussão inclui probabilidades, quantificação de incerteza e limiares de confiança. Não há valores de limiar, ECE, Brier score ou experimento de calibração apresentados. Confiança não é sinônimo de acurácia ou de explicação fiel.

## 14. Classificação multiclasse recomendada

**Página 7 · Differential diagnosis**

**Trecho grifado:**

> this diagnostic complexity underscores the importance of multi-class classification frameworks rather than binary disease–non-disease models.

**Comentário:**

RQ1/RQ6 — Recomenda classificação multiclasse para distinguir doenças visualmente semelhantes (hanseníase, escabiose, bouba, leishmaniose cutânea, úlcera de Buruli e mimetizadores). É recomendação, não classificador novo com classes/dados/treino e matriz de confusão próprios.

## 15. Mapa ilustrativo, não resultado experimental

**Página 7 · Figura 2 — legenda**

**Trecho grifado:**

> Conceptual illustration of explainable artificial intelligence (XAI) output in skin disease diagnosis

**Comentário:**

RQ1/RQ3 — Figura 2 é explicitamente conceitual. O mapa colorido não documenta saída de modelo treinado/avaliado neste artigo nem diagnóstico confirmado da lesão ilustrada. Não usá-lo como evidência de eficácia ou localização correta de hanseníase.

## 16. Qualidade e pré-processamento recomendados

**Página 8 · Practical considerations for LMIC deployment**

**Trecho grifado:**

> This variability necessitates robust preprocessing pipelines and quality-control mechanisms capable of flagging unreliable inputs prior to inference.

**Comentário:**

RQ1/RQ7 — Iluminação, resolução, movimento e câmeras são apontados como fontes de variação; recomenda-se pré-processamento e controle de qualidade. Não há pipeline próprio com parâmetros ou avaliação de robustez quantitativa.

## 17. Validação entre dispositivos

**Página 8 · Practical considerations for LMIC deployment**

**Trecho grifado:**

> Bias-aware evaluation across device classes is thus essential to ensure equitable performance.

**Comentário:**

RQ3/RQ7 — Recomenda avaliação entre classes de dispositivos, execução offline/edge e integração ao trabalho clínico. Não apresenta experimento próprio entre smartphones, países ou centros, nem métricas de latência, memória ou uso real.

## 18. Resultados amplos de dermatologia

**Página 9 · Conclusion**

**Trecho grifado:**

> accuracy or AUC values exceeding 85–90% in controlled settings

**Comentário:**

RQ3/RQ4 — Faixa narrativa citada para dermatologia geral em ambientes controlados; agrega menções a métricas diferentes (accuracy/AUC) sem experimento comum. Não atribuir 85–90% à hanseníase, ao diagnóstico multiclasse de NTDs ou a um modelo dos autores.

## 19. Limitações da revisão

**Página 9 · Limitations of this review**

**Trecho grifado:**

> substantial heterogeneity in study design, datasets, AI architectures, and reporting standards limited direct quantitative comparison across studies.

**Comentário:**

RQ3/RQ4 — Heterogeneidade limita comparação quantitativa direta. Busca restrita ao inglês e campo em evolução também são limitações reconhecidas. Não há avaliação formal tabulada de risco de viés/certeza da evidência apresentada.

## 20. Ausência de estimativa específica por doença

**Página 9 · Limitations of this review**

**Trecho grifado:**

> the limited availability of NTD-specific AI studies constrained the ability to draw disease-specific performance estimates, necessitating cautious interpretation of generalisability.

**Comentário:**

RQ4/RQ7 — Os próprios autores reconhecem insuficiência de evidência específica para NTDs. Não há estimativa de desempenho isolada e auditável para hanseníase nem resultado externo próprio. Evidência de câncer de pele/outras dermatoses é indireta para as RQs sobre hanseníase.

## 21. Sem dataset próprio

**Página 9 · Data availability**

**Trecho grifado:**

> No datasets were generated or analysed during the current study.

**Comentário:**

RQ2/RQ3 — Revisão sem geração ou análise de datasets próprios. Tamanhos de bases na Tabela 3 pertencem aos estudos citados; não somar como amostra única, nem inventar divisão de treino/teste ou população dos autores.

## 22. Veículo e DOI

**Página 1 · Cabeçalho editorial**

**Trecho grifado:**

> https\://doi.org/10.1186/s44398-026-00033-w

**Comentário:**

RQ8 — Artigo de revisão em revista: BMC Artificial Intelligence, 2026, volume 2, artigo 15; DOI 10.1186/s44398-026-00033-w. Não é conferência. O número 15 é identificador do artigo, não intervalo de páginas; PDF com 11 páginas.

## 23. Datasets citados e evidência indireta

**Página 4 · Tabela 3 — linhas Esteva, Han e Groh**

**Rótulos da área marcada:**

> Esteva et al. (2017): 129,450 images; Predominantly light skin tones Han et al. (2018): 49,567 images; Not stratified (region-based) Groh et al. (2021): Fitzpatrick17k dataset; Explicit (Fitzpatrick I–VI)

**Comentário:**

RQ2/RQ5/RQ6 — Transcrição dos campos de dataset/representação da Tabela 3. 129.450 imagens são de câncer de pele; 49.567, onicomicose; Fitzpatrick17k cobre condições dermatológicas gerais. Não são bases específicas de hanseníase apresentadas nesta revisão. Os números são reportados pela revisão, sem auditoria dos estudos primários. Tabela também inclui métodos de disentanglement, difusão, CNN/Grad-CAM e revisão multimodal de NTDs, com dados e estratos incompletos.

## 24. Hanseníase no diagnóstico diferencial

**Página 5 · Tabela 4 — Leprosy**

**Rótulos da área marcada:**

> Leprosy | Hypopigmented or erythematous plaques, nodules | Tinea, vitiligo, psoriasis | Subtle early lesions; sensory loss under-detected | Detection of lesion borders and texture changes

**Comentário:**

RQ1/RQ6 — A tabela descreve placas/nódulos e mimetizadores da hanseníase, propondo detecção de bordas e mudanças de textura como oportunidade para IA. São características e aplicações conceituais, não variáveis extraídas ou resultados de um classificador validado. A limitação referente à perda sensorial também não é resolvida por uma fotografia isolada neste estudo.
