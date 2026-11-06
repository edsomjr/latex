---
tags: []
parent: 'A trustworthy and explainable deep learning framework for skin lesion detection in smart dermatology'
collections:
    - TCC_Leituras
$version: 192
$libraryID: 2
$itemKey: DXR3GZSZ

---
# RQs, trechos grifados e notas

**Artigo:** Mohammad A. Eita; Hamada Rizk. *A trustworthy and explainable deep learning framework for skin lesion detection in smart dermatology*. Engineering Applications of Artificial Intelligence, 159, 111594, 2025. DOI: 10.1016/j.engappai.2025.111594.

**Fonte da análise:** PDF fornecido, 18 páginas. A numeração abaixo corresponde às páginas do PDF, coincidentes com a paginação impressa. Esta extração se limita ao artigo; não inclui auditoria do código, dos datasets ou de fontes externas.

**Sobre as perguntas:** os enunciados das RQs foram fornecidos pelo usuário e estão reproduzidos abaixo. As respostas distinguem informações relatadas, interpretação crítica e dados não localizados. RQ4 corresponde a métricas/resultados; RQ6, a modelos/abordagens de IA.

**Tipo de estudo:** pesquisa experimental computacional; desenvolvimento e avaliação de detecção/localização e classificação multiclasse de lesões. Hanseníase é uma das seis classes. Não é revisão, nem estudo exclusivamente dedicado à hanseníase, nem validação clínica prospectiva concluída.

## RQ1 — Quais técnicas de visão computacional são utilizadas para identificar manifestações dermatológicas associadas à hanseníase?

**Resposta:** framework baseado em YOLOv8, especificado como **YOLOv8n** na avaliação. Localiza lesões por bounding boxes e atribui classes; não apresenta segmentação por máscara como resultado principal. O texto descreve extração profunda de características em múltiplas escalas, backbone denominado CSPDarknet53 e agregação por PANet (seção 5.2). Esses nomes são descrições dos autores, sem verificação independente da implementação.

*   **Pré-processamento:** redimensionamento preservando proporção, padding e entrada 640 × 640; normalização das intensidades para \[0,1]; remoção de pelos por limiarização e operações morfológicas. Padronização por média/desvio-padrão é apresentada como possibilidade adicional, não como execução confirmada.
*   **Aumento:** espelhamentos horizontal/vertical; recortes aleatórios; contraste; rotações aleatórias de −15° a +15° e rotações de 90°/180°; brilho com faixas de ±0,15 e ±0,25; exposição com fator 1 + alfa, alfa em ±0,15; ruído gaussiano, com aplicação parcial descrita em até 0,1% dos pixels. O artigo afirma que o aumento triplicou o dataset.
*   **Treinamento:** AdamW, learning rate 0,001, momentum 0,9 e weight decay 0,0005; lote 16; focal loss com alfa 0,25 e gama 2,0 para exemplos difíceis/desequilíbrio.
*   **Pós-processamento:** Non-Maximum Suppression (NMS).
*   **Explicabilidade:** mapas de saliência por gradientes em relação à entrada, combinando classificação e localização. Não identificar automaticamente como Grad-CAM. A inspeção visual das explicações não demonstra validade clínica.

**Evidência:** páginas 4–9, seções 5.1–5.3; anotações 04–11. **Limites:** detalhes de implementação incompletos; não tratar saliência como segmentação supervisionada nem ajuste fotométrico como diversidade populacional real.

## RQ2 — Quais conjuntos de dados e populações são utilizados no desenvolvimento e na avaliação desses modelos?

**Resposta:** o principal é o **Fredrick Skin Disease Dataset**, público, disponibilizado no Roboflow. O artigo declara **1.101 imagens**, seis classes e as contagens abaixo de **anotações**.

| Classe                                | Anotações declaradas |
| ------------------------------------- | -------------------- |
| Acne                                  | 1.208                |
| Wart (verruga)                        | 807                  |
| Leprosy (hanseníase)                  | 643                  |
| Psoriasis (psoríase)                  | 261                  |
| Keratosis Pilaris (queratose pilar)   | 137                  |
| Atopic Dermatitis (dermatite atópica) | 74                   |
| **Total calculado**                   | **3.130**            |


As **643 anotações de hanseníase** representam aproximadamente 20,5% das anotações. Não são 643 pacientes, imagens ou lesões únicas comprovadamente distintas. O número de pacientes, a contagem de imagens por classe, o país de recrutamento, a composição demográfica e os tons de pele não são suficientemente informados. A seção 6.2.2 usa essas mesmas contagens como “training instances”, sem reconciliá-las claramente com a divisão dos dados.

O aumento é descrito como triplicação: **3.303 imagens seria uma inferência aritmética** a partir de 1.101, não uma contagem final expressamente apresentada. Variantes aumentadas não são observações clínicas independentes.

O segundo conjunto é denominado pelos autores **“HAM10000 Skin Diseases Detection dataset”**, também do Roboflow Universe. Não localizei tamanho efetivamente usado, distribuição de classes, número de pacientes ou correspondência dos rótulos com as seis classes do Fredrick. Não assumir que o conjunto corresponde integralmente ao HAM10000 original, nem que inclui hanseníase, apenas pelo nome.

**Endereços transcritos do artigo, não auditados nesta análise:**

*   Principal: https\://universe.roboflow\.com/fredrick-gk-wpenz/skin-disease-hwlrn
*   Segundo dataset, referência Universe (2024): https\://universe.roboflow\.com/universitas-dian-nuswantoro-u3s2y/skin\_diases\_detection

**Evidência:** página 4, seção 4; página 7; página 12, seções 6.2.2–6.2.3; disponibilidade dos dados na página 16 e referência na página 18; anotações 02–03, 08, 16–17.

## RQ3 — Quais métodos, procedimentos são utilizados para avaliar o desempenho desses modelos e quais resultados são reportados?

**Resposta:** divisão **holdout de 85%/10%/5%** para treinamento/validação/teste, descrita sobre o **dataset aumentado**. A validação é usada para ajuste de hiperparâmetros e monitoramento; o teste é declarado exclusivo para avaliação. Há curvas de perdas, curvas precisão–recall e métricas em função do limiar de confiança, ablação de aumento, comparação entre modelos e avaliação em um segundo dataset.

A redação não esclarece se a divisão ocorreu antes da geração das variantes, se versões da mesma imagem ficaram no mesmo subconjunto ou se houve separação por paciente. Assim, existe **risco de vazamento**, caso imagens relacionadas estejam em conjuntos diferentes, mas **não há evidência suficiente para afirmar que ocorreu**. Também não localizei protocolo de validação cruzada, repetições independentes, sementes, intervalos de confiança, desvios-padrão de desempenho ou testes de significância. A indicação de convergência em torno de 50 épocas não confirma o número total de épocas.

A avaliação denominada cross-dataset não esclarece suficientemente congelamento do modelo, eventual retreinamento/fine-tuning, seleção de amostras nem mapeamento das classes. Estudos prospectivos com dermatologistas permanecem trabalho futuro.

**Resultados reportados:** no Fredrick, precision 90,4%, recall 85,6%, F1 87,9% e mAP50 91,2%; no segundo dataset, 74,1%, 78,2%, 76,0% e 82,4%, respectivamente, com mAP50–95 54,0%. Para hanseníase, a Figura 10 informa F1 81% e mAP50 84%, mas a Figura 6(b) traz AP\@0,5 91,4%; o protocolo não explica suficientemente a divergência. As tabelas das RQs 4 e 6 detalham os resultados.

**Evidência:** páginas 8–9, 11–12 e 16; anotações 10, 12, 14, 17, 21 e 25.

## RQ4 — Quais métricas são utilizadas para avaliar o desempenho desses modelos e quais resultados são reportados?

**Resposta:** precision, recall, F1-score e mAP\@50; para o segundo dataset também **mAP\@50–95**. Há curvas F1–confiança, precisão–recall, precisão–confiança e recall–confiança, além de perdas de treinamento/validação. São relatados tempos de treinamento e inferência.

| Avaliação do modelo proposto   | Precision (%) | Recall (%) | F1 (%) | mAP@50 (%) | mAP@50–95 (%)  |
| ------------------------------ | ------------- | ---------- | ------ | ---------- | -------------- |
| Fredrick — resultado principal | 90,4          | 85,6       | 87,9   | 91,2       | Não localizado |
| Segundo dataset — seção 6.2.3  | 74,1          | 78,2       | 76,0   | 82,4       | 54,0           |


**Hanseníase:** Figura 10: F1 81% e mAP50 84%; Figura 6(b): AP\@0,5 91,4%. O artigo não esclarece a divergência. Para os valores globais também há diferença: a Figura 6 apresenta mAP\@0,5 85,8% e pico de F1 83%, enquanto o resultado principal é 91,2% e 87,9%. Não confundir métricas globais com desempenho da classe hanseníase.

**Eficiência:** 0,35 h de treinamento e 2,5 ms/imagem para o proposto; treinamento em duas NVIDIA Tesla T4. Não são medidas demonstradas de um fluxo clínico completo em smartphone.

**Cuidados:** mAP\@50 é métrica de detecção com limiar de IoU de 0,5, não accuracy. AP por classe também não é accuracy. Os escores de confiança de caixas individuais não são sensibilidade, especificidade ou acurácia do estudo. Apesar de a seção 6 mencionar “accuracy”, não localizei um valor separado claramente identificado de acurácia global nem acurácia específica de hanseníase. Tampouco localizei AUC ROC ou especificidade como resultados do modelo proposto. Preservar divergências descritas na RQ6.

**Evidência:** páginas 9–15; anotações 13–15, 18, 20, 22 e 27–28.

## RQ5 — Como o desempenho dos modelos varia entre diferentes grupos ou tons de pele?

**Resposta:** **não localizei avaliação quantitativa estratificada por tom de pele**. Não são fornecidos grupos Fitzpatrick/Monk, distribuição de participantes por tom, métricas por grupo nem comparação estatística entre tons.

O artigo alega que transformações geométricas/fotométricas ampliam generalização, mas reconhece que os datasets não cobrem todo o espectro de tons e propõe incluir mais dados de pessoas com pele escura como trabalho futuro. Ajustar brilho/contraste não demonstra que novos grupos populacionais foram representados; a queda de desempenho entre datasets não isola o efeito do tom de pele.

**Classificação para extração:** diversidade/viés discutidos qualitativamente; desempenho por tom de pele **não informado**. Não inferir características populacionais a partir de afiliações dos autores ou imagens ilustrativas.

**Evidência:** páginas 6, 12 e 16; anotações 07, 23–24.

## RQ6 — Quais modelos e abordagens de inteligência artificial são utilizados para identificar manifestações dermatológicas associadas à hanseníase?

**Resposta:** modelo proposto **YOLOv8n** comparado com YOLOv9t, YOLOv10n, ViT, Faster R-CNN e RetinaNet. A tabela abaixo transcreve os resultados gerais relatados no texto da comparação (páginas 13–15), sem corrigir divergências.

| Modelo             | Precision (%) | Recall (%) | F1 (%) | mAP50 (%) |
| ------------------ | ------------- | ---------- | ------ | --------- |
| YOLOv8n proposto   | 90,4          | 85,6       | 87,9   | 91,2      |
| YOLOv9t            | 91,7          | 80,5       | 85,2   | 89,7      |
| YOLOv10n           | 82,2          | 84,8       | 78,9   | 87,5      |
| Vision Transformer | 86,2          | 85,1       | 85,6   | 88,5      |
| Faster R-CNN       | 59,6          | 71,0       | 64,8   | 55,0      |
| RetinaNet          | 56,0          | 72,9       | 63,6   | 58,0      |


**Resultado específico de hanseníase:** a **Figura 10, página 14**, apresenta **F1 de 81% e mAP50 de 84%**. Na **Figura 6(b), página 12**, a legenda informa **AP\@0,5 de 0,914 (91,4%) para Leprosy**. Não foi localizada explicação suficiente para conciliar essas apresentações. O AP da classe não é accuracy e o resultado geral de 91,2% não é desempenho exclusivo de hanseníase.

**Divergências relevantes:**

1.  Resultado global principal: F1 87,9% (87,93% na seção 6.1.2) e mAP50 91,2%; Figura 6: pico de F1 0,83 a confiança 0,542 e mAP\@0,5 global 0,858.
2.  Hanseníase: AP\@0,5 de 91,4% na Figura 6(b), mas mAP50 de 84% na Figura 10. Não juntar os dois como se fossem um resultado único.
3.  YOLOv10n: F1 relatado de 78,9% não corresponde à média harmônica direta de precision 82,2% e recall 84,8%, aproximadamente 83,48%. Diferenças de agregação ou erro de relato são possibilidades não esclarecidas.
4.  As legendas das Figuras 9 e 10 repetem uma descrição de aumento de dados, embora o conteúdo mostre comparação entre datasets e entre classes, respectivamente. A identificação dos valores nesta análise considera o conteúdo visual e as seções correspondentes.

**Ablação:** F1 sem aumento 79,7; brilho 88,0; espelhamento 82,7; ruído 85,8; rotação 80,2 (seção 6.2.1). Sem inferência de significância estatística.

**Evidência:** páginas 11–15; anotações 13–16, 18–22, 27–28. O ranking é restrito às condições relatadas; falta detalhamento para uma auditoria de equivalência de ajuste dos modelos.

## RQ7 — Como a capacidade de generalização dos modelos é avaliada, especialmente quando são utilizados conjuntos de dados diferentes daqueles empregados no treinamento?

**Resposta:** **sim, há uma avaliação em segundo dataset relatada pelos autores como cross-dataset**. O Fredrick é o benchmark principal e o conjunto denominado HAM10000 Skin Diseases Detection é o segundo. Usando os resultados principais do texto, as quedas são:

| Métrica   | Fredrick | Segundo dataset | Queda calculada         |
| --------- | -------- | --------------- | ----------------------- |
| Precision | 90,4%    | 74,1%           | 16,3 pontos percentuais |
| Recall    | 85,6%    | 78,2%           | 7,4 pontos percentuais  |
| F1        | 87,9%    | 76,0%           | 11,9 pontos percentuais |
| mAP@50    | 91,2%    | 82,4%           | 8,8 pontos percentuais  |


**Qualificação da evidência:** registrar “avaliação em segundo dataset relatada; protocolo externo parcialmente descrito”. Não afirmar transferência sem ajuste comprovada: o texto não detalha suficientemente retreinamento, rótulos compatíveis, independência das amostras e tamanho do teste. **Não localizei validação externa específica de hanseníase.** A presença dessa classe no segundo conjunto não é estabelecida pelo artigo.

As limitações incluem diversidade incompleta de tons/modalidades/doenças raras, mudança de domínio, possível risco de vazamento na divisão do dataset aumentado e ausência de validação clínica prospectiva concluída. A hipótese de generalização clínica não está demonstrada somente por desempenho em imagens públicas.

**Evidência:** página 12, seção 6.2.3; Figura 9, página 14; seção 6.4, página 16; anotações 12, 17–18, 23 e 25.

## RQ8 — O artigo foi publicado em que tipo de veículo de publicação? (revista, conferência)

**Resposta:** artigo original de pesquisa em **periódico**, *Engineering Applications of Artificial Intelligence*, volume **159**, identificador **111594**, ano **2025**, Elsevier. DOI **10.1016/j.engappai.2025.111594**. O PDF indica “Research paper”, aceitação em 19 de junho de 2025 e disponibilidade on-line em 5 de julho de 2025. **Não é conferência; não é revisão de literatura.**

**Evidência:** página 1, cabeçalho e metadados editoriais; anotação 26.

# Trechos e notas para o Zotero

Cada número corresponde a uma anotação no PDF. Os trechos textuais abaixo são literais, com quebras de linha/hifenização de fim de linha normalizadas. As duas últimas entradas são marcações de área em figuras, com transcrição dos rótulos visíveis. Os comentários podem ser copiados diretamente para o Zotero.

## 01. Tipo de estudo e tarefa

**Página 4 · 5. Methodology**

**Trecho grifado:**

> The methodology employed in this research leverages the YOLOv8 model for detecting and classifying a variety of skin lesions, including Acne, Atopic Dermatitis, Keratosis Pilaris, Leprosy, Psoriasis, and Wart.

**Comentário:**

Tipo de estudo: pesquisa experimental computacional com desenvolvimento e avaliação de um detector multiclasse. RQ1/RQ6 — YOLOv8 para localizar e classificar lesões de seis condições, incluindo hanseníase. Não é revisão nem classificador binário exclusivo de hanseníase; os resultados globais não devem ser atribuídos automaticamente a essa doença.

## 02. Dataset principal e unidade de contagem

**Página 4 · 4. Dataset**

**Trecho grifado:**

> The dataset comprises a total of 1101 images across six distinct classes: Acne, Wart, Leprosy, Psoriasis, Keratosis Pilaris, and Atopic Dermatitis.

**Comentário:**

RQ2 — Fredrick Skin Disease Dataset, público, disponibilizado no Roboflow: 1.101 imagens e seis classes. O artigo não informa número de pacientes nem número de imagens específico de hanseníase. Não confundir imagens com anotações de objetos ou pacientes.

## 03. Quantidade de anotações de hanseníase

**Página 4 · 4. Dataset**

**Trecho grifado:**

> Leprosy includes 643 annotations, representing around 20.5% of the dataset.

**Comentário:**

RQ2 — Hanseníase: 643 anotações, cerca de 20,5% das anotações. As seis contagens somam 3.130 anotações: acne 1.208, verruga 807, hanseníase 643, psoríase 261, queratose pilar 137 e dermatite atópica 74. Não registrar 643 como pacientes ou como imagens independentes. A seção 6.2.2 posteriormente chama essas contagens de instâncias de treinamento, sem esclarecer a reconciliação com a divisão do dataset.

## 04. Preservação da proporção das imagens

**Página 4 · 5.1.1**

**Trecho grifado:**

> The rescaling process involves adjusting the spatial dimensions of the image while maintaining its aspect ratio to prevent distortion. This is achieved by padding the resized image with a border of a constant value (typically zero, corresponding to black) to fit the target dimensions

**Comentário:**

RQ1 — Redimensionamento com preservação da proporção e preenchimento das bordas (padding). A entrada final é declarada como 640 × 640 pixels na página 9. Não se trata de segmentação de lesões por máscara.

## 05. Normalização

**Página 4 · 5.1.1**

**Trecho grifado:**

> Following rescaling, pixel values of the image are normalized to the range \[0, 1].

**Comentário:**

RQ1 — Normalização das intensidades para \[0,1], com divisão por 255 descrita na página 5. A padronização por média e desvio-padrão é apresentada como etapa que poderia ser incorporada, não como procedimento comprovadamente executado.

## 06. Remoção de pelos

**Página 5 · 5.1.1**

**Trecho grifado:**

> To address this, a hair removal technique is applied using morphological operations

**Comentário:**

RQ1 — Os autores declaram remoção de pelos com operações morfológicas; o parágrafo menciona limiarização, dilatação e erosão. Parâmetros e detalhes de implementação são insuficientes para reproduzir integralmente essa etapa.

## 07. Aumento de dados e diversidade alegada

**Página 6 · 5.1.2**

**Trecho grifado:**

> We employed a combination of geometric and photometric transformations to enhance the model’s generalizability across diverse skin tones and lighting conditions. Specifically, augmentations such as rotation, random cropping, contrast adjustments, and Gaussian noise were applied to simulate real-world variations in medical imaging.

**Comentário:**

RQ1/RQ5/RQ7 — Aumento de dados geométrico e fotométrico: rotação, recorte aleatório, contraste e ruído gaussiano; a seção também descreve espelhamentos, brilho e exposição. A intenção de ampliar generalização entre tons de pele não equivale a uma avaliação estratificada por tom nem demonstra equidade.

## 08. Expansão do dataset

**Página 7 · 5.1.2**

**Trecho grifado:**

> These augmentations effectively tripled the size of the original dataset, thereby reducing the risk of overfitting and improving the model’s ability to generalize to unseen data.

**Comentário:**

RQ1/RQ2/RQ3 — Os autores afirmam que o aumento triplicou o dataset. Isso corresponderia a 3.303 imagens derivadas se aplicado às 1.101 originais; 3.303 é cálculo, não contagem explicitada no artigo. Não são novos pacientes ou observações independentes. A página 9 descreve a divisão do dataset aumentado, sem esclarecer o agrupamento de variantes da mesma imagem.

## 09. Focal loss

**Página 8 · 5.2**

**Trecho grifado:**

> To address this, the model integrates a focal loss component into the classification loss.

**Comentário:**

RQ1/RQ6 — Focal loss incorporada à perda de classificação para lidar com desequilíbrio e exemplos difíceis. Parâmetros declarados: alfa 0,25 e gama 2,0. A presença dessa técnica não comprova, por si só, ausência de viés ou eficácia em populações sub-representadas.

## 10. Configuração de treinamento

**Página 9 · 5.2**

**Trecho grifado:**

> The model was trained with a batch size of 16 and an image input size of 640 × 640 pixels.

**Comentário:**

RQ1/RQ3 — Lote 16 e entrada 640 × 640. A página 8 declara AdamW, learning rate 0,001, momentum 0,9 e weight decay 0,0005. A página 11 menciona convergência em torno de 50 épocas, sem que isso deva ser tomado automaticamente como número total de épocas. Não localizei sementes, repetições ou validação cruzada.

## 11. Explicabilidade

**Página 9 · 5.3**

**Trecho grifado:**

> Saliency maps are derived by calculating the gradient of the model’s output with respect to the input image.

**Comentário:**

RQ1/RQ6 — Mapas de saliência baseados em gradientes da saída em relação à imagem; o texto descreve combinação de informações de classificação e localização. Não registrar automaticamente como Grad-CAM: a técnica usada é descrita aqui por gradientes de entrada. As visualizações não equivalem a validação clínica das explicações.

## 12. Divisão dos dados e possível vazamento

**Página 9 · 6. Results and evaluation**

**Trecho grifado:**

> The training set is 85% of the augmented dataset, used to optimize the model’s weights and learn the underlying patterns of the skin lesions. A validation set, accounting for 10%, was utilized to tune hyperparameters and monitor the model’s performance during training, ensuring that the model did not overfit. Finally, the remaining 5% was reserved as the test set, used exclusively to evaluate the model’s generalization performance on unseen data.

**Comentário:**

RQ3 — Holdout declarado: 85% treinamento, 10% validação e 5% teste, referido ao dataset aumentado. Não localizei explicação de separação por paciente/imagem original nem de confinamento das variantes aumentadas a um único subconjunto. Há risco metodológico de vazamento se variantes da mesma imagem estiverem em conjuntos diferentes; o texto não permite afirmar que isso efetivamente ocorreu.

## 13. Resultados globais no dataset principal

**Página 12 · 6.2.3**

**Trecho grifado:**

> On this dataset, the proposed model achieved a precision of 90.4%, recall of 85.6%, F1-score of 87.9%, and mAP\@50 of 91.2%, indicating strong performance in both detecting and classifying skin lesions with accurate localization.

**Comentário:**

RQ4/RQ6 — Resultados globais no Fredrick: precision 90,4%; recall 85,6%; F1 87,9%; mAP\@50 91,2%. A seção 6.1.2 apresenta F1 87,93%. São métricas gerais de detecção, não resultados exclusivos de hanseníase nem accuracy de 91,2%. Há divergência com a Figura 6, que mostra mAP\@0.5 global 0,858.

## 14. Divergência de F1 entre apresentações

**Página 11 · 6.1.3**

**Trecho grifado:**

> The F1-confidence curve (Fig. 6(a)) reveals the model’s ability to achieve a balanced trade-off between precision and recall, with a peak F1 score of 0.83 at a confidence threshold of 0.54 for all classes combined.

**Comentário:**

RQ3/RQ4/RQ6 — A curva F1/confiança informa pico global de 0,83, enquanto o resultado principal é F1 87,9%/87,93%. A Figura 6(a) traz limiar 0,542; o texto arredonda para 0,54. Não localizei explicação suficiente sobre diferença de execução, subconjunto ou agregação para conciliar os resultados.

## 15. Divergência de mAP

**Página 11 · 6.1.3**

**Trecho grifado:**

> The overall mAP\@0.5 value of 0.858 confirms that the model performs well overall.

**Comentário:**

RQ4/RQ6 — mAP\@0.5 global de 0,858 (85,8%) nas curvas da Figura 6, diferente de 91,2% no resultado principal. Preservar ambos com suas fontes; não selecionar o maior valor sem registrar a divergência.

## 16. Interpretação específica de hanseníase

**Página 12 · 6.2.2**

**Trecho grifado:**

> Similarly, Leprosy, with 643 instances, also demonstrates moderate performance, potentially due to its overlapping visual characteristics with other classes and high inter-patient variation.

**Comentário:**

RQ2/RQ4 — O texto reconhece desempenho moderado para hanseníase. A Figura 10 mostra F1 81% e mAP50 84%; já a Figura 6(b) exibe AP de 0,914 para Leprosy. A causa dessa diferença não fica esclarecida. As 643 instâncias correspondem à contagem descrita como anotações na seção 4, não a 643 pacientes.

## 17. Segundo dataset e protocolo externo

**Página 12 · 6.2.3**

**Trecho grifado:**

> To validate the framework’s ability to generalize beyond this controlled setup, we further evaluated it on the HAM10000 Skin Diseases Detection dataset from Roboflow Universe.

**Comentário:**

RQ2/RQ3/RQ7 — Os autores relatam avaliação em segundo dataset, denominado no artigo HAM10000 Skin Diseases Detection, do Roboflow Universe. Não ficam claros tamanho usado, classes, mapeamento entre rótulos, sobreposição com o primeiro dataset ou eventual retreinamento/fine-tuning. Não assumir equivalência ao HAM10000 original nem comprovação de validação externa específica de hanseníase.

## 18. Resultados no segundo dataset

**Página 12 · 6.2.3**

**Trecho grifado:**

> When tested on this dataset, the proposed model attained a precision of 74.1%, recall of 78.2%, F1-score of 76.0%, mAP\@50 of 82.4%, and mAP\@50–95 of 54.0%.

**Comentário:**

RQ4/RQ6/RQ7 — Segundo dataset: precision 74,1%; recall 78,2%; F1 76,0%; mAP\@50 82,4%; mAP\@50–95 54,0%. Em relação aos valores principais do Fredrick, quedas de 16,3, 7,4, 11,9 e 8,8 pontos percentuais, respectivamente. Resultados gerais; não há resultado externo específico de hanseníase identificado. A queda não pode ser atribuída isoladamente ao tom de pele.

## 19. Modelos comparados

**Página 13 · 6.3.1**

**Trecho grifado:**

> Fig. 11 presents a comprehensive evaluation of the proposed YOLOv8n-based skin lesion detection framework against five alternative models: YOLOv9t, YOLOv10n, Vision Transformer (ViT), Faster R-CNN, and RetinaNet.

**Comentário:**

RQ6 — Modelo proposto YOLOv8n; comparadores: YOLOv9t, YOLOv10n, ViT, Faster R-CNN e RetinaNet. Não localizei detalhamento completo e uniforme dos hiperparâmetros, inicialização e ajuste de cada baseline. Interpretar a comparação no contexto experimental relatado, sem generalizar superioridade universal.

## 20. Inconsistência no F1 do YOLOv10n

**Página 14 · 6.3.1**

**Trecho grifado:**

> This trade-off leads to a lower F1-Score of 78.9% and mAP50 of 87.5%, reflecting a model that is faster but less reliable for nuanced lesion detection tasks.

**Comentário:**

RQ4/RQ6 — Para YOLOv10n, o texto informa precision 82,2%, recall 84,8% e F1 78,9%. A média harmônica direta desses P/R é aproximadamente 83,48%, não 78,9%. Pode haver diferença de agregação ou erro de relato, mas o artigo não a esclarece. Preservar o valor publicado com ressalva; não corrigir silenciosamente.

## 21. Ablação do aumento de dados

**Página 11 · 6.2.1**

**Trecho grifado:**

> Notably, the F1-Score peaked at 88.0 when brightness adjustment was applied.

**Comentário:**

RQ1/RQ3/RQ4 — Na ablação: F1 sem aumento 79,7; com brilho 88,0; espelhamento 82,7; ruído 85,8; rotação 80,2. Comparação do experimento relatado, sem intervalos de confiança ou testes estatísticos identificados. Melhoria com brilho não demonstra por si só melhoria entre tons de pele.

## 22. Eficiência computacional

**Página 15 · 6.3.2**

**Trecho grifado:**

> the proposed model demonstrates the most advantageous runtime profile among all evaluated methods, completing training in only 0.35 h and achieving ultra-fast inference with a latency of 2.5 ms per image.

**Comentário:**

RQ4/RQ6 — Tempo reportado: treinamento 0,35 h (21 minutos) e inferência 2,5 ms/imagem. A seção 6.4 informa treinamento em duas NVIDIA Tesla T4. Não extrapolar esses tempos para celular ou atendimento clínico completo; ensaios nesses dispositivos não foram identificados.

## 23. Limitação de tons de pele

**Página 16 · 6.4**

**Trecho grifado:**

> The current datasets do not cover the full spectrum of skin tones, imaging modalities, and rare dermatological conditions encountered globally.

**Comentário:**

RQ5/RQ7 — Limitação explícita de cobertura de tons de pele. Não localizei classificação Fitzpatrick/Monk, contagens por tom, métricas estratificadas ou comparação quantitativa entre tons. Registrar diversidade insuficiente reconhecida pelos autores; não inferir tons pelas figuras, nacionalidades ou ajustes de brilho.

## 24. Peles escuras como trabalho futuro

**Página 16 · 7. Conclusions**

**Trecho grifado:**

> One key area is the inclusion of additional data from underrepresented populations, such as individuals with darker skin tones, which would help mitigate any potential biases.

**Comentário:**

RQ5 — Inclusão de pessoas com pele mais escura é proposta como melhoria futura. Não é evidência de coleta já realizada nem de redução de viés demonstrada neste estudo.

## 25. Validação clínica ainda futura

**Página 16 · 6.4**

**Trecho grifado:**

> Future work will involve prospective user studies with dermatologists, capturing both qualitative trust assessments and integration feedback, which are essential components for evidence-based certification.

**Comentário:**

RQ3/RQ7 — Estudos prospectivos com dermatologistas são trabalho futuro. Resultados computacionais e mapas de saliência não demonstram validação clínica prospectiva ou confiança dos profissionais já avaliada. O texto menciona preparação de documentação para aprovação ética; não apresenta aprovação ou estudo prospectivo concluído.

## 26. Veículo de publicação

**Página 1 · Cabeçalho editorial**

**Trecho grifado:**

> Engineering Applications of Artificial Intelligence 159 (2025) 111594

**Comentário:**

RQ8 — Artigo de pesquisa em periódico: Engineering Applications of Artificial Intelligence, volume 159, artigo 111594, 2025. DOI: 10.1016/j.engappai.2025.111594. Não é artigo de conferência nem revisão.

## 27. AP específico de hanseníase na curva PR

**Página 12 · Figura 6(b)**

**Rótulos da área marcada:**

> Leprosy 0.914 all classes 0.858 mAP\@0.5

**Comentário:**

RQ4/RQ6 — A legenda da curva precisão–recall informa AP\@0.5 de 0,914 para Leprosy (91,4%) e mAP\@0.5 global de 0,858 (85,8%). Trata-se de AP por classe, não accuracy. Difere do mAP50 de 84% para Leprosy na Figura 10 e do mAP50 global principal de 91,2%. Não localizei justificativa suficiente para conciliar essas apresentações.

## 28. F1 e mAP50 específicos de hanseníase

**Página 14 · Figura 10**

**Rótulos da área marcada:**

> Leprosy 81 84

**Comentário:**

RQ4/RQ6 — Na Figura 10, as barras de Leprosy indicam F1-Score 81% e mAP50 84%, conforme as legendas azul e laranja. Esses são resultados específicos de hanseníase. A Figura 6(b) apresenta AP\@0.5 de 91,4% para a mesma classe; manter a divergência registrada. A contagem de 643 refere-se a anotações/instâncias, não a pacientes.
