---
tags: []
parent: 'Reimagining leprosy elimination with AI analysis of a combination of skin lesion images with demographic and clinical data'
collections:
    - TCC_Leituras
$version: 345
$libraryID: 2
$itemKey: R26CNWCQ

---
# Extração de dados — Reimagining leprosy elimination with AI analysis of a combination of skin lesion images with demographic and clinical data

Revisão Evidentia 312 · TCC\_Leituras

**1. Título:** Reimagining leprosy elimination with AI analysis of a combination of skin lesion images with demographic and clinical data

**2. Autores:** Raquel R Barbieri; Yixi Xu; Lucy Setian; Paulo Thiago Souza-Santos; Anusua Trivedi; Jim Cristofono; Ricardo Bhering; Kevin White; Anna M Sales; Geralyn Miller; José Augusto C Nery; Michael Sharman; Richard Bumann; Shun Zhang; Mohamad Goldust; Euzenir N Sarno; Fareed Mirza; Arielle Cavaliero; Sander Timmer; Elena Bonfiglioli; Cairns Smith; David Scollard; Alexander A. Navarini; Ann Aerts; Juan Lavista Ferres; Milton O Moraes

**3. Ano de publicação:** 2022

**4. Fonte de publicação:** The Lancet Regional Health - Americas

**5. Tipo de estudo:** Estudo clínico observacional de desenvolvimento e avaliação interna de assistente diagnóstico, com coleta padronizada de imagens e metadados.

**6. Tipo de veículo de publicação:** Artigo de periódico.

**7. RQ1 Técnica de visão computacional utilizada:** Fotografias panorâmicas, de perto e da borda, anotadas com VGG Image Annotator. CNNs predizem por imagem; histogramas reúnem probabilidades das lesões por paciente para combinação com dados clínicos.

**8. RQ2 Dataset utilizado:** AI4Leprosy, base aberta da clínica de hanseníase da Fiocruz (Rio de Janeiro, Brasil); DOI do repositório: 10.35078/1PSIEL.

**9. RQ2 Características da população / Doença ou manifestação dermatológica:** 228 recrutados; 222 analisados com lesões suspeitas de hanseníase ou de outras dermatoses (máculas, placas, nódulos). Idade >6 anos; excluídos HIV/tuberculose e ausência de confirmação. Confirmação/exclusão por avaliação clínica, histologia, baciloscopia e qPCR em casos equívocos. Resultados: 582 lesões e 1.226 imagens na amostra final; o resumo relata 1.229 imagens coletadas e 585 registros de metadados.

**10. RQ2 Quantidade de imagens:** 1226

**11. RQ3 Avaliação de desempenho dos modelos:** Somente imagem: ResNet-50 ajustada em close-ups, acurácia 66,60%, AUC 74,56% em validação cruzada. No teste de 40 pacientes, elastic-net com saídas do modelo de metadados + informações do paciente: acurácia 90%, AUC 96,46%, sensibilidade 89%, especificidade 91%. Essa configuração NÃO exige imagens. Na Tabela 3, com todas as entradas, elastic-net: 88%, 92%, 83%, 91%, respectivamente. Texto atribui maior AUC (98,74%) a RF apenas com dados do paciente; na tabela os valores arredondados nessa linha são 99% para XGB e 98% para RF.

**12. RQ4 Métricas utilizadas:** Acurácia, AUC ROC, sensibilidade e especificidade; médias/DP na validação cruzada e erros-padrão no teste. Importância por permutação e odds ratios para interpretação.

**13. RQ5 Informações sobre tom de pele:** Os autores dizem que a população brasileira permitiu coletar vários tipos de pele; sem escala, distribuição ou fototipos especificados. Cor da lesão não equivale ao tom basal de pele.

**14. RQ6 Comparação do desempenho entre tons de pele:** Não há comparação de desempenho por tom de pele.

**15. RQ7 Modelo ou Abordagem:** AI4Leprosy em dois estágios: modelo 1 (ResNet-50 e Inception-v4, ajuste integral vs. congelamento); modelo 2 (metadados: regressão logística elastic-net, XGBoost, random forest); modelo 3 (histogramas das saídas e/ou dados do paciente, mesmos três classificadores).

**16. RQ8 Avaliação de generalização do modelo:** Teste em pacientes distintos, porém provenientes do mesmo centro. Coleta em outros continentes, tons e smartphones é trabalho futuro; não há teste externo.

**17. Método de validação:** Hold-out aleatório por paciente: 182 desenvolvimento/40 teste; 5-fold CV para modelos 1–2 e seleção, posterior reajuste nos 182. Análises adicionais de regressão com validação cruzada repetida.

**18. Limitações e conclusões:** Amostra pequena de centro de referência, possível viés de seleção e dependência de dados clínicos coletados por especialistas. Fotografias isoladas tiveram desempenho inferior. Indicado para suspeição e encaminhamento; exige validação em atenção primária e outras populações.

## Trechos grifados e comentários

**[p. 3](zotero://open-pdf/library/items/WW7V7QB4?page=3\&annotation=GDKK8UJP)** — “Study design and workﬂow”\
Tipo de estudo — Coleta padronizada no centro de referência; confirmação diagnóstica subsequente.

**[p. 1](zotero://open-pdf/library/items/WW7V7QB4?page=1\&annotation=JIJRV3VM)** — “stored in an open-source dataset”\
RQ2 — Resumo: 1.229 imagens e 585 conjuntos de metadados; reconciliar com a contagem da amostra final nos Resultados.

**[p. 5](zotero://open-pdf/library/items/WW7V7QB4?page=5\&annotation=77PB7XMZ)** — “total of 582 skin lesions and 1226 images were collected”\
RQ2 — Contagem nos Resultados para os 222 participantes finais: 582 lesões e 1.226 imagens. Este é o denominador registrado no campo inteiro.

**[p. 3](zotero://open-pdf/library/items/WW7V7QB4?page=3\&annotation=5QIHB7LJ)** — “a close-up photo and”\
RQ1 — Aquisição de vista panorâmica, close-up e borda com pele normal adjacente.

**[p. 5](zotero://open-pdf/library/items/WW7V7QB4?page=5\&annotation=FLHGQN8H)** — “The remaining 182 patients were used for both model”\
Método de validação — 182 pacientes para desenvolvimento e seleção por 5-fold CV, 40 reservados ao teste do modelo final no mesmo centro.

**[p. 5](zotero://open-pdf/library/items/WW7V7QB4?page=5\&annotation=2PCF6TN5)** — “Inception-v4 or”\
RQ7 — Comparação entre Inception-v4 e ResNet-50; apenas imagens: melhor resultado com ResNet-50 ajustada em close-ups.

**[p. 5](zotero://open-pdf/library/items/WW7V7QB4?page=5\&annotation=R79RYU9T)** — “although lower accuracy”\
RQ3/RQ4 — ResNet-50 em close-up: 66,60% de acurácia e AUC 74,56%.

**[p. 6](zotero://open-pdf/library/items/WW7V7QB4?page=6\&annotation=EBYAV87P)** — “Model 2 outputs + patient info”\
RQ3 — Tabela 3: elastic-net com informações do paciente e saídas de metadados, sem usar imagens, alcançou acurácia 90%, sensibilidade 89%, especificidade 91% e AUC 96,46% (texto).

**[p. 8](zotero://open-pdf/library/items/WW7V7QB4?page=8\&annotation=3W9X2JZ4)** — “allowed image collection from a variety of skin types.”\
RQ5/RQ6/RQ8 — Diversidade mencionada qualitativamente, sem desempenho estratificado. Avaliação em outros tipos de pele e cenários é futura.

**[p. 8](zotero://open-pdf/library/items/WW7V7QB4?page=8\&annotation=K3J548BC)** — “lesions suspect of leprosy”\
Limitações — Ferramenta de suspeição para encaminhamento. Imagens isoladas foram inferiores à informação clínica; generalização independente não demonstrada.
