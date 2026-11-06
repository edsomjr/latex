---
tags: []
parent: 'Integrative Image Processing Framework for Enhanced Detection of Leprosy-Associated Chronic Wounds'
collections:
    - TCC_Leituras
$version: 315
$libraryID: 2
$itemKey: JJGN3BFV

---
# Mehta et al. (2026) — CO-WinF: respostas às RQs e notas de leitura

**Artigo:** Integrative Image Processing Framework for Enhanced Detection of Leprosy-Associated Chronic Wounds. Jalpa Mehta, Saraswati Mishra, Rashmi Nilesh Malvankar e Shwetambari Borade. *The International Journal of Lower Extremity Wounds*, 2026. DOI: 10.1177/15347346251412645.

**Fonte:** PDF fornecido pelo usuário, 12 páginas. As páginas abaixo são as páginas do PDF. Análise restrita ao conteúdo deste artigo; dados de trabalhos citados não foram tratados como experimentos dos autores. O PDF anotado é uma cópia independente; o original do Zotero foi preservado e as anotações não foram inseridas diretamente na biblioteca.

**Enquadramento para o TCC:** estudo metodológico experimental sobre análise/segmentação de feridas crônicas em pacientes com hanseníase. É pertinente se a revisão inclui complicações cutâneas/feridas associadas à doença. Não demonstra diagnóstico etiológico ou diferencial da hanseníase a partir de imagens. A presença de um módulo de classificação não substitui a necessidade de especificar classes e avaliar esse desfecho.

## RQ1. Quais técnicas de visão computacional são utilizadas para identificar manifestações dermatológicas associadas à hanseníase?

O framework **CO-WinF** tem três módulos:

*   **AINCE:** divisão em blocos, equalização adaptativa de histograma com limitação de contraste (CLAHE) e filtro bilateral que preserva bordas, para tratar iluminação desigual, contraste e ruído. Beta=0,15 é ajustado em subconjunto de validação (p. 5). A Figura 3 mostra saída em escala de cinza; não apresenta comparação RGB versus escala de cinza.
*   **MEPS:** segmentação multiescala baseada em U-Net, mapas de borda por gradientes tipo Sobel, atenção espacial sensível a bordas, conexões de salto enriquecidas e fusão de características rasas e profundas por concatenação/convolução 1×1.
*   **HSTFC:** extração de características profundas com CNN leve e descritores LBP/HOG, concatenados e ponderados por atenção antes do ensemble de classificação.

A manifestação avaliada é a **ferida crônica**, com máscaras binárias de ferida/fundo. Não há experimento que demonstre detecção de hanseníase entre doenças semelhantes. Albumentations consta entre bibliotecas, mas transformações de aumento de dados e suas probabilidades não são especificadas. Não há resolução final de entrada ou avaliação isolada quantitativa de cada pré-processamento claramente reportadas. Evidências: pp. 3–7 e 9; notas 2–7.

## RQ2. Quais conjuntos de dados e populações são utilizados no desenvolvimento e na avaliação desses modelos?

Utiliza **CO2Wounds-V2**, com **764 imagens RGB de smartphone**, coletadas de novembro de 2021 a agosto de 2023 (1 ano e 9 meses). A população descrita é de **96 pacientes com hanseníase**, sendo **18 mulheres e 78 homens**, idade média **75,5 ± 9,9 anos**.

| Conjunto    | Imagens | Anotações descritas                                 |
| ----------- | ------- | --------------------------------------------------- |
| Treinamento | 485     | Caixas delimitadoras e máscaras semânticas binárias |
| Validação   | 122     | Caixas delimitadoras e máscaras semânticas binárias |
| Teste       | 157     | Descrito como sem anotações                         |


As máscaras rotulam pixels como ferida ou fundo; o texto refere formato COCO. Fonte de dados indicada pelo artigo: [CO2Wounds-V2 no Mendeley Data](https://data.mendeley.com/datasets/s2w7rjwz49/2). O país, a instituição de coleta, a distribuição por fototipo/etnia e os pacientes em cada divisão não são especificados neste artigo. Não inferir esses dados da afiliação indiana dos autores. A expressão “lepromatous ulcers” aparece na limitação, mas não é acompanhada de documentação da classificação clínica dos 96 pacientes. HAM10000, PAD-UFES-20 e base brasileira aparecem como literatura comparativa, sem demonstração de uso no treinamento/teste de CO-WinF. Evidências: pp. 7–8 e 11; notas 9–11, 16–17.

## RQ3. Quais métodos, procedimentos são utilizados para avaliar o desempenho desses modelos e quais resultados são reportados?

Avaliação interna com divisão fixa de treino/validação/teste e curvas de acurácia/perda ao longo de **25 épocas**. Configuração: Python 3.9, PyTorch 1.10.0, XGBoost 1.4.2, semente 42, batch 16, quatro workers, Adam com learning rate 10⁻⁴ e weight decay 10⁻⁵, scheduler ReduceLROnPlateau. São descritos desktop Windows, Intel Core i7-10700K e 32 GB de RAM; a versão CUDA não estabelece por si só qual GPU foi usada.

São mostrados exemplos qualitativos das etapas e uma tabela de métricas por conjunto. O teste reporta acurácia 97,20%, precisão 94,50%, recall 95,10%, F1 92,50% e IoU 86,50%. Há comparação com resultados da literatura em diferentes bases/tarefas, sem protocolo comum de reexecução esclarecido. Não há ablação quantitativa que isole o ganho de AINCE, MEPS e HSTFC, validação cruzada, repetições com sementes diferentes, testes estatísticos ou intervalos de confiança.

**Ressalvas:** o artigo descreve o teste como não anotado e não explica como obteve rótulos de referência para as métricas. Não esclarece separação por paciente, unidade/agregação das métricas ou classes do HSTFC. A declaração “No data, models, or code were generated or used during the study” contradiz a metodologia experimental. Isso limita a auditabilidade e a reprodutibilidade; não é motivo para inventar um protocolo ausente. As alegações de eficiência, interpretabilidade e utilidade clínica não são acompanhadas de benchmark de tempo/memória, estudo de explicabilidade ou validação clínica prospectiva. Evidências: pp. 6–11; notas 8, 11–16 e 19.

## RQ4. Quais métricas são utilizadas para avaliar o desempenho desses modelos e quais resultados são reportados?

Transcrição da **Tabela 2, página 10**, em porcentagem:

| Métrica  | Treinamento | Validação | Teste |
| -------- | ----------- | --------- | ----- |
| Precisão | 96,12       | 94,98     | 94,50 |
| Recall   | 96,50       | 95,78     | 95,10 |
| F1-score | 95,20       | 93,10     | 92,50 |
| IoU      | 89,00       | 87,09     | 86,50 |
| Acurácia | 98,38       | 97,53     | 97,20 |


Acurácia e perda também aparecem nas curvas. O resumo destaca os valores de **validação**, e não os de teste. A tabela comparativa chama a última métrica de **mIoU**, enquanto a Tabela 2 a chama de **IoU**; o método de média não é esclarecido. Também não há definição suficiente para registrar acurácia como diagnóstico por paciente ou distinguir métricas de segmentação das do classificador HSTFC.

**Consistência numérica:** se calculado diretamente por 2PR/(P+R), o F1 seria aproximadamente 96,31% no treino, 95,38% na validação e 94,80% no teste, diferente de 95,20%, 93,10% e 92,50%. Médias por imagem/classe podem explicar diferenças entre métricas agregadas; o artigo não informa essa escolha. Portanto, os valores acima são os publicados, sem correção arbitrária. Não há AUC, especificidade ou métricas diagnósticas específicas de hanseníase apresentadas para CO-WinF. Valores de outros estudos na revisão não devem ser atribuídos ao método. Evidências: pp. 1, 8 e 10; notas 12–15.

## RQ5. Como o desempenho dos modelos varia entre diferentes grupos ou tons de pele?

**Não avaliado/reportado.** Embora informe sexo e idade da amostra, não apresenta resultados estratificados por sexo, idade, etnia, fototipo Fitzpatrick ou outro marcador de pigmentação. Não é possível quantificar diferenças entre grupos ou concluir equidade. Correção de iluminação e a expressão “diverse real-world conditions” não demonstram robustez entre tons de pele. Evidências contextuais: população na p. 7 e resultados agregados na p. 10; notas 3, 10 e 18. A ausência é conclusão da leitura do artigo, não uma declaração literal dos autores.

## RQ6. Quais modelos e abordagens de inteligência artificial são utilizados para identificar manifestações dermatológicas associadas à hanseníase?

**CO-WinF** integra processamento clássico de imagens, segmentação por deep learning e classificação híbrida:

*   **MEPS:** U-Net modificada com atenção orientada a bordas e fusão multiescala.
*   **HSTFC:** CNN leve não nomeada, LBP/HOG, fusão com atenção e árvores de gradient boosting; XGBoost é indicado como exemplo na formulação e consta no ambiente implementado.
*   **Desbalanceamento:** funções objetivo ponderadas e parâmetro scale-pos-weight, sem valores especificados.

AINCE é pré-processamento clássico, não uma rede separada de diagnóstico. Não há resultados por classes clínicas de hanseníase nem avaliação isolada do HSTFC. ResNeXt-50, ResNet101, EfficientNet, Segformer, ViT, SVM e outros modelos aparecem na comparação com literatura; isso não os torna componentes treinados de CO-WinF. Evidências: pp. 3–7 e 10; notas 5–7 e 16.

## RQ7. Como a capacidade de generalização dos modelos é avaliada, especialmente quando são utilizados conjuntos de dados diferentes daqueles empregados no treinamento?

A evidência apresentada é **interna ao CO2Wounds-V2**: comparação entre treino/validação/teste e inspeção de curvas. Não há avaliação de CO-WinF em base externa independente, outro centro/país, outras etiologias de ferida ou coorte clínica prospectiva. A tabela com vários datasets resume métodos da literatura e não configura experimento de transferência entre bases para o modelo proposto.

A generalização é limitada pela ausência de informação sobre separação por paciente, origem das anotações de teste e variabilidade estatística. Não são apresentados experimentos controlados de robustez a câmeras, iluminação ou pigmentação. Os autores reconhecem que a validação é específica às úlceras estudadas e propõem bases com diferentes feridas para avaliar generalização entre doenças em trabalho futuro. Portanto, “generalizável” deve ser registrado como alegação/proposta, não como comprovação externa. Evidências: pp. 8, 10–11; notas 11, 16–18.

## RQ8. O artigo foi publicado em que tipo de veículo de publicação? (revista, conferência)

**Revista científica:** *The International Journal of Lower Extremity Wounds*, publicada pela SAGE. O documento é identificado como **Original Article**, copyright 2026, DOI **10.1177/15347346251412645**. Esta versão tem 12 páginas e cabeçalhos 0(0), sem volume/número final informado. Não confundir com a conferência ICIP 2024, que é o veículo do artigo citado sobre CO2Wounds-V2. Evidência: p. 1, nota 1.

# Trechos e notas para o Zotero

Cada número corresponde a uma anotação no PDF. Os trechos textuais abaixo são literais, com quebras de linha/hifenização de fim de linha normalizadas. Nas tabelas, os valores são transcritos na ordem das colunas; suas escalas são explicadas em cada nota. Os comentários podem ser copiados diretamente para o Zotero.

## 01. Tipo de publicação

**Página 1 · Cabeçalho**

**Trecho grifado:**

> Original Article

**Comentário:**

RQ8 — Artigo original de periódico: The International Journal of Lower Extremity Wounds, SAGE, 2026. DOI 10.1177/15347346251412645. O PDF tem 12 páginas e cabeçalhos 0(0), sem volume/número definitivo indicado. Não é publicação em conferência.

## 02. Escopo da pesquisa

**Página 1 · Abstract**

**Trecho grifado:**

> Automated leprosy chronic wound analysis from smartphone-acquired images remains hindered by uneven illumination, indistinct lesion margins, and poor spatial–textural integration.

**Comentário:**

RQ1/RQ6 — CO-WinF analisa feridas crônicas associadas à hanseníase em fotografias de smartphone. A avaliação apresentada se concentra na segmentação de ferida versus fundo; não demonstra diagnóstico diferencial de hanseníase versus outras doenças ou pessoas saudáveis.

## 03. Pré-processamento

**Página 4 · AINCE**

**Trecho grifado:**

> Adaptive Illumination Normalization and Contrast Enhancement (AINCE) divides each image into tiles and applies Contrast-Limited Adaptive Histogram Equalization (CLAHE) to redistribute pixel intensities.

**Comentário:**

RQ1 — AINCE divide a imagem em blocos e aplica CLAHE para realçar contraste local e normalizar iluminação. O estágio seguinte usa filtro bilateral para reduzir ruído preservando bordas. Não confundir normalização de iluminação com validação entre tons de pele.

## 04. Filtro bilateral

**Página 4 · AINCE**

**Trecho grifado:**

> AINCE then employs an edge-preserving bilateral filter to smooth noise while maintaining critical lesion boundaries.

**Comentário:**

RQ1 — Filtragem bilateral após CLAHE. O método descreve parâmetros adaptados ao bloco; na página 5, beta=0,15 é ajustado em subconjunto de validação. Isso constitui ajuste interno, não validação externa.

## 05. Segmentação e atenção

**Página 5 · MEPS**

**Trecho grifado:**

> At its core, it integrates a U-Net-based architecture augmented with an edge-aware attention mechanism, which refines feature maps by emphasizing strong gradient transitions indicative of lesion borders.

**Comentário:**

RQ1/RQ6 — MEPS: U-Net multiescala com atenção orientada a bordas. Emprega gradientes tipo Sobel, conexões de salto enriquecidas com mapas de borda e fusão de características rasas/profundas para delimitar feridas.

## 06. Características profundas e texturais

**Página 6 · HSTFC**

**Trecho grifado:**

> HSTFC extracts deep features using a lightweight convolutional neural network (CNN) backbone optimized for efficiency while concurrently computing classical descriptors such as local binary patterns (LBP) and histograms of oriented gradients (HOG).

**Comentário:**

RQ1/RQ6 — HSTFC combina embeddings de CNN leve com LBP e HOG, por concatenação e pesos de atenção. O backbone não recebe nome comercial específico; não atribuir ResNet/MobileNet. As classes e resultados independentes desse classificador não estão claramente definidos.

## 07. Ensemble e desbalanceamento

**Página 6 · HSTFC**

**Trecho grifado:**

> via weighted objective functions and scale-pos-weight hyperparameters.

**Comentário:**

RQ6 — Classificação por ensemble de árvores com gradient boosting (XGBoost é citado como exemplo e aparece como biblioteca na implementação). Usa objetivos ponderados/scale-pos-weight. Não informa valores desses pesos, distribuição de classes ou resultados isolados do classificador.

## 08. Treinamento

**Página 7 · Implementation Setup**

**Trecho grifado:**

> Training utilized the Adam optimizer (initial learning rate 1×10−4, weight decay 1×10−5) alongside a ReduceLROnPlateau scheduler to adaptively lower the learning rate.

**Comentário:**

RQ3 — Adam, learning rate 0,0001, weight decay 0,00001 e ReduceLROnPlateau; batch 16, quatro workers e semente 42 (mesmo parágrafo). Curvas de treino/validação abrangem 25 épocas. Não há validação cruzada, repetições ou intervalos de confiança relatados.

## 09. Base e divisão

**Página 7 · Dataset Description**

**Trecho grifado:**

> This comprehensive dataset comprises 764 RGB images that reflect real-world clinical conditions, acquired over 1 year and 9 months (November 2021 to August 2023) using smartphone cameras. The images are organized into three distinct splits: 485 images for training, 122 for validation, and 157 unlabelled images reserved for testing

**Comentário:**

RQ2/RQ3 — CO2Wounds-V2: 764 imagens RGB; 485 treino, 122 validação e 157 teste descritas como sem rótulos. Coleta entre novembro/2021 e agosto/2023, em smartphones. Não informa neste artigo país/instituição de coleta nem se a separação impede imagens do mesmo paciente em conjuntos diferentes.

## 10. População

**Página 7 · Dataset Description**

**Trecho grifado:**

> Captured from 96 leprosy patients, of which 18 were female and 78 were male, with an average age of approximately 75.5 years (±9.9 years)

**Comentário:**

RQ2/RQ5 — 96 pacientes: 18 mulheres, 78 homens; idade média 75,5 ± 9,9 anos. Não há distribuição por fototipo/etnia nem métricas estratificadas por sexo, idade ou pigmentação. 764 imagens não equivalem a 764 pacientes.

## 11. Rótulos e problema do teste

**Página 8 · Dataset Description**

**Trecho grifado:**

> training and validation sets feature detection bounding boxes and binary semantic segmentation masks for each image, labeling each pixel as part of a wound or background. The testing set is provided without annotations for unbiased performance evaluation.

**Comentário:**

RQ2/RQ3/RQ7 — Treino/validação têm caixas e máscaras binárias ferida/fundo. O teste é descrito como não anotado, mas a Tabela 2 reporta métricas supervisionadas de teste. Não explica acesso a ground truth oculto, servidor de avaliação ou anotação adicional. Portanto, a procedência dessas métricas de teste fica insuficientemente esclarecida.

## 12. Resultados da validação

**Página 8 · Performance of the Proposed Model**

**Trecho grifado:**

> The precision reached 94.98% and recall 95.78%, with an F1 Score of 93.10% and an IoU Score of 87.09%.

**Comentário:**

RQ4 — Validação: precisão 94,98%; recall 95,78%; F1 93,10%; IoU 87,09%; acurácia 97,53% na Tabela 2. O F1 calculado diretamente desses valores de precisão/recall seria aproximadamente 95,38%, não 93,10%. Médias por imagem/classe podem diferir do cálculo agregado, mas o artigo não especifica a agregação; preservar os números publicados e assinalar a ambiguidade.

## 13. Resultados do teste

**Página 8 · Performance of the Proposed Model**

**Trecho grifado:**

> In the testing phase, the metrics remain comparable to the validation results, with a precision of 94.50%, recall of 95.10%, F1 Score of 92.50%, and IoU Score of 86.50%.

**Comentário:**

RQ3/RQ4 — Teste reportado: precisão 94,50%; recall 95,10%; F1 92,50%; IoU 86,50%; acurácia 97,20% (Tabela 2). São valores declarados, com protocolo de ground truth não esclarecido. Não são sensibilidade/acurácia diagnóstica para reconhecer hanseníase em novos pacientes.

## 14. Treino

**Página 8 · Performance of the Proposed Model**

**Trecho grifado:**

> The high Precision and Recall percentages during training of 96.12% and 96.50%, respectively

**Comentário:**

RQ4 — Treino: precisão 96,12%; recall 96,50%; F1 95,20%; IoU 89,00%; acurácia 98,38% (Tabela 2). Métricas de treinamento não são estimativas independentes de generalização.

## 15. Acurácia por conjunto

**Página 10 · Tabela 2**

**Trecho grifado:**

> Accuracy 98.38 97.53 97.20

**Comentário:**

RQ4 — Linha da Tabela 2, na ordem treino/validação/teste (%): 98,38 / 97,53 / 97,20. A unidade de cálculo da acurácia não é explicitada; no contexto de máscaras binárias, não interpretar como percentual de pacientes corretamente diagnosticados. IoU é chamado mIoU em outras partes sem detalhamento da média.

## 16. Comparação com literatura

**Página 8 · Comparative Performance Analysis**

**Trecho grifado:**

> The comparative performance table provides a comprehensive evaluation of various state-of-the-art techniques across multiple datasets, including HAM10000, CO2Wounds, the Brazilian leprosy dataset, and PAD-UFES-20.

**Comentário:**

RQ3/RQ7 — A tabela comparativa reúne técnicas de referências em diferentes bases/tarefas. A linha do modelo proposto é apenas CO2Wounds. Não demonstra treinamento/teste de CO-WinF em HAM10000, PAD-UFES-20 ou na base brasileira; não é validação externa. Não há protocolo comum de reexecução esclarecido.

## 17. Restrição da validação

**Página 11 · Limitação antes da conclusão**

**Trecho grifado:**

> Therefore, while the framework is inherently extendable to other chronic wounds, the present validation remains specific to lepromatous ulcers.

**Comentário:**

RQ2/RQ7 — Autores limitam a validação a úlceras que denominam lepromatosas. O texto não detalha confirmação/subtipagem dos 96 pacientes, portanto essa expressão não prova que todos tinham hanseníase lepromatosa. Aplicação a outras feridas permanece proposta.

## 18. Generalização futura

**Página 11 · Conclusion**

**Trecho grifado:**

> As part of future work, this research can be extended by incorporating multi-wound datasets to evaluate cross-disease generalisation and fine-tune the architecture for broader clinical adoption.

**Comentário:**

RQ7 — Generalização entre doenças e bases com múltiplos tipos de ferida é trabalho futuro. Não há teste externo, multicêntrico, prospectivo clínico ou estratificação por dispositivo/iluminação/tom de pele demonstrados. Diferenças pequenas entre treino e validação não bastam para comprovar robustez clínica.

## 19. Contradição de disponibilidade

**Página 11 · Data Availability**

**Trecho grifado:**

> No data, models, or code were generated or used during the study

**Comentário:**

RQ2/RQ3 — A declaração afirma que nenhum dado/modelo/código foi gerado ou usado, contradizendo a descrição de experimentos com CO2Wounds-V2, PyTorch e XGBoost. Registrar como inconsistência de relato; não concluir ausência real de experimentos nem inventar disponibilização de código/pesos.
