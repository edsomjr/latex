---
tags: []
parent: 'A Machine Learning-Based Diagnosis of Leprosy: Study'
collections:
    - TCC_Leituras
$version: 189
$libraryID: 2
$itemKey: 5FBHG4QS

---
**Síntese e contribuição para o TCC — Ahikpa e Himabindu (2025)**

O artigo *A Machine Learning-Based Diagnosis of Leprosy: Study* apresenta uma revisão de aplicações de aprendizado de máquina ao diagnóstico de hanseníase, abrangendo imagens de lesões e dados clínicos estruturados. Reúne abordagens com CNNs, ResNet101, SVM, regressão logística, Random Forest e XGBoost, além de técnicas de segmentação e extração de características de textura, como GLCM, LBP e WLD.

Para nosso TCC, sua principal contribuição é organizar modelos, técnicas e limitações encontrados na literatura. A revisão aponta problemas recorrentes: conjuntos de dados pequenos, desequilíbrio de classes, diversidade populacional limitada, restrições de acesso aos dados e falta de padronização dos procedimentos de avaliação. Esses aspectos ajudam a orientar a análise dos estudos primários e o planejamento do experimento.

Embora apresente resultados elevados em alguns trabalhos, o artigo não permite concluir qual modelo é superior: os números vêm de estudos com dados e condições de avaliação diferentes. Também mistura resultados de modelos baseados em imagens com resultados obtidos apenas com metadados. Essa distinção deve ser preservada na síntese da nossa revisão.

Quanto ao foco em pele negra, não foram localizadas métricas estratificadas por tom de pele nem comparações quantitativas entre grupos. O artigo discute limitações de diversidade e generalização, mas não demonstra especificamente uma queda de desempenho em peles escuras. Portanto, contribui para identificar uma lacuna de avaliação, sem fornecer uma resposta quantitativa à nossa questão principal.

**Limitações identificadas na leitura**

Há inconsistências internas: a legenda da Figura 1 menciona 22 pacientes, enquanto outras partes informam 222; o estudo de Beesetty recebe valores de accuracy de 26.56% e 73.13% sem esclarecimento suficiente; e a tabela apresenta precision e recall para Jitendra \[17], embora a coluna de limitações afirme que apenas accuracy e F-Measure foram reportadas. Também não foi localizado um protocolo de busca e seleção suficientemente detalhado para caracterizar a revisão como sistemática.

**Conclusão para utilização no TCC**

Este artigo é útil como síntese secundária e apoio à discussão das limitações da literatura. Os valores de desempenho devem ser extraídos preferencialmente dos estudos originais já incluídos na nossa revisão, evitando reproduzir inconsistências ou contar o mesmo resultado duas vezes. Para o planejamento experimental, a leitura reforça a importância de documentar a origem e a composição dos dados, a separação entre treinamento e teste e, quando os dados permitirem, avaliar desempenho por tom de pele e generalização em bases externas.

**Registro de referências complementares**

Os candidatos identificados nas referências já constam na nossa seleção, exceto *Classification of Leprosy using Artificial Neural Networks and Machine Learning* e *Skin Diseases Detection using LBP and WLD—An Ensembling Approach*. Esses dois permanecem como candidatos à triagem complementar, sem inclusão automática.
