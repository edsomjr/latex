---
tags: []
parent: 'A Machine Learning-Based Diagnosis of Leprosy: Study'
collections:
    - TCC_Leituras
$version: 190
$libraryID: 2
$itemKey: 4EDR4T8A

---
# RQs e partes grifadas

***

**1. Tipo de estudo — página 1, seção II, “RELATED WORKS”**

**Grifar:**

> This study conducted a review to showcase the various Machine learning algorithms used for Leprosy detection.

**Comentário:**\
Tipo de estudo: revisão de literatura. Os autores sintetizam trabalhos anteriores; os resultados apresentados não correspondem a um experimento próprio. O resumo pode causar ambiguidade, mas esta seção identifica explicitamente o trabalho como revisão.

***

**2. Escopo da revisão — página 1, seção II**

**Grifar:**

> The goal of the study is to collect all the existing papers on AI/ML for leprosy diagnosis in the African and Asian populations between 2011 and 2024 to ensure relevance to current advancements in medical image processing and AI-based diagnostics.

**Comentário:**\
Escopo declarado: estudos de 2011 a 2024 sobre IA/ML no diagnóstico de hanseníase em populações africanas e asiáticas. Atenção: o parágrafo também menciona Brasil posteriormente. Não localizei descrição suficiente de bases, strings e processo de seleção para caracterizar esta revisão como sistemática.

***

**3. Técnicas de segmentação e aumento de dados — página 2, seção II.A**

**Grifar:**

> They used flipping, rotation, and scaling of images to create variability in the training set.

**Comentário:**\
RQ1 e RQ7 — A revisão atribui ao estudo de Jitendra \[18] aumento de dados por espelhamento, rotação e mudança de escala. É uma estratégia para aumentar a variabilidade do treinamento; não constitui evidência de avaliação em dataset externo.

**Grifar também:**

> Since the methodology focuses on ROI segmentation using a Fuzzy C-Means (FCM) clustering algorithm driven by the Firefly heuristic, each image included a region of interest (ROI).

**Comentário:**\
RQ1 — Segmentação de região de interesse (ROI) por Fuzzy C-Means orientado pela heurística Firefly, conforme descrição do estudo de Jitendra \[18]. Informação relatada pela revisão.

***

**4. Pré-processamento e extração de características — página 2, seção II.A**

**Grifar:**

> Banerjee and al. standardized image dimensions by resizing and cropping the lesion areas to 144\*144 pixels. Then, the images were converted to grayscale to simplify the processing and reduce computational load.

**Comentário:**\
RQ1 — No estudo de Banerjee \[20], a revisão descreve redimensionamento e recorte das lesões para 144 × 144 pixels, seguidos de conversão para escala de cinza.

**Grifar também:**

> The Discrete Cosine Transform (DCT) was one of the methods used to extract features for images.

**Comentário:**\
RQ1 — A revisão também atribui a Banerjee \[20] extração de características por DCT. A tabela destaca LBP e WLD; preservar essas informações como descrições da revisão, sem assumir que a tabela apresenta todo o processamento.

***

**5. Dataset de Barbieri — página 2, seção II.A**

**Grifar:**

> Barbieri and al. used high-resolution data from 222 patients (1229 images), including their demographic information and skin lesion photos. That dataset, for privacy reasons, access is limited and requires registration and ethical permission.

**Comentário:**\
RQ2 — Barbieri \[15]: 222 pacientes e 1.229 imagens, com fotografias de lesões e informações demográficas. Acesso descrito como restrito, com registro e autorização ética. Pacientes e imagens são unidades diferentes; não há aqui contagem de lesões distintas.

***

**6. População de Beesetty e tamanho planejado da amostra — página 2, seção II.A**

**Grifar:**

> Patients were enrolled from multiple districts across Telangana through SRH-organized leprosy camps. The initial aim was to collect images from 1,000 participants (500 with confirmed leprosy and 500 with leprosy-like conditions), but data collection was interrupted by the COVID-19 pandemic, resulting in a limited dataset.

**Comentário:**\
RQ2 — Beesetty \[19]: participantes de vários distritos de Telangana, recrutados em atividades organizadas pelo SRH. Os 1.000 participantes eram uma META, não a amostra final. O tamanho efetivamente coletado não está informado neste trecho. A localização geográfica não permite inferir tom de pele.

***

**7. Dataset de Jitendra — página 2, seção II.A**

**Grifar:**

> In their work “Heuristic Segmentation Assisted Deep-Spatial Feature Learning Model for Leprosy Detection,” Jitendra and al. (2024) used a clinically acquired dataset of 220 leprosy lesion images.

**Comentário:**\
RQ2 — A revisão atribui 220 imagens ao estudo de Jitendra \[18]. Não confundir com 220 pacientes ou 220 lesões distintas. O texto seguinte menciona imagens de hanseníase ou pele normal; a distribuição entre classes não fica esclarecida.

***

**8. Repetições e variabilidade dos resultados — página 2, seção II.A**

**Grifar:**

> To show the stability of the model, they ran the models multiple times and calculated a standard deviation, which gave 0.058,0.06,0.088, respectively.

**Comentário:**\
RQ3 — Para Barbieri \[15], a revisão relata execuções repetidas e desvios-padrão de 0.058, 0.06 e 0.088, respectivamente para LR, XGB e RF, conforme a ordem do parágrafo anterior. Número de execuções e procedimento detalhado não informados. Não interpretar automaticamente como validação cruzada.

***

**9. Divisão de treinamento e teste — página 3, legenda da Figura 1**

**Grifar:**

> Comprehensive data modeling summary encompassing the complete dataset of 22 patient records. Images (model 1) or metadata (model 2) from 182 patients were used to train the algorithms in a training dataset, while 40 patients were kept as a testing group for validation in model 3.

**Comentário:**\
RQ2, RQ3 e RQ7 — A figura, atribuída a Barbieri \[15], descreve 182 pacientes para treinamento e 40 para teste. Há inconsistência: a legenda começa com 22 registros, enquanto o texto e a tabela informam 222 pacientes, compatíveis com 182 + 40. Registrar a divergência sem corrigir silenciosamente. O teste não está identificado como validação em dataset externo.

***

**10. Modelos e resultados — página 4, Tabela I**

**Grifar:** Nas linhas abaixo, selecione as células “Algorithm Used” e “Evaluation Metrics (%)”. Crie uma anotação por linha.

**Linha Baweja and Parhar \[14] — comentário:**\
RQ4 e RQ6 — CNN: accuracy de 91.6%, conforme síntese da revisão. A seção II.A também relata 69.4% para uma arquitetura com menos filtros. Não são experimentos próprios deste artigo.

**Linha Barbieri et al. \[15] — comentário:**\
RQ4 e RQ6 — LR: accuracy de 81.3%; XGBoost: 80.8%; RF: 77.9%. A coluna “Key Results” caracteriza os resultados como modelos apenas com metadados. Não registrar esses valores como desempenho de modelos exclusivamente baseados em imagens.

**Linha Jalpa Metha \[16] — comentário:**\
RQ4 e RQ6 — Accuracy: LR 95.80%, SVM 97.80% e ANN 95.56%. A tabela não informa o nome do dataset; modalidade dos dados e conjunto de avaliação precisam de esclarecimento.

**Linha R. Jitendra et al. \[17] — comentário:**\
RQ1, RQ4 e RQ6 — Abordagem híbrida com ResNet101, características GLCM e Random Forest. Resultados: accuracy 97.20%, precision 99.69%, recall 95.82% e F1 97.80%. Contradição interna: a coluna de limitações afirma que o estudo reporta apenas accuracy e F-Measure.

**Linha R. Jitendra et al. \[18] — comentário:**\
RQ4 e RQ6 — RF com características GLCM: accuracy 92.7%, precision 89.5%, recall 92.1% e F1 94%. A forma de agregação das métricas não está esclarecida; conferir antes de interpretar sua relação.

**Linha R. Beesetty \[19] — comentário:**\
RQ4 e RQ6 — A tabela atribui accuracy de 73.13% a baselines/Nearest Neighbor. Na página 2, o texto informa 26.56% para Baseline1 no teste. O PDF não esclarece se são configurações distintas ou erro de relato; manter a divergência registrada.

**Linha Banerjee et al. \[20] — comentário:**\
RQ1, RQ4 e RQ6 — SVM multiclasse com características LBP/WLD: accuracy de 83.97%. Não há identificação clara de resultado separado para hanseníase; não atribuir automaticamente esse valor ao desempenho específico nessa doença.

***

**11. Resultado de AUC com metadados — página 3, continuação da seção II.B**

**Grifar:**

> In studies that used structured metadata rather than images \[figure 1], Barbieri and al. reported an AUC of 88.6% using Logistic Regression

**Comentário:**\
RQ4 — A revisão relata AUC de 88.6% para Logistic Regression com metadados estruturados. Manter essa modalidade explícita e preservar a apresentação percentual usada no artigo. Não atribuir o resultado a um modelo exclusivamente de imagens.

***

**12. Diversidade populacional e tons de pele — página 3, seção III**

**Grifar:**

> Cultural, ethnic, and geographical variations in skin conditions are rarely addressed, which limits model performance outside the original sample group.

**Comentário:**\
RQ5 — Discussão qualitativa sobre diversidade e desempenho fora da população original. Não apresenta métricas por grupo, classificação de tom de pele ou comparação entre tons. Portanto, este trecho sustenta uma limitação apontada pelos autores, não uma diferença quantitativa demonstrada.

***

**13. Limitações de generalização — página 3, seção III**

**Grifar:**

> With few publicly available image repositories and significant data imbalance, many models suffer from overfitting and cannot generalize across broader populations.

**Comentário:**\
RQ7 — Os autores apontam escassez de dados públicos, desequilíbrio e sobreajuste como limitações de generalização. Não apresentam aqui experimento entre datasets que quantifique essa limitação. Validação externa/cross-dataset: não localizada no PDF.

***

**14. Limitação da comparação entre estudos — página 3, seção II.B**

**Grifar:**

> Lack of standardization in feature extraction methods, preprocessing steps, and evaluation protocols made cross-study comparison difficult.

**Comentário:**\
RQ3 e interpretação dos resultados — A própria revisão reconhece diferenças entre extração de características, pré-processamento e protocolos de avaliação. Não usar as accuracies da Tabela I como ranking direto de superioridade entre modelos avaliados em condições distintas.

***

**15. Veículo de publicação — página 1, cabeçalho**

**Grifar:**

> 2025 IEEE International Conference on Emerging Trends in Computing and Communication (ETCOM)

**Comentário:**\
RQ8 — Artigo publicado em conferência: IEEE ETCOM 2025. O cabeçalho informa Mangalore, Índia, em 28–29 de novembro de 2025. Tipo de estudo: revisão; tipo de veículo: conferência.
