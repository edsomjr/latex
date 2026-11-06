---
tags: []
parent: 'Leprosy Skin Lesion Detection: An AI Approach Using Few Shot Learning in a Small Clinical Dataset'
collections:
    - TCC_Leituras
$version: 378
$libraryID: 2
$itemKey: PBR2UV92

---
# Extração de dados — Leprosy Skin Lesion Detection: An AI Approach Using Few Shot Learning in a Small Clinical Dataset

Revisão Evidentia 312 · TCC\_Leituras

**1. Título:** Leprosy Skin Lesion Detection: An AI Approach Using Few Shot Learning in a Small Clinical Dataset

**2. Autores:** R Beesetty; S A Reddy; S Modali; G Sunkara; J Dalal; J Damagathla; D Banerjee; M Venkatachalapathy

**3. Ano de publicação:** 2023

**4. Fonte de publicação:** Indian Journal of Leprosy, vol. 95, pp. 89–102.

**5. Tipo de estudo:** Artigo original exploratório de viabilidade; coleta clínica não intervencionista de imagens e experimento computacional de triagem.

**6. Tipo de veículo de publicação:** Artigo de periódico.

**7. RQ1 Técnica de visão computacional utilizada:** Fotografia multimodal: câmera SLR, duas orientações de polarização e smartphone; agrupamento hierárquico aglomerativo de Ward de características morfológicas; aprendizagem de similaridade entre pares de imagens e classificação few-shot.

**8. RQ2 Dataset utilizado:** Dataset clínico próprio coletado com o Sivananda Rehabilitation Home, em campanhas em distritos de Telangana, Índia. 1.931 imagens de 396 lesões em quatro modos e, em alguns casos, diferentes campos de visão. Uma categoria burn patch foi excluída da modelagem; número de imagens efetivamente selecionadas para o modelo não discriminado.

**9. RQ2 Características da população / Doença ou manifestação dermatológica:** 151 pacientes dermatológicos elegíveis; 368 lesões de hanseníase e 28 lesões não hansênicas de oito condições simulantes. Inclusão de todas as idades e gêneros; excluídos pacientes com >3 meses de tratamento. Diagnóstico clínico por especialista segundo critérios OMS; não há confirmação laboratorial universal.

**10. RQ2 Quantidade de imagens:** 1931

**11. RQ3 Avaliação de desempenho dos modelos:** Rede siamesa, acurácia treino/teste na Tabela 3: 2-way 1-shot 91,25%/73,13% (resumo e conclusão: 73,12%); 3-way 1-shot 89,38%/73,75%. Teste hanseníase vs. demais: sensibilidade/especificidade 72,39%/73,66% (2-way) e 69,33%/77,65% (3-way). Acurácia de teste dos baselines, 2-way/3-way: vizinho mais próximo em pixels 26,56%/13,75%; embeddings Inception V3 17,19%/20,31%.

**12. RQ4 Métricas utilizadas:** Acurácia episódica; sensibilidade e especificidade, calculadas por esquema um contra os demais. Sem IC reportados para essas estimativas.

**13. RQ5 Informações sobre tom de pele:** Ficha clínica registra grau de bronzeamento (nenhum, leve, moderado, grave). A pigmentação da lesão é classificada como hipo, normal ou hiper e usada no agrupamento morfológico. Não equivale ao tom constitutivo da pele; não se relata Fitzpatrick, colorimetria ou distribuição basal de fototipos.

**14. RQ6 Comparação do desempenho entre tons de pele:** Não há desempenho estratificado por grau de bronzeamento nem por tom constitutivo; os grupos morfológicos não são grupos de tom de pele.

**15. RQ7 Modelo ou Abordagem:** Few-shot learning em rede siamesa: quatro blocos convolucionais (Conv2D 3×3, 64 filtros, batch normalization, ReLU e max pooling), camada de 4.096 dimensões, norma L2 e sigmoide; resultados com perda contrastiva, Adam e 40 mil iterações. Comparação com vizinho mais próximo em pixels e em embeddings de Inception V3 pré-treinado.

**16. RQ8 Avaliação de generalização do modelo:** Testa subgrupos morfológicos e doenças com rótulos não vistos no treino, no mesmo estudo de coleta. Não há validação externa em outra base. Treino e teste participaram dos ciclos de monitoramento; independência por paciente não explicitada. Diferentes dispositivos na captura não constituem validação independente entre dispositivos.

**17. Método de validação:** Divisão interna por classes disjuntas: nove classes para treino e sete para teste (Tabela 2). Tarefas episódicas aleatórias 2-way e 3-way com um exemplo por classe (320 tarefas por experimento); validação dos dois subconjuntos a cada 256 iterações com 160 tarefas 2-way 1-shot.

**18. Limitações e conclusões:** A triagem por imagem mostrou viabilidade exploratória, mas a amostra é pequena e desbalanceada, houve interrupção pela pandemia e faltam simulantes. Rótulos clínicos, ruído na anotação e variações de campo de visão podem limitar o desempenho. Não cobre hanseníase puramente neural ou infiltração difusa sem lesão distinguível. Autores pedem validação clínica e laboratorial, maior amostra e fotos de celulares obtidas por profissionais de campo.

## Trechos grifados e comentários

**[p. 1](zotero://open-pdf/library/items/DJH2KPH9?page=1\&annotation=T95WVBMK)** — “This is an exploratory research study”\
Tipo de estudo — avaliação exploratória da viabilidade de triagem de hanseníase por imagens.

**[p. 3](zotero://open-pdf/library/items/DJH2KPH9?page=3\&annotation=H8R2JY7B)** — “with the Sivananda Rehabilitation Home (SRH), Hyderabad, India.”\
RQ2 — Coleta clínica própria em Telangana, Índia, com a rede de clínicas do SRH.

**[p. 1](zotero://open-pdf/library/items/DJH2KPH9?page=1\&annotation=GQ75GAIF)** — “A total of 368 clinically diagnosed leprosy and 28 non-leprosy skin lesions were collected by an expert leprologist from 151 eligible patients”\
RQ2 — 396 lesões em 151 pacientes; 368 hansênicas e 28 simulantes. As contagens são de lesões e não de imagens.

**[p. 6](zotero://open-pdf/library/items/DJH2KPH9?page=6\&annotation=EEXKHMY7)** — “with extra samples, constituting 1931 images.”\
RQ1/RQ2 — 1.931 imagens adquiridas em quatro modos. Algumas lesões foram fotografadas com diferentes campos de visão; não confundir 396 lesões com o total de fotografias.

**[p. 5](zotero://open-pdf/library/items/DJH2KPH9?page=5\&annotation=C7MLYB6X)** — “Degree of skin tanning”\
RQ5/RQ6 — A ficha registra grau de bronzeamento em quatro níveis. Não há escala de fototipo relatada nem comparação de desempenho por tom de pele.

**[p. 5](zotero://open-pdf/library/items/DJH2KPH9?page=5\&annotation=IHJE5PRU)** — “Pigmentation”\
RQ5 — Na seção de dados da lesão, pigmentação hipo, normal ou hiper descreve a lesão, não o tom de pele basal do participante.

**[p. 8](zotero://open-pdf/library/items/DJH2KPH9?page=8\&annotation=HWTK2XGA)** — “A hierarchical agglomerative clustering algorithm was applied to all leprosy lesions using Ward’s distance metric.”\
RQ1 — Agrupamento morfológico hierárquico de Ward para gerar nove subgrupos de lesões hansênicas.

**[p. 9](zotero://open-pdf/library/items/DJH2KPH9?page=9\&annotation=MCAW5SPC)** — “The Siamese network encoder used in the study has four convolutional blocks”\
RQ7 — Rede siamesa few-shot com quatro blocos convolucionais e aprendizado contrastivo. Baselines de vizinho mais próximo com pixels e com embeddings Inception V3.

**[p. 9](zotero://open-pdf/library/items/DJH2KPH9?page=9\&annotation=3QKUY7IM)** — “The data were split into training data and test data by forming a disjoint set of train-set labels and test-set labels.”\
RQ8/Método — Classes de treino e teste disjuntas, porém de uma mesma coleta. Sem avaliação independente em outra base.

**[p. 10](zotero://open-pdf/library/items/DJH2KPH9?page=10\&annotation=IZ44PS98)** — “Both the training set and the testing set were validated for every 256 iterations”\
Método — Ambos os subconjuntos foram monitorados periodicamente durante o treinamento, o que limita a independência da estimativa de teste.

**[p. 9](zotero://open-pdf/library/items/DJH2KPH9?page=9\&annotation=8D84NJ6D)** — “Siamese networks 91.25% 73.13% 89.38% 73.75%”\
RQ3/RQ4 — Tabela 3: acurácias treino/teste de 91,25%/73,13% para 2-way e 89,38%/73,75% para 3-way. No resumo/conclusão, o primeiro teste aparece como 73,12%.

**[p. 10](zotero://open-pdf/library/items/DJH2KPH9?page=10\&annotation=W24DW8UN)** — “Siamese model 72.39% 73.66% 69.33% 77.65%”\
RQ3/RQ4 — Tabela 4: sensibilidade/especificidade de teste 72,39%/73,66% (2-way) e 69,33%/77,65% (3-way).

**[p. 12](zotero://open-pdf/library/items/DJH2KPH9?page=12\&annotation=REZIGHRH)** — “Another major limitation in our study is the lack of sufficient leprosy-simulant classes”\
Limitações — Poucas lesões simulantes, amostra pequena e rótulos clínicos. Autores propõem validação futura com confirmação laboratorial e fotos capturadas por trabalhadores de saúde.
