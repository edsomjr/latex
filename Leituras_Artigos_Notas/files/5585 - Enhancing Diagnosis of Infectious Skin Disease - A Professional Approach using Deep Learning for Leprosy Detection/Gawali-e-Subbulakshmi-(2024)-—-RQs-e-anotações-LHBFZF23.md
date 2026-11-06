---
tags: []
parent: 'Enhancing Diagnosis of Infectious Skin Disease: A Professional Approach using Deep Learning for Leprosy Detection'
collections:
    - TCC_Leituras
$version: 287
$libraryID: 2
$itemKey: LHBFZF23

---
# Gawali e Subbulakshmi (2024) — RQs e anotações

**Artigo:** *Enhancing Diagnosis of Infectious Skin Disease: A Professional Approach using Deep Learning for Leprosy Detection*.\
**Autores:** Chetan Jitendra Gawali e S. Subbulakshmi.\
**Veículo:** 2024 15th International Conference on Computing Communication and Networking Technologies (ICCCNT), IEEE.\
**DOI:** 10.1109/ICCCNT61001.2024.10725616.\
**Fonte da extração:** PDF fornecido, sete páginas. As páginas abaixo correspondem à posição no PDF.

A cópia anotada contém 25 grifos com comentários em português. O arquivo original do Zotero foi preservado. As anotações estão incorporadas à cópia PDF; não foram inseridas diretamente no banco de dados do Zotero. Os trechos transcritos ao final correspondem aos grifos, com quebras de linha e hifenização tipográfica normalizadas. A marcação do veículo abrange a margem editorial vertical.

**Tipo de estudo:** experimento computacional de classificação binária de imagens em hanseníase versus não hanseníase. O resumo declara foco na hanseníase tuberculoide, mas não apresenta classificação entre subtipos. Não é validação clínica prospectiva. As respostas distinguem resultados apresentados, alegações dos autores e informações não relatadas.

## RQ1. Quais técnicas de visão computacional são utilizadas para identificar manifestações dermatológicas associadas à hanseníase?

São utilizadas CNNs com transferência de aprendizado e extração de características a partir de pesos pré-treinados no ImageNet: VGG16, MobileNet v1, Xception v1 e EfficientNet B0. As camadas superiores originais são removidas para adaptação à classificação binária. A abordagem principal usa EfficientNet B0 como extrator de características e uma cabeça de classificação descrita com camadas densas (p. 3–5; anotações 4, 8 e 9).

O pré-processamento declara entrada **128 × 128 pixels, RGB**, também representada na Figura 1. Entretanto, a seção de pré-processamento cita **224 × 224 como exemplo** e apresenta intervalos de normalização 0–1 ou −1 a 1 sem definir claramente qual foi empregado. Isso limita a reprodução da implementação (p. 3–4; anotações 5 e 6).

O aumento de dados de treinamento inclui reescala, zoom, rotação e alterações de brilho; o texto acrescenta saturação e variação aleatória da intensidade de cor. Não são detalhadas faixas, probabilidades ou quantidades geradas. Não localizei segmentação de lesões/ROI ou máscaras como etapa experimental. Técnicas de explicabilidade são propostas como trabalho futuro; não devem ser atribuídas ao método por aparecerem na revisão de trabalhos relacionados (p. 3–4 e 6; anotações 7 e 16).

## RQ2. Quais conjuntos de dados e populações são utilizados no desenvolvimento e na avaliação desses modelos?

O artigo informa um dataset público do **Kaggle**, com **1.476 imagens**. No mesmo parágrafo, informa **1.476 para treino, 62 para validação e 62 para teste**. A soma dessas parcelas é **1.600**, incompatível com o total declarado. Não há explicação suficiente para resolver a diferença ou atribuí-la a aumento de dados (p. 3; anotações 2 e 3).

Não localizei identificação inequívoca do dataset por nome, URL, versão ou autoria, nem contagens por classe e por subconjunto. A tarefa é hanseníase versus não hanseníase, mas a composição clínica da classe negativa não é suficientemente caracterizada.

Não são informados número de pacientes, número de lesões únicas, procedência geográfica das imagens, distribuição etária, sexo, etnia, tons de pele ou procedimento de confirmação clínica/rotulagem. A motivação e as afiliações indianas não permitem concluir que os participantes sejam indianos. Também não se esclarece se várias imagens de um paciente ou lesão foram mantidas no mesmo subconjunto.

O **ImageNet** é utilizado para pré-treinamento das redes; não constitui uma população clínica de avaliação de hanseníase nem validação externa do classificador.

## RQ3. Quais métodos, procedimentos são utilizados para avaliar o desempenho desses modelos e quais resultados são reportados?

O procedimento declarado é uma divisão interna em treino, validação e teste, com comparação entre quatro arquiteturas. Os quantitativos têm a inconsistência descrita na RQ2. Não localizei validação cruzada, repetições com sementes diferentes, intervalos de confiança, testes de significância ou descrição de separação por paciente/lesão e deduplicação (p. 3 e 5).

Para a abordagem EfficientNet B0, o texto descreve Adam, taxa de aprendizado **0,01**, **hinge loss**, regularização L1/L2, máximo de **20 épocas** e early stopping por acurácia de validação, com paciência de **20 épocas** e restauração do melhor modelo. Teto e paciência iguais não documentam efetiva parada antecipada antes do limite. A página 6 menciona resultados após **15 épocas**, sem esclarecer a relação com o checkpoint ou a duração efetiva (anotações 10–12).

Não são suficientemente especificados batch size, coeficientes de regularização, congelamento das camadas e hiperparâmetros completos dos comparadores. Parte da descrição de suas cabeças usa termos hipotéticos como “likely” e “might”.

Na Tabela I, EfficientNet B0 apresenta o maior F1 (**0,9217**), MobileNet v1 a maior precisão (**0,9592**) e VGG16 a maior revocação (**0,9474**). Na Tabela II, VGG16 apresenta a maior acurácia de validação (**0,95**), contra **0,90** de EfficientNet B0. Portanto, o modelo favorecido pelos autores não lidera todas as métricas. A identificação do subconjunto da Tabela I não é inequívoca; não a registrar automaticamente como resultado confirmado de teste. Os valores completos estão na RQ4.

## RQ4. Quais métricas são utilizadas para avaliar o desempenho desses modelos e quais resultados são reportados?

As métricas apresentadas são **precision (precisão), recall (revocação/sensibilidade), F1-score e accuracy (acurácia)**. Os valores abaixo preservam a escala 0–1 do artigo.

**Tabela I — página 5; anotações 17–20.** O subconjunto de avaliação não é identificado inequivocamente no trecho que apresenta a tabela.

| Modelo          | Precision | Recall | F1-score |
| --------------- | --------- | ------ | -------- |
| VGG16           | 0,7714    | 0,9474 | 0,8504   |
| MobileNet V1    | 0,9592    | 0,8246 | 0,8868   |
| Xception        | 0,8947    | 0,8947 | 0,8947   |
| EfficientNet B0 | 0,9138    | 0,9298 | 0,9217   |


**Tabela II — página 6; anotações 21–24.** Resultados explicitamente rotulados como treino e validação, acompanhados de parâmetros treináveis.

| Modelo          | Acurácia de treino | Acurácia de validação | Parâmetros treináveis |
| --------------- | ------------------ | --------------------- | --------------------- |
| VGG 16          | 0,98               | 0,95                  | 50.343.937            |
| MobileNet       | 0,95               | 0,85                  | 1.050.625             |
| Xception        | 0,90               | 0,70                  | 2.099.201             |
| EfficientNet B0 | 0,95               | 0,90                  | 164.097               |


**Divergência importante:** o resumo chama **0,9138 de accuracy**, enquanto a Tabela I e a conclusão o identificam como **precision**. Registrar 91,38% como precisão na Tabela I e preservar a divergência; não tratá-lo como acurácia de teste comprovada (anotação 13).

Os parâmetros treináveis são uma medida de tamanho da parte ajustada do modelo, não uma métrica de desempenho diagnóstico. Não equivalem necessariamente ao total de parâmetros, ao tamanho do arquivo, a FLOPs, à latência ou ao consumo energético. Não localizei resultados de AUC, especificidade, contagens brutas de matriz de confusão, suporte por classe ou intervalos de confiança. A saída linear também não implica probabilidade calibrada.

## RQ5. Como o desempenho dos modelos varia entre diferentes grupos ou tons de pele?

**Não avaliado/reportado.** O artigo não apresenta desempenho estratificado por tom de pele, etnia, sexo, idade ou outro grupo populacional; também não caracteriza a distribuição desses atributos no dataset. Não é possível concluir que o desempenho seja equivalente entre grupos.

Alterações de brilho, saturação e intensidade de cor no aumento de dados não substituem uma avaliação em grupos de tons de pele documentados. A validação em datasets maiores e mais diversos aparece como trabalho futuro (p. 6; anotação 16).

## RQ6. Quais modelos e abordagens de inteligência artificial são utilizados para identificar manifestações dermatológicas associadas à hanseníase?

São comparadas **VGG16, MobileNet v1, Xception v1 e EfficientNet B0**, com transferência de aprendizado do ImageNet. A abordagem enfatizada é EfficientNet B0 como extrator de características, obtido via TensorFlow Hub, seguido por camada densa de **128 unidades com ReLU** e **uma unidade de saída com ativação linear**, com L1/L2, Adam e hinge loss (p. 3–5; anotações 4 e 8–10).

Há uma **ambiguidade entre a metodologia e a conclusão**: a conclusão afirma usar **SVM para a classificação final**, mas a metodologia descreve as camadas densas acima. Não há especificação de kernel, C, treinamento de SVM separado ou resultados isolados que confirmem essa implementação. Hinge loss, por si só, não comprova uso de um classificador SVM independente. Para a extração da revisão, registrar a implementação detalhada e acrescentar que “EfficientNet B0 + SVM” é alegado na conclusão, sem resolução da divergência (p. 6; anotação 14).

O foco declarado em hanseníase tuberculoide não corresponde a um experimento de classificação entre subtipos: a saída é binária, hanseníase versus não hanseníase. EfficientNet B0 tem maior F1 na Tabela I e menor número reportado de parâmetros treináveis na Tabela II, mas não a maior acurácia de validação.

## RQ7. Como a capacidade de generalização dos modelos é avaliada, especialmente quando são utilizados conjuntos de dados diferentes daqueles empregados no treinamento?

A evidência apresentada se restringe à divisão interna declarada do dataset e às métricas de treino/validação e da Tabela I. Não localizei teste cross-dataset, conjunto clínico externo independente, avaliação em outro centro/população ou estudo prospectivo. A composição das divisões e a ausência de informação sobre agrupamento por paciente limitam a avaliação de possível vazamento de dados; isso não permite afirmar que vazamento ocorreu.

O artigo declara que **validação externa em dataset independente é necessária** e propõe bases maiores e mais diversas como trabalho futuro (p. 6; anotações 15 e 16). Pré-treinamento no ImageNet, aumento de dados e early stopping são estratégias de desenvolvimento/regularização; não são demonstrações de desempenho externo.

Diferenças entre treino e validação, sobretudo 0,90 versus 0,70 para Xception, sugerem cautela quanto à generalização interna. Não provam por si só a causa dessas diferenças. Não há resultados que sustentem generalização entre tons de pele ou uso clínico em outras populações. Aplicações móveis também são propostas futuras, sem benchmark de implantação apresentado.

## RQ8. O artigo foi publicado em que tipo de veículo de publicação? (revista, conferência)

**Conferência.** Publicado na **2024 15th International Conference on Computing Communication and Networking Technologies (ICCCNT)**, IEEE. O rodapé informa **24–28 de junho de 2024**, IIT Mandi, Kamand, Índia. DOI: **10.1109/ICCCNT61001.2024.10725616** (p. 1; anotação 25). Não é artigo de revista.

## Cuidados para a síntese da revisão

*   Preservar a divergência entre total de imagens (1.476) e soma dos subconjuntos (1.600).
*   Separar precisão 0,9138 da acurácia de validação 0,90; o resumo troca o rótulo da primeira.
*   Registrar a divergência entre a cabeça densa descrita e o SVM alegado na conclusão.
*   Não transformar normalização/dimensão dadas como exemplos em configuração experimental confirmada.
*   Registrar diversidade de tons de pele e validação externa como não avaliadas, sem inferir resultados a partir de aumento de dados ou propostas futuras.

# Trechos e notas para o Zotero

Cada número corresponde a uma anotação no PDF. Os trechos textuais abaixo são literais, com quebras de linha/hifenização de fim de linha normalizadas. A última anotação é uma marcação de área da margem editorial vertical. Nas tabelas, os valores são transcritos na ordem das colunas; suas escalas são explicadas em cada nota. Os comentários podem ser copiados diretamente para o Zotero.

## 01. Tipo de estudo e foco

**Página 1 · Resumo**

**Trecho grifado:**

> This study explores the potential of deep learning techniques to improve leprosy diagnosis, specifically focusing on tuberculoid leprosy.

**Comentário:**

Tipo de estudo: pesquisa experimental computacional com comparação de modelos. RQ1/RQ6 — Foco declarado em hanseníase tuberculoide, mas tarefa implementada é binária (leprosy vs. non-leprosy), não discriminação entre subtipos de hanseníase. Não é revisão nem validação clínica prospectiva.

## 02. Fonte e tamanho do dataset

**Página 3 · V.A. Dataset**

**Trecho grifado:**

> The dataset is publicly available on the open-source Kaggle platform, comprised a total of 1476 images.

**Comentário:**

RQ2 — Dataset declarado público no Kaggle, com total de 1.476 imagens. Não localizei nome inequívoco, URL, versão, autor do dataset ou composição da classe negativa. Não são informados pacientes, lesões únicas, país de origem, idade, sexo, tons de pele ou processo de confirmação clínica/rotulagem. Contexto indiano e afiliações não estabelecem a população das imagens.

## 03. Divisão e inconsistência do total

**Página 3 · V.A. Dataset**

**Trecho grifado:**

> the dataset is divided into three distinct parts: train (1476 images), valid (62 images), and test (62 images).

**Comentário:**

RQ2/RQ3 — Treino 1.476, validação 62, teste 62: soma calculada 1.600, incompatível com o total de 1.476 declarado no mesmo parágrafo. Não corrigir silenciosamente nem assumir que a diferença é aumento de dados; isso não é explicado. Não há contagem por classe/subconjunto nem descrição de separação por paciente ou imagem original.

## 04. Pré-treinamento

**Página 3 · III.2. Transfer Learning and Model Adaptation**

**Trecho grifado:**

> The convolutional bases of VGG16, MobileNet v1, Xception v1, and EfficientNet B0 were initialized with weights pre-trained on the ImageNet dataset.

**Comentário:**

RQ1/RQ6 — Transfer learning com VGG16, MobileNet v1, Xception v1 e EfficientNet B0, com pesos ImageNet. Camadas superiores originais são removidas para adaptação. Não confundir MobileNet v1 com v2, apesar de haver referência bibliográfica sobre v2. ImageNet é pré-treinamento, não teste externo de hanseníase.

## 05. Dimensão de entrada declarada

**Página 3 · III.2**

**Trecho grifado:**

> All models were adapted to accept input images resized to 128x128 pixels with three color channels (RGB), a standard format for image classification tasks.

**Comentário:**

RQ1 — Dimensão declarada: 128 × 128 RGB, também na Figura 1. A seção V.D posteriormente dá 224 × 224 como exemplo, sem resolver a diferença. Preservar 128 × 128 como especificação explícita, registrando a inconsistência. Não localizei segmentação de ROI ou máscaras como etapa experimental.

## 06. Exemplos que deixam pré-processamento ambíguo

**Página 4 · V.D. Data Preprocessing**

**Trecho grifado:**

> Images were resized to a standard dimension (e.g., 224x224 pixels) to ensure compatibility with the EfficientNet B0 model and efficient processing.

**Comentário:**

RQ1/RQ3 — Aqui aparece e.g., 224×224, enquanto a seção III e a Figura 1 indicam 128×128. O parágrafo seguinte também dá normalização 0–1 ou −1 a 1 como exemplos, sem especificar a opção executada. A implementação não é integralmente reproduzível a partir desta descrição.

## 07. Aumento de dados no treino

**Página 3 · IV. Architecture Diagram**

**Trecho grifado:**

> various data augmentation techniques are applied to the training data. These include rescaling, zooming, rotation, and adjusting brightness

**Comentário:**

RQ1/RQ3/RQ7 — Aumento atribuído ao treino: reescala, zoom, rotação e brilho; seção V.B acrescenta saturação e intensidade aleatória de cor. Faixas, probabilidades e quantidade de imagens geradas não são detalhadas. Aumentar variação fotométrica não comprova diversidade de tons de pele ou validação externa.

## 08. Cabeça densa e saída linear

**Página 5 · V.F. Classification**

**Trecho grifado:**

> This model adds two fully-connected (dense) layers after the pre-trained EfficientNet B0 for classification.

**Comentário:**

RQ1/RQ6 — Metodologia detalha EfficientNet B0 com duas camadas densas: 128 unidades/ReLU e uma saída linear; regularização L1/L2 e hinge loss. A conclusão afirma uso de SVM, sem kernel, C ou descrição de treinamento de SVM separado. Preservar a inconsistência; hinge loss por si só não comprova classificador SVM independente.

## 09. Saída binária e calibração

**Página 5 · V.F. Classification**

**Trecho grifado:**

> This layer has a single unit with a linear activation function, suitable for binary classification (leprosy vs. non-leprosy)

**Comentário:**

RQ4/RQ6 — Saída linear única para hanseníase versus não hanseníase. Uma saída linear não é automaticamente probabilidade calibrada, apesar de o texto usar likelihood em outra seção. Limiar de decisão, codificação dos rótulos e calibração não estão suficientemente especificados.

## 10. Otimizador e perda

**Página 5 · V.G. Training**

**Trecho grifado:**

> The hinge loss function, suitable for binary classification and margin maximization, is employed.

**Comentário:**

RQ3/RQ6 — Hinge loss; mesma seção declara Adam e learning rate 0,01. Batch size, coeficientes de L1/L2, camadas congeladas/descongeladas e hiperparâmetros completos dos comparadores não são suficientemente detalhados. Há trechos que descrevem suas cabeças com likely/might, reduzindo a clareza do protocolo.

## 11. Máximo de épocas

**Página 5 · V.G. Training**

**Trecho grifado:**

> Due to limited computational resources, 20 epochs were chosen as the maximum training duration.

**Comentário:**

RQ3 — Máximo de 20 épocas. A descrição de early stopping adota 20 épocas sem melhora, o que não documenta parada antecipada antes desse teto em uma execução comum. Página 6 apresenta resultados de EfficientNet B0 após 15 épocas, mas não esclarece se esse foi o checkpoint selecionado ou a duração efetiva. Não inferir redução de épocas confirmada.

## 12. Early stopping

**Página 5 · V.G. Training**

**Trecho grifado:**

> During training, if the validation accuracy doesn’t improve for a certain number of epochs (20 in this case), the training is stopped early.

**Comentário:**

RQ3 — Monitoramento da validation accuracy, paciência declarada de 20 épocas e restauração do melhor modelo. Como o teto também é 20, falta esclarecer a operação efetiva da parada. Não localizei validação cruzada, repetições, sementes, intervalos de confiança ou testes de significância.

## 13. Accuracy confundida com precision

**Página 1 · Resumo**

**Trecho grifado:**

> With a recall of 0.9298, an F1 score of 0.9217, and an accuracy of 0.9138, EfficientNetB0 performed the best.

**Comentário:**

RQ3/RQ4 — O resumo chama 0,9138 de accuracy, mas Tabela I, análise e conclusão identificam esse valor como precision. A Tabela II informa accuracy de treino 0,95 e validação 0,90 para EfficientNet B0. Não registrar 91,38% como acurácia de teste comprovada; preservar a divergência de rótulo da métrica.

## 14. SVM alegado na conclusão

**Página 6 · VII. Conclusion**

**Trecho grifado:**

> By utilizing a pre-trained EfficientNetB0 model for feature extraction and employing support vector machines (SVMs) for final classification, we aim to enhance the accuracy and robustness of leprosy detection.

**Comentário:**

RQ6 — Conclusão menciona EfficientNetB0 + SVM, mas a metodologia detalha camadas densas/ReLU/linear treinadas com hinge loss e Adam. Não há resultado isolado de SVM nem comparação tabulada de classificadores tradicionais. Registrar como ambiguidade, não como implementação de SVM confirmada.

## 15. Validação externa ainda necessária

**Página 6 · VII. Conclusion**

**Trecho grifado:**

> External validation on an independent dataset is crucial to ensure the model’s generalizability in real-world scenarios.

**Comentário:**

RQ7 — Os próprios autores apontam validação externa como necessária. Não localizei experimento cross-dataset, teste em centro/população independente ou avaliação prospectiva. Teste interno declarado e aumento de dados não equivalem a validação externa.

## 16. Explicabilidade e aplicativo como futuro

**Página 6 · VII. Conclusion**

**Trecho grifado:**

> Future work will focus on further validating this model on larger and more diverse datasets, exploring the integration of explainable AI techniques to enhance interpretability, and investigating the potential for real-world deployment through mobile health applications.

**Comentário:**

RQ1/RQ5/RQ7 — Bases maiores/diversas, XAI e aplicação móvel aparecem como trabalho futuro. Não atribuir Grad-CAM/LIME dos trabalhos relacionados à implementação deste estudo. Não são apresentados resultados por tom de pele nem benchmark móvel de latência, energia ou memória.

## 17. VGG16 — precision, recall e F1

**Página 5 · Tabela I**

**Trecho grifado:**

> VGG16 0.7714 0.9474 0.8504

**Comentário:**

RQ3/RQ4/RQ6 — VGG16: precision 0.7714, recall 0.9474 e F1 0.8504 (escala 0–1), conforme Tabela I. O trecho dos resultados não explicita inequivocamente o split usado para esta tabela; não misturar com accuracy de treino/validação da Tabela II. Maior recall (94,74%) entre os quatro, porém menor precision (77,14%).

## 18. MobileNet V1 — precision, recall e F1

**Página 5 · Tabela I**

**Trecho grifado:**

> MobileNet V1 0.9592 0.8246 0.8868

**Comentário:**

RQ3/RQ4/RQ6 — MobileNet V1: precision 0.9592, recall 0.8246 e F1 0.8868 (escala 0–1), conforme Tabela I. O trecho dos resultados não explicita inequivocamente o split usado para esta tabela; não misturar com accuracy de treino/validação da Tabela II. Maior precision (95,92%), mas menor recall (82,46%).

## 19. Xception — precision, recall e F1

**Página 5 · Tabela I**

**Trecho grifado:**

> Xception 0.8947 0.8947 0.8947

**Comentário:**

RQ3/RQ4/RQ6 — Xception: precision 0.8947, recall 0.8947 e F1 0.8947 (escala 0–1), conforme Tabela I. O trecho dos resultados não explicita inequivocamente o split usado para esta tabela; não misturar com accuracy de treino/validação da Tabela II.

## 20. EfficientNet B0 — precision, recall e F1

**Página 5 · Tabela I**

**Trecho grifado:**

> EfficientNet B0 0.9138 0.9298 0.9217

**Comentário:**

RQ3/RQ4/RQ6 — EfficientNet B0: precision 0.9138, recall 0.9298 e F1 0.9217 (escala 0–1), conforme Tabela I. O trecho dos resultados não explicita inequivocamente o split usado para esta tabela; não misturar com accuracy de treino/validação da Tabela II. Maior F1 (92,17%), não maior precision nem recall isoladamente. 0,9138 é precision nesta tabela; o resumo o rotula como accuracy.

## 21. VGG 16 — accuracy e parâmetros treináveis

**Página 6 · Tabela II**

**Trecho grifado:**

> VGG 16 0.98 0.95 50343937

**Comentário:**

RQ3/RQ4/RQ6 — VGG 16: accuracy de treino 0.98, validação 0.95; 50,343,937 parâmetros treináveis, conforme Tabela II. Estes não são resultados identificados como teste. Parâmetros treináveis não representam necessariamente todos os parâmetros da rede, tamanho do arquivo, FLOPs ou latência. Maior validation accuracy da tabela (95%), superior aos 90% de EfficientNet B0; a escolha deste último é sustentada pelo F1/eficiência alegada, não por vencer toda métrica.

## 22. MobileNet — accuracy e parâmetros treináveis

**Página 6 · Tabela II**

**Trecho grifado:**

> MobileNet 0.95 0.85 1050625

**Comentário:**

RQ3/RQ4/RQ6 — MobileNet: accuracy de treino 0.95, validação 0.85; 1,050,625 parâmetros treináveis, conforme Tabela II. Estes não são resultados identificados como teste. Parâmetros treináveis não representam necessariamente todos os parâmetros da rede, tamanho do arquivo, FLOPs ou latência.

## 23. Xception — accuracy e parâmetros treináveis

**Página 6 · Tabela II**

**Trecho grifado:**

> Xception 0.9 0.7 2099201

**Comentário:**

RQ3/RQ4/RQ6 — Xception: accuracy de treino 0.9, validação 0.7; 2,099,201 parâmetros treináveis, conforme Tabela II. Estes não são resultados identificados como teste. Parâmetros treináveis não representam necessariamente todos os parâmetros da rede, tamanho do arquivo, FLOPs ou latência.

## 24. EfficientNet B0 — accuracy e parâmetros treináveis

**Página 6 · Tabela II**

**Trecho grifado:**

> EfficientNet B0 0.95 0.9 164097

**Comentário:**

RQ3/RQ4/RQ6 — EfficientNet B0: accuracy de treino 0.95, validação 0.9; 164,097 parâmetros treináveis, conforme Tabela II. Estes não são resultados identificados como teste. Parâmetros treináveis não representam necessariamente todos os parâmetros da rede, tamanho do arquivo, FLOPs ou latência.

## 25. Veículo de publicação

**Página 1 · Margem editorial vertical**

**Rótulos da área marcada:**

> 2024 15th International Conference on Computing Communication and Networking Technologies (ICCCNT) DOI: 10.1109/ICCCNT61001.2024.10725616

**Comentário:**

RQ8 — Artigo de conferência: 2024 15th International Conference on Computing Communication and Networking Technologies (ICCCNT), IEEE. O rodapé informa 24–28 de junho de 2024, IIT Mandi, Kamand, Índia. DOI 10.1109/ICCCNT61001.2024.10725616. Não é artigo de revista.
