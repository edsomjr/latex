---
tags: []
parent: 'A Machine Learning-Based Diagnosis of Leprosy: Study'
collections:
    - TCC_Leituras
$version: 191
$libraryID: 2
$itemKey: WB7PZT7J

---
**Extração por perguntas de pesquisa — Ahikpa e Himabindu (2025)**

**Artigo:** *A Machine Learning-Based Diagnosis of Leprosy: Study*.\
**Tipo:** revisão de literatura. Os resultados apresentados são provenientes de estudos citados, não de experimentos próprios dos autores.

**1. Quais técnicas de visão computacional são utilizadas para identificar manifestações dermatológicas associadas à hanseníase?**

A revisão descreve extração de características por CNNs, descritores de textura GLCM, LBP e WLD, transformada DCT e segmentação de regiões de interesse por Fuzzy C-Means orientado pela heurística Firefly. Também apresenta combinação de características GLCM com características profundas de ResNet101. Entre os procedimentos de preparação das imagens, menciona recorte, redimensionamento, conversão para escala de cinza e aumento de dados por espelhamento, rotação e mudança de escala.

**Referência:** Ahikpa e Himabindu (2025), p. 2, seção II.A; pp. 3–4, seção II.B e Tabela I.

**2. Quais conjuntos de dados e populações são utilizados no desenvolvimento e na avaliação desses modelos?**

São relatadas imagens de DermNetNZ e buscas no Google, além de conjuntos clínicos de instituições brasileiras e indianas. Para Barbieri et al., a revisão informa **222 pacientes e 1.229 imagens**, acompanhadas de dados demográficos e clínicos. Para Jitendra \[18], informa **220 imagens**, sem esclarecer o número de pacientes. Beesetty utilizou dados coletados com o Sivananda Rehabilitation Home, em Hyderabad, com participantes de diferentes distritos de Telangana. Banerjee utilizou imagens de pacientes ambulatoriais de uma instituição em Kolkata.

A composição por tom de pele e o número de lesões distintas não são detalhados. Os 1.000 participantes mencionados para Beesetty constituíam uma meta de recrutamento, não a amostra final. Há divergência na legenda da Figura 1, que informa 22 pacientes, enquanto o texto e a tabela informam 222.

**Referência:** Ahikpa e Himabindu (2025), p. 2, seção II.A; p. 3, legenda da Figura 1; p. 4, Tabela I.

**3. Quais métodos, procedimentos são utilizados para avaliar o desempenho desses modelos e quais resultados são reportados?**

O artigo compara resultados publicados em estudos anteriores, sem realizar avaliação própria sob um protocolo comum. Para Barbieri, descreve **182 pacientes para treinamento e 40 para teste**, além de execuções repetidas dos modelos. Relata accuracy de **81.3% para LR, 80.8% para XGB e 77.9% para RF**, com desvios-padrão de **0.058, 0.06 e 0.088**, respectivamente.

Para Baweja e Parhar, compara arquiteturas CNN com diferentes quantidades de filtros: accuracy média de **91.6%**, contra **69.4%** na arquitetura com menos filtros. Também compara SVM, LR e ANN no estudo de Mehta, com accuracy de **97.80%, 95.80% e 95.56%**, respectivamente.

Número de repetições, detalhes de validação cruzada e procedimentos de separação dos dados para todos os estudos: **Não localizado no PDF — requer conferência manual**. A revisão reconhece que a falta de padronização dificulta comparações entre estudos.

**Referência:** Ahikpa e Himabindu (2025), pp. 2–3, seções II.A e II.B; p. 3, Figura 1.

**4. Quais métricas são utilizadas para avaliar o desempenho desses modelos e quais resultados são reportados?**

A revisão apresenta accuracy, precision, recall, F1/F-Measure e AUC. Sensitivity e specificity são mencionadas, mas seus valores não são fornecidos no relato de Barbieri.

| Estudo citado / modelo                 | Resultados relatados pela revisão                                                                          |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Baweja e Parhar — CNN                  | Accuracy: **91.6%**; arquitetura com menos filtros: **69.4%**.                                             |
| Barbieri — LR, XGB e RF                | Accuracy: **81.3%, 80.8% e 77.9%**, respectivamente. AUC de **88.6%** para LR com metadados.               |
| Mehta — SVM, LR e ANN                  | Accuracy: **97.80%, 95.80% e 95.56%**, respectivamente.                                                    |
| Jitendra \[17] — ResNet101/GLCM e RF   | Accuracy: **97.20%**; precision: **99.69%**; recall: **95.82%**; F1: **97.80%**.                           |
| Jitendra \[18] — RF/GLCM               | Accuracy: **92.7%**; precision: **89.5%**; recall: **92.1%**; F1: **94%**.                                 |
| Beesetty — baseline/nearest neighbor   | Accuracy: **26.56%** na p. 2 e **73.13%** na p. 3 e na tabela, sem esclarecimento suficiente da diferença. |
| Banerjee — SVM multiclasse com LBP/WLD | Accuracy: **83.97%**, sem resultado específico de hanseníase claramente identificado.                      |


Os resultados de Barbieri destacados na tabela são caracterizados como baseados em metadados. A tabela também contém uma contradição para Jitendra \[17]: apresenta precision e recall, mas afirma, nas limitações, que apenas accuracy e F-Measure foram reportadas. Os valores devem ser tratados como informações da revisão, pendentes de conferência nos estudos originais quando utilizados na síntese quantitativa.

**Referência:** Ahikpa e Himabindu (2025), pp. 2–3, seção II; p. 4, Tabela I.

**5. Como o desempenho dos modelos varia entre diferentes grupos ou tons de pele?**

Resultados quantitativos por grupo ou tom de pele: **Não localizado no PDF — requer conferência manual**. O artigo discute qualitativamente a pouca atenção às variações culturais, étnicas e geográficas e à diversidade dos conjuntos de dados. Não apresenta classificação de tons de pele nem métricas estratificadas que permitam medir diferenças de desempenho.

**Referência:** Ahikpa e Himabindu (2025), p. 3, seção III, *Discussion*.

**6. Quais modelos e abordagens de inteligência artificial são utilizados para identificar manifestações dermatológicas associadas à hanseníase?**

A revisão reúne CNNs, SVM, regressão logística, Random Forest, XGBoost, ANN e nearest neighbor. Descreve uma abordagem híbrida com ResNet101, características GLCM e classificação por Random Forest; uma abordagem de few-shot learning no estudo de Beesetty; e SVM multiclasse com descritores LBP/WLD no estudo de Banerjee. Também apresenta modelos baseados em metadados e combinação de imagens com dados clínicos.

Nem todos os resultados descritos correspondem a modelos exclusivamente baseados em imagens. A revisão não detalha suficientemente as arquiteturas, o pré-treinamento e os hiperparâmetros de todos os trabalhos.

**Referência:** Ahikpa e Himabindu (2025), p. 2, seção II; p. 3, Figura 1; p. 4, Tabela I.

**7. Como a capacidade de generalização dos modelos é avaliada, especialmente quando são utilizados conjuntos de dados diferentes daqueles empregados no treinamento?**

Avaliação explícita entre datasets distintos ou validação externa em outra instituição ou população: **Não localizado no PDF — requer conferência manual**.

O artigo descreve um grupo separado de teste para Barbieri e aumento de dados para Jitendra \[18], mas não apresenta resultados de avaliação entre bases. Discute amostras pequenas, desequilíbrio, diversidade limitada e sobreajuste como obstáculos à generalização. O aumento de dados é apresentado como estratégia de treinamento, sem demonstrar, por si só, desempenho em dados externos.

**Referência:** Ahikpa e Himabindu (2025), p. 2, seção II.A; p. 3, Figura 1 e seção III; p. 4, seção IV.

**8. O artigo foi publicado em que tipo de veículo de publicação? (revista, conferência)**

Foi publicado em **conferência**, na *2025 IEEE International Conference on Emerging Trends in Computing and Communication (ETCOM)*, realizada em Mangalore, Índia, em 28–29 de novembro de 2025, conforme o cabeçalho do PDF.

**Referência:** Ahikpa e Himabindu (2025), p. 1, cabeçalho.

**Referência bibliográfica do artigo analisado**

AHIKPA, Etienne Djidji; HIMABINDU, K. *A Machine Learning-Based Diagnosis of Leprosy: Study*. In: 2025 IEEE International Conference on Emerging Trends in Computing and Communication (ETCOM). IEEE, 2025. p. 1–5. DOI: 10.1109/ETCOM66606.2025.11436464.
