---
tags: []
parent: 'Skin Diseases Detection Using LBP and WLD: An Ensembling Approach'
collections:
    - TCC_Leituras
$version: 334
$libraryID: 2
$itemKey: CENWP37L

---
# Extração de dados — Skin Diseases Detection Using LBP and WLD: An Ensembling Approach

Revisão Evidentia 312 · TCC\_Leituras

**1. Título:** Skin Diseases Detection Using LBP and WLD: An Ensembling Approach

**2. Autores:** Arnab Banerjee; Somenath Sarkar; Mita Nasipuri; Nibaran Das

**3. Ano de publicação:** 2023

**4. Fonte de publicação:** SN Computer Science, vol. 5, art. 72 (edição 2024; publicação online em 07/12/2023 segundo o registro Zotero). DOI: 10.1007/s42979-023-02395-8.

**5. Tipo de estudo:** Pesquisa original experimental de desenvolvimento e comparação de classificadores de imagens clínicas.

**6. Tipo de veículo de publicação:** Artigo de periódico.

**7. RQ1 Técnica de visão computacional utilizada:** Recorte manual da região proeminente, redimensionamento para 144 × 144 e conversão em cinza. Fusão de histogramas dos descritores de textura LBP e WLD invariantes à rotação, em quatro regiões delimitadas pelo centro de gravidade (cogriWeberLBP).

**8. RQ2 Dataset utilizado:** JUCMATER: Skindb.v1, base própria de fotografias obtidas no ambulatório da School of Tropical Medicine, Kolkata, Índia, durante mais de um ano; acesso por solicitação.

**9. RQ2 Características da população / Doença ou manifestação dermatológica:** 141 pacientes; múltiplas lesões podiam gerar múltiplas imagens. Quatro classes: hanseníase (262 imagens), vitiligo (210), pitiríase versicolor (242) e pele normal (162). Imagens borradas excluídas.

**10. RQ2 Quantidade de imagens:** 876

**11. RQ3 Avaliação de desempenho dos modelos:** Acurácia global de 91,3793% com cogriWeberLBP + Multi-SVM (parâmetros de vizinhança 16,2; C=8, gamma=0,125). Entre as CNNs: GoogLeNet 73%, ResNet152 78%, MobileNet 81%, DenseNet121 83%, ResNet101 89%. Vantagem de 2,38 pontos percentuais sobre a melhor CNN; não é sensibilidade para hanseníase.

**12. RQ4 Métricas utilizadas:** Acurácia de reconhecimento (%); exemplos qualitativos de erros.

**13. RQ5 Informações sobre tom de pele:** Não há medida ou distribuição de tons de pele/fototipos. Cor das lesões é descrita visualmente; não representa fototipo do paciente.

**14. RQ6 Comparação do desempenho entre tons de pele:** Não comparado; não há resultados por tom de pele.

**15. RQ7 Modelo ou Abordagem:** Ensemble de descritores (cogriWeberLBP) com classificador Multi-SVM de kernel RBF e grid search; comparação com variações de LBP/WLD, DCT, DFT, GLCM e cinco CNNs.

**16. RQ8 Avaliação de generalização do modelo:** Somente teste interno da mesma base; sem avaliação externa. Não se esclarece se imagens do mesmo paciente foram mantidas em uma única partição.

**17. Método de validação:** Hold-out treino:teste de 4:1 sobre as imagens; grid search de C e gamma. Não há validação cruzada descrita como método de avaliação final.

**18. Limitações e conclusões:** Autores relatam confusão de placas brancas de hanseníase com vitiligo e de pele normal com manchas vermelhas com hanseníase. O método superou as alternativas nesta base; sugerem coletar mais imagens e explorar outros descritores e redes.

## Trechos grifados e comentários

**[p. 1](zotero://open-pdf/library/items/3Y55WDDP?page=1\&annotation=YKDI3SL6)** — “ORIGINAL RESEARCH”\
Tipo: pesquisa original em SN Computer Science. O registro indica publicação online em 2023 e a edição do PDF é de 2024.

**[p. 3](zotero://open-pdf/library/items/3Y55WDDP?page=3\&annotation=5GJYY2ZY)** — “the images of skin lesions from 141 patients were taken.”\
População: 141 pacientes do ambulatório da STM, Kolkata. O artigo admite múltiplas imagens por paciente.

**[p. 3](zotero://open-pdf/library/items/3Y55WDDP?page=3\&annotation=7MXQ7BP9)** — “A total of 876 images were considered”\
RQ2: JUCMATER: Skindb.v1 contém 262 imagens de hanseníase, 210 de vitiligo, 242 de pitiríase versicolor e 162 de pele normal.

**[p. 4](zotero://open-pdf/library/items/3Y55WDDP?page=4\&annotation=QFIHVPQ2)** — “The data set images were cropped and resized to 144 × 144”\
RQ1: recorte de lesão e padronização de tamanho; as imagens coloridas foram convertidas para tons de cinza. Não há avaliação por fototipo.

**[p. 8](zotero://open-pdf/library/items/3Y55WDDP?page=8\&annotation=UK45NVNM)** — “The data set was divided into 4:1 ratio for preparing the training and testing data set.”\
Validação/RQ8: hold-out interno na mesma base, sem demonstração de independência por paciente ou de validação externa.

**[p. 8](zotero://open-pdf/library/items/3Y55WDDP?page=8\&annotation=K84BLFVQ)** — “The grid search method was applied to find the best regularization parameter(C)”\
RQ7: ajuste do Multi-SVM RBF por busca em grade de C e gamma, usando os vetores de textura.

**[p. 1](zotero://open-pdf/library/items/3Y55WDDP?page=1\&annotation=AX6EHFFB)** — “This ensemble technique achieved 91.38% accuracy using a multilevel support vector machine”\
RQ3/RQ4: melhor resultado de acurácia global (quatro classes); o melhor comparador profundo, ResNet101, atingiu 89%.

**[p. 10](zotero://open-pdf/library/items/3Y55WDDP?page=10\&annotation=DTF93RIM)** — “big white patches were incorrectly detected as vitiligo.”\
Limitação: manchas brancas de hanseníase foram confundidas com vitiligo e pele normal com manchas vermelhas foi confundida com hanseníase.
