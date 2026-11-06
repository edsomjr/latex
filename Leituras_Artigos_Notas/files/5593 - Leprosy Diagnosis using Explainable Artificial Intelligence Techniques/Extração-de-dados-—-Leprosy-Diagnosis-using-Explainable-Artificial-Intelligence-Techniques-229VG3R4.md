---
tags: []
parent: 'Leprosy Diagnosis using Explainable Artificial Intelligence Techniques'
collections:
    - TCC_Leituras
$version: 325
$libraryID: 2
$itemKey: 229VG3R4

---
# Extração de dados — Leprosy Diagnosis using Explainable Artificial Intelligence Techniques

Revisão Evidentia 312 · TCC\_Leituras

**1. Título:** Leprosy Diagnosis using Explainable Artificial Intelligence Techniques

**2. Autores:** Asis Kaur Baweja; S Aditya; M. Kanchana

**3. Ano de publicação:** 2023

**4. Fonte de publicação:** International Conference on Sustainable Computing and Data Communication Systems (ICSCDS), IEEE, pp. 551–556.

**5. Tipo de estudo:** Estudo primário experimental de desenvolvimento e comparação de classificadores de imagens com explicabilidade pós-hoc.

**6. Tipo de veículo de publicação:** Artigo em anais de conferência.

**7. RQ1 Técnica de visão computacional utilizada:** Classificação binária de fotografias por CNN; rotação aleatória de 0 a 90°, redução de escala por fator 0,1 e desfoque; explicações com visualização de ativações, mapas de sensibilidade à oclusão e Grad-CAM.

**8. RQ2 Dataset utilizado:** Imagens selecionadas de DermNet NZ no Kaggle e de web scraping, submetidas a curadoria manual.

**9. RQ2 Características da população / Doença ou manifestação dermatológica:** Imagens cutâneas de hanseníase e de não hanseníase, em números iguais. Não informa número de pacientes, demografia nem confirmação clínica das imagens da web.

**10. RQ2 Quantidade de imagens:** Não informado ou não aplicável como total único. Deixar o campo inteiro vazio; ver dataset e população.

**11. RQ3 Avaliação de desempenho dos modelos:** Tabela 1 — LeprosyNet: acurácia 98%, precisão 97,5%, recall 98%, F1 97,5%; AlexNet: 81%, 80%, 82%, 80%; ResNet: 80% para as quatro métricas. Fig. 8, especificamente para a classe hanseníase: precisão 99%, recall 97%, F1 98%. LeprosyNet tem a maior AUC segundo os autores, sem número informado.

**12. RQ4 Métricas utilizadas:** Acurácia, precisão, recall, F1; curva ROC (TPR/FPR), AUC comparativa e resultados por classe.

**13. RQ5 Informações sobre tom de pele:** Não informa escala de tom de pele, fototipos nem distribuição dos exemplos por pigmentação.

**14. RQ6 Comparação do desempenho entre tons de pele:** Não há comparação entre tons de pele.

**15. RQ7 Modelo ou Abordagem:** LeprosyNet: CNN criada pelos autores com quatro camadas convolucionais, max pooling 3×3, batch normalization, ReLU e Adam. Comparadores AlexNet e ResNet, classificação adaptada à tarefa; profundidade da ResNet não especificada.

**16. RQ8 Avaliação de generalização do modelo:** Teste interno em imagens da mesma base composta. A comparação com trabalhos publicados não constitui avaliação externa. Sem teste em outra população, dispositivo ou base independente.

**17. Método de validação:** Hold-out por imagem com seleção aleatória: 80% treino e 20% teste. Transformações aplicadas aos dois subconjuntos; não há relato de separação por paciente ou controle de duplicatas.

**18. Limitações e conclusões:** Autores concluem que LeprosyNet supera os comparadores no teste interno e que seus mapas destacam lesões; sugerem aplicativo para triagem futura. Limites da evidência: volume da base não explicitado, rótulos de origem heterogênea, ausência de teste externo ou validação clínica das explicações.

## Trechos grifados e comentários

**[p. 1](zotero://open-pdf/library/items/LF437JGZ?page=1\&annotation=75MLCQAW)** — “Proceedings of the International Conference on Sustainable Computing and Data Communication Systems (ICSCDS-2023)”\
Fonte e veículo — trabalho nos anais da conferência IEEE ICSCDS 2023.

**[p. 2](zotero://open-pdf/library/items/LF437JGZ?page=2\&annotation=LXPQM5QD)** — “images from the dermnetnz dataset from Kaggle as well as manual cleaning of results obtained from web scraping.”\
RQ2 — Base composta a partir de DermNet NZ/Kaggle e web scraping. Não se informa o número total de imagens.

**[p. 2](zotero://open-pdf/library/items/LF437JGZ?page=2\&annotation=KL4HKCGJ)** — “Hence equal number of positive and negative examples are a part of the data set.”\
RQ2/RQ5/RQ6 — Classes de hanseníase e não hanseníase balanceadas. Não há estratificação por tom de pele; balanceamento das classes não demonstra diversidade demográfica.

**[p. 2](zotero://open-pdf/library/items/LF437JGZ?page=2\&annotation=ZKNJNDSX)** — “rotation, scale transformations, and blurring have been undertaken on both testing as well as training subdivisions.”\
RQ1/validação — Rotação, alteração de escala e desfoque foram aplicados tanto ao treino quanto ao teste.

**[p. 3](zotero://open-pdf/library/items/LF437JGZ?page=3\&annotation=7G4DT65H)** — “The proposed model has a linear architecture consisting of four convolutional layers.”\
RQ7 — LeprosyNet é uma CNN própria de quatro camadas convolucionais; comparadores: AlexNet e ResNet.

**[p. 1](zotero://open-pdf/library/items/LF437JGZ?page=1\&annotation=QFXBLF3X)** — “explainable AI techniques like Activation Layer Visualization, Occlusion Sensitivity and Grad-CAM are used.”\
RQ1/RQ7 — Três métodos de explicabilidade localizam regiões relevantes para a classificação.

**[p. 4](zotero://open-pdf/library/items/LF437JGZ?page=4\&annotation=LY9965JN)** — “The images in the test dataset are selected at random.”\
RQ8/Método — Hold-out aleatório por imagem, 80:20. Não é relatada avaliação externa.

**[p. 5](zotero://open-pdf/library/items/LF437JGZ?page=5\&annotation=YSH4GCYC)** — “LeprosyNet 0.975 0.98 0.975 0.98”\
RQ3/RQ4 — Tabela 1: precisão 0,975; recall 0,98; F1 0,975; acurácia 0,98. Acurácias dos comparadores: AlexNet 0,81 e ResNet 0,80.

**[p. 6](zotero://open-pdf/library/items/LF437JGZ?page=6\&annotation=EHL8JB44)** — “In future this model can be integrated into an app or website and can be used as a preliminary Leprosy detection test.”\
Limitações/conclusão — Aplicação para triagem preliminar é proposta futura; não foi avaliada em pacientes em uso clínico.
