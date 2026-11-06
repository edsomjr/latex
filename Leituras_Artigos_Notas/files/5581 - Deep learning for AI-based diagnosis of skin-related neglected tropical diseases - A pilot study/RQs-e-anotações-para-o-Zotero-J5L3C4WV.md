---
tags: []
parent: 'Deep learning for AI-based diagnosis of skin-related neglected tropical diseases: A pilot study'
collections:
    - TCC_Leituras
$version: 229
$libraryID: 2
$itemKey: J5L3C4WV

---
# RQs e anotações para o Zotero

**Artigo:** Rie R. Yotsu; Zhengming Ding; Jihun Hamm; Ronald E. Blanton. *Deep learning for AI-based diagnosis of skin-related neglected tropical diseases: A pilot study*. PLOS Neglected Tropical Diseases, 17(8), e0011230, 2023. **DOI:** 10.1371/journal.pntd.0011230.

**Fonte e escopo:** análise do PDF fornecido, 12 páginas, sem auditoria dos dados, código ou fontes externas. As oito RQs reproduzem os enunciados do exemplo anterior. As referências usam a posição no PDF, coincidente com a numeração impressa de 1 a 12. Comentários e interpretação estão neste Markdown; o PDF contém somente o artigo original grifado.

**Tipo de estudo e enquadramento:** estudo piloto experimental de classificação multiclasse de fotografias clínicas de cinco doenças tropicais negligenciadas cutâneas: úlcera de Buruli, hanseníase, micetoma, escabiose e bouba. Atende aos critérios temáticos de inclusão do protocolo: avalia IA em imagens humanas e inclui hanseníase entre as doenças. Publicado após 2020, em inglês, com texto completo; não é exclusivamente IA generativa. A duplicidade deve ser verificada na base da revisão. Não é segmentação nem validação de implantação no Brasil ou em Angola.

## RQ1 — Quais técnicas de visão computacional são utilizadas para identificar manifestações dermatológicas associadas à hanseníase?

**Resposta:** classificação supervisionada de imagens RGB por redes neurais convolucionais, com cinco classes de doença. O classificador recebe imagens e produz um vetor de cinco probabilidades. São usadas extração de características e transferência de aprendizado com ajuste dos parâmetros da rede.

As imagens são redimensionadas para **224 × 224 pixels**, com três canais RGB. O texto informa aumento de dados e normalização, mas não detalha todas as transformações. As representações têm 2.048 dimensões para ResNet-50 e 4.096 para VGG-16. Há análise qualitativa de erros e projeção das representações por **PCA**, que auxilia a visualização, não constitui um modelo diagnóstico adicional.

Dados clínicos foram coletados para apoiar a avaliação dos dermatologistas. A integração desses dados ao classificador é sugerida na discussão, especialmente perda de sensibilidade para hanseníase, mas não foi testada neste experimento. Não há avaliação de segmentação ou detecção por caixas.

**Evidências:** páginas 3–5, seção Methods; páginas 8–9, Feature visualization e Discussion; anotações 05–06, 15 e 17.

## RQ2 — Quais conjuntos de dados e populações são utilizados no desenvolvimento e na avaliação desses modelos?

**Resposta:** coleção própria de fotografias clínicas obtidas prospectivamente em **Costa do Marfim e Gana**, por meio de projetos de documentação digital e teledermatologia. O conjunto tem **1.709 imagens de 506 pacientes**, todos descritos como provenientes de populações africanas de pele escura, com Fitzpatrick IV ou superior.

| Característica       | Informação do artigo                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------ |
| Locais de coleta     | Seis distritos de saúde: quatro na Costa do Marfim e dois em Gana                          |
| Aquisição            | Enfermeiros e agentes comunitários treinados; campo e clínicas rurais                      |
| Dispositivo          | Câmera do tablet Lenovo Tab M10 FHD Plus                                                   |
| Formato original     | JPEG, 1.920 × 2.560 pixels                                                                 |
| Unidade de avaliação | Imagem; múltiplas fotografias por paciente                                                 |
| Rótulos              | Diagnósticos dermatológicos; confirmação laboratorial em parte dos casos de Buruli e bouba |
| Tom de pele          | Fitzpatrick IV ou superior; sem distribuição por fototipo                                  |
| Acesso               | Não público; solicitação institucional indicada no artigo                                  |


| Doença           | Pacientes | Imagens   |
| ---------------- | --------- | --------- |
| Úlcera de Buruli | 200       | 784       |
| Hanseníase       | 38        | 131       |
| Micetoma         | 12        | 32        |
| Escabiose        | 107       | 389       |
| Bouba            | 149       | 373       |
| **Total**        | **506**   | **1.709** |


Entre os casos de Buruli, 97 pacientes/361 imagens têm PCR positivo; para bouba, 62 pacientes/147 imagens têm DPP positivo. Essas confirmações não se estendem automaticamente à hanseníase. O subconjunto da Task 1(b) contém 1.060 imagens ao restringir Buruli e bouba aos positivos laboratoriais, mantendo as demais doenças.

Diagnósticos remotos são avaliados independentemente por dois dermatologistas experientes, com terceiro avaliador e discussão em caso de discordância. Quando disponível, o diagnóstico presencial é priorizado. O estudo relata aprovação ética e consentimento escrito.

**Disponibilidade declarada:** dados não públicos por risco à privacidade. O artigo indica contato com Tulane Human Research Protection Office & Institutional Review Boards, **<irbmain@tulane.edu>**, para acesso. Isso não garante autorização ou disponibilidade atual.

**Evidências:** páginas 1, 3–5, Data Availability, Data collection, Dataset screening, Tabela 1 e Analysis; anotações 01–04 e 21.

## RQ3 — Quais métodos, procedimentos são utilizados para avaliar o desempenho desses modelos e quais resultados são reportados?

**Resposta:** avaliação interna com separação descrita por pacientes, comparação entre duas arquiteturas e variação da proporção de treinamento. O texto informa ausência de sobreposição entre pacientes de treino e teste. As tabelas descrevem k como percentual de imagens; o procedimento de seleção é descrito por pacientes. Preservar essa diferença de redação sem presumir uma divisão aleatória independente por imagem.

*   **Task 1(a):** todos os casos, 1.709 imagens; proporções de treino de 30%, 40%, 50%, 60% e 70%.
*   **Task 1(b):** 1.060 imagens, com Buruli e bouba restritos aos casos positivos nos testes laboratoriais; mesmas proporções de treino.
*   **Task 2(a)/(b):** ResNet-50, comparando treinamento com 50 pacientes de Buruli diagnosticados clinicamente versus 50 com PCR positivo, mantendo as amostras de treino das outras doenças e o mesmo conjunto de teste.

Na Task 2, o treino também inclui 19 pacientes de hanseníase, 6 de micetoma, 54 de escabiose e 31 de bouba. O teste é descrito com 100 pacientes de Buruli, 19 de hanseníase, 5 de micetoma, 54 de escabiose e 75 de bouba. **Inconsistência do relato:** a Tabela 1 apresenta 107 pacientes com escabiose, enquanto a descrição da Task 2 soma 54 + 54 = 108, apesar de afirmar ausência de sobreposição. O texto não esclarece a divergência; ela não comprova vazamento.

Os modelos usam SGD com momentum 0,9, PyTorch e GPU NVIDIA Titan V. Não são informados no texto principal número de épocas, learning rate, batch size, sementes, validação cruzada, intervalos de confiança ou testes de significância.

A ResNet-50 chega a **84,63%** de acurácia global na Task 1(a), k=70%. Na Task 2, as acurácias globais são **77% e 80%**. Essas medidas não representam o acerto específico de hanseníase. Não comparar Tasks 1(a) e 1(b) como se apenas a confirmação laboratorial variasse: os tamanhos e a composição também mudam.

**Evidências:** páginas 4–7, Analysis, Tabelas 1–3 e Figura 1; anotações 07–14.

## RQ4 — Quais métricas são utilizadas para avaliar o desempenho desses modelos e quais resultados são reportados?

**Resposta:** **Top-1 accuracy e Matthews correlation coefficient (MCC)**, além de matrizes de confusão por doença. A unidade é imagem; não são resultados por paciente nem por pixel. Não são reportados F1, AUC, precisão e especificidade dos modelos como resultados principais.

Valores da **Tabela 2, página 6 — Task 1(a), 1.709 imagens**:

| Modelo    | Treino k (%) | Top-1 accuracy (%) | MCC        |
| --------- | ------------ | ------------------ | ---------- |
| ResNet-50 | 30           | 78,55              | 0,6776     |
| ResNet-50 | 40           | 79,36              | 0,6897     |
| ResNet-50 | 50           | 82,20              | 0,7308     |
| ResNet-50 | 60           | 82,84              | 0,7394     |
| ResNet-50 | 70           | **84,63**          | **0,7715** |
| VGG-16    | 30           | 76,61              | 0,6440     |
| VGG-16    | 40           | 78,45              | 0,6758     |
| VGG-16    | 50           | 80,55              | 0,7038     |
| VGG-16    | 60           | 80,27              | 0,6984     |
| VGG-16    | 70           | 82,22              | 0,7336     |


Valores da **Tabela 3, página 6 — Task 1(b), 1.060 imagens**:

| Modelo    | Treino k (%) | Top-1 accuracy (%) | MCC        |
| --------- | ------------ | ------------------ | ---------- |
| ResNet-50 | 30           | 75,71              | 0,6505     |
| ResNet-50 | 40           | 76,52              | 0,6615     |
| ResNet-50 | 50           | 77,19              | 0,6725     |
| ResNet-50 | 60           | 79,15              | 0,7011     |
| ResNet-50 | 70           | **84,17**          | **0,7706** |
| VGG-16    | 30           | 73,64              | 0,6204     |
| VGG-16    | 40           | 74,93              | 0,6407     |
| VGG-16    | 50           | 75,79              | 0,6515     |
| VGG-16    | 60           | 78,72              | 0,6948     |
| VGG-16    | 70           | 79,44              | 0,7011     |


**Negrito:** maior valor de cada métrica em cada tabela. A célula 75,79% aparece com símbolo de porcentagem duplicado no original; o valor numérico foi preservado.

**Task 2 — resultados globais e específicos, páginas 6–7:**

| Resultado                                                  | Task 2(a): diagnóstico clínico de Buruli | Task 2(b): PCR positivo de Buruli |
| ---------------------------------------------------------- | ---------------------------------------- | --------------------------------- |
| Acurácia global informada no texto                         | 77%                                      | 80%                               |
| Hanseníase corretamente classificada, diagonal da Figura 1 | 12%                                      | 13%                               |
| Hanseníase classificada como escabiose, Figura 1           | 66%                                      | 64%                               |


**Interpretação:**

*   Os 12% e 13% são valores lidos diretamente da matriz normalizada pela classe real, interpretáveis como **recall/sensibilidade da classe hanseníase por imagem**. Os autores não os apresentam em uma tabela separada denominada sensibilidade.
*   O aumento de 12% para 13% equivale a 1 ponto percentual. Não há teste de significância apresentado.
*   Não usar 84,63% como acurácia específica da hanseníase, nem misturar resultados das Tasks 1 e 2.
*   A matriz contém percentuais arredondados; não há suporte suficiente para reconstruir exatamente precisão, especificidade ou F1 sem contagens por classe no teste.
*   O artigo descreve MCC como 0–1; sua faixa matemática usual é −1 a +1. Os valores reportados devem ser preservados.
*   A tendência com mais dados é de melhora, mas não é estritamente monotônica: a VGG-16 cai de 80,55% para 80,27% entre k=50% e k=60% na Tabela 2.
*   Valores de sensibilidade de testes clínicos/PCR citados na discussão pertencem a outros estudos, não à avaliação destes modelos.

**Evidências:** páginas 5–7 e 9; Tabelas 2–3 e Figura 1; anotações 08–14.

## RQ5 — Como o desempenho dos modelos varia entre diferentes grupos ou tons de pele?

**Resposta:** **não é possível determinar pelo artigo**. Todas as imagens são descritas como provenientes de populações africanas de pele escura, com Fitzpatrick IV ou superior, mas não há contagem por fototipo nem desempenho separado por IV, V ou VI. Não há comparação com pele clara, métricas de equidade ou análise por sexo/idade.

O estudo traz evidência em pele escura, mas não demonstra igualdade de desempenho entre tons nem disparidade racial. A discussão sobre fairness aborda desbalanceamento entre classes de doença e escassez/diversidade de imagens. Fototipo e identidade racial não são medidas equivalentes.

**Registro sugerido:** “Populações africanas de pele escura, Fitzpatrick IV ou superior; distribuição por fototipo e desempenho entre grupos não reportados.”

**Evidências:** página 3, Introduction; páginas 9–10, Discussion; anotações 01–02 e 18. A ausência de estratificação não foi convertida em uma afirmação textual atribuída aos autores.

## RQ6 — Quais modelos e abordagens de inteligência artificial são utilizados para identificar manifestações dermatológicas associadas à hanseníase?

**Resposta:** duas CNNs, **ResNet-50 e VGG-16**, pré-treinadas no ImageNet e ajustadas para classificação supervisionada de cinco doenças. Não há avaliação de U-Net, Transformer ou IA generativa neste estudo.

| Modelo    | Representação   | Tarefa                         | Avaliação                           |
| --------- | --------------- | ------------------------------ | ----------------------------------- |
| ResNet-50 | 2.048 dimensões | Classificação de cinco doenças | Tasks 1 e 2; análise de erros e PCA |
| VGG-16    | 4.096 dimensões | Classificação de cinco doenças | Task 1                              |


O classificador final produz cinco probabilidades. O texto descreve atualização dos parâmetros da rede, sustentando o enquadramento como fine-tuning/transferência de aprendizado, não somente uso de características congeladas. ImageNet é pré-treinamento, não validação externa para hanseníase.

A discussão atribui vantagens à profundidade da ResNet-50, mas não apresenta ablação que isole esse fator. Também não há benchmark de latência, memória ou custo que sustente conclusões operacionais sobre eficiência.

**Evidências:** páginas 4–5 e 8–9; anotações 05–06 e 15–17.

## RQ7 — Como a capacidade de generalização dos modelos é avaliada, especialmente quando são utilizados conjuntos de dados diferentes daqueles empregados no treinamento?

**Resposta:** teste interno com pacientes separados do treinamento. A análise por PCA mostra qualitativamente menor separação das classes no teste. **Não localizei validação externa/cross-dataset**, avaliação deixando um país exclusivamente para teste ou teste no Brasil/Angola.

Dados de dois países não equivalem automaticamente a validação externa. As comparações de tamanho/composição dos conjuntos são experimentos internos. O artigo não mede gap por dispositivo, país, fototipo ou serviço.

Os autores reconhecem poucos casos, desbalanceamento e heterogeneidade de iluminação, fundo e apresentação das lesões. Para hanseníase, relatam diversidade de formas clínicas e feridas/deformidades associadas à neuropatia. A tentativa de estratificar apresentações reduziu ainda mais as amostras, sem resultados considerados úteis pelos autores. Isso não é evidência de validação bem-sucedida por subtipo.

A coleta em campo e clínicas rurais aproxima os dados do contexto de recursos limitados, mas não comprova benefício do modelo implantado na rede pública. A utilidade clínica permanece uma possibilidade discutida.

**Registro sugerido:** “Avaliação interna com separação declarada por pacientes; generalização explorada qualitativamente por PCA; validação externa e impacto assistencial não reportados.”

**Evidências:** páginas 5 e 8–10; anotações 07, 15–17 e 19–20.

## RQ8 — O artigo foi publicado em que tipo de veículo de publicação? (revista, conferência)

**Resposta:** **revista científica** — *PLOS Neglected Tropical Diseases*, volume **17**, número **8**, artigo **e0011230**, publicado em **14 de agosto de 2023**. DOI **10.1371/journal.pntd.0011230**. A primeira página identifica “RESEARCH ARTICLE”.

**Evidência:** página 1, cabeçalho e bloco editorial. Os metadados editoriais são legíveis no original, sem grifo específico.

## Síntese para a ficha de extração

*   **Tarefa:** classificação de cinco doenças cutâneas, incluindo hanseníase; não segmentação.
*   **Dataset/população:** 1.709 imagens/506 pacientes, Costa do Marfim e Gana; hanseníase: 131 imagens/38 pacientes; Fitzpatrick IV ou superior.
*   **Modelos:** ResNet-50 e VGG-16, ImageNet e ajuste supervisionado.
*   **Avaliação:** teste interno, separação declarada por pacientes, variação de proporções de treino e comparação de composição diagnóstica. Divergência na contagem de escabiose da Task 2 deve ser registrada.
*   **Melhor resultado global da Task 1(a):** Top-1 accuracy 84,63%, MCC 0,7715, ResNet-50, k=70%.
*   **Hanseníase na Task 2:** recall interpretado da matriz de 12% e 13%; não confundir com acurácia global.
*   **Tons de pele:** população de pele escura descrita; comparação por tom não realizada. **Generalização externa:** não localizada.
*   **Contribuição à RQ central do protocolo:** avaliar desempenho específico da hanseníase, além dos resultados agregados; considerar separação por paciente e análise de erros. O estudo não estabelece validade para a rede pública brasileira ou angolana.

# Trechos e notas para o Zotero

Cada número corresponde a um grifo no PDF, preservando a numeração da análise anterior. Os fragmentos abaixo são transcritos das áreas grifadas, com quebras de linha normalizadas; alguns são âncoras curtas cujo contexto está indicado no comentário. Os comentários podem ser copiados diretamente para o Zotero. Não há comentários incorporados ao PDF.

## 01. População e tom de pele

**Página 3**

**Trecho grifado:**

> All images are from

**Comentário:**

RQ2/RQ5 — População: todas as imagens são de populações africanas de pele escura, Fitzpatrick IV ou superior. Não há distribuição individual por fototipo nem comparação entre tons. Fototipo não equivale a identidade racial.

## 02. Fototipos incluídos

**Página 3**

**Trecho grifado:**

> Fitzpatrick skin type IV or above.

**Comentário:**

RQ5/RQ7 — Relevância direta para pele escura. Não extrapolar automaticamente para Brasil ou Angola.

## 03. Local e contexto da coleta

**Página 3**

**Trecho grifado:**

> six health districts

**Comentário:**

RQ2/RQ7 — Coleta em seis distritos de saúde de Costa do Marfim e Gana, por enfermeiros/agentes comunitários, em campo e clínicas rurais. Contexto de recursos limitados; não é validação no SUS ou em Angola.

## 04. Tamanho e composição do dataset

**Página 4**

**Trecho grifado:**

> Table 1. Patient and image sample sizes.

**Comentário:**

RQ2 — Dataset: 1.709 imagens / 506 pacientes. Hanseníase: 131 imagens / 38 pacientes. Classes desbalanceadas; múltiplas fotos por paciente.

## 05. Arquiteturas avaliadas

**Página 4**

**Trecho grifado:**

> ResNet-50 (50-layer residual neural network)

**Comentário:**

RQ1/RQ6 — Modelos efetivamente avaliados: ResNet-50 e VGG-16. Classificação supervisionada multiclasse (cinco doenças), não segmentação.

## 06. Pré-treinamento e preparo das imagens

**Página 4**

**Trecho grifado:**

> trained on the ImageNet dataset,

**Comentário:**

RQ1/RQ6 — Pré-treinamento ImageNet, imagens RGB 224 x 224, aumento de dados e normalização; ajuste dos parâmetros da rede. Evidência de transferência de aprendizado/fine-tuning.

## 07. Separação entre treinamento e teste

**Página 5**

**Trecho grifado:**

> the remaining patients were used to test

**Comentário:**

RQ3/RQ7 — Separação descrita por pacientes: imagens de pacientes distintos em treino e teste. Importante com múltiplas fotografias do mesmo indivíduo. Não é validação externa.

## 08. Métricas de desempenho

**Página 5**

**Trecho grifado:**

> Top-1 accuracy

**Comentário:**

RQ3/RQ4 — Métricas principais: Top-1 accuracy e MCC. Acurácia global de cinco classes não é sensibilidade específica para hanseníase.

## 09. Intervalo do MCC

**Página 5**

**Trecho grifado:**

> (MCC, 0\~1)

**Comentário:**

RQ4 — Nota crítica: os autores descrevem MCC como 0 a 1; a faixa matemática usual é -1 a +1. Registrar fielmente os resultados sem reproduzir essa limitação como definição geral.

## 10. Comparação com teste comum

**Página 5**

**Trecho grifado:**

> The test set was the same for the two models,

**Comentário:**

RQ3 — Task 2: mesmo teste e comparação de treinamento com diagnóstico clínico versus PCR positivo de Buruli. Não significa confirmação laboratorial da hanseníase.

## 11. Resultado global da ResNet-50

**Página 6**

**Trecho grifado:**

> 84.63%

**Comentário:**

RQ4 — Task 1(a), ResNet-50, k=70%: acurácia global 84,63%; MCC 0,7715. Resultado agregado de cinco doenças, não de hanseníase isolada.

## 12. Resultado global da VGG-16

**Página 6**

**Trecho grifado:**

> 82.22%

**Comentário:**

RQ4 — Task 1(a), VGG-16, k=70%: acurácia global 82,22%; MCC 0,7336. Diferença observada não acompanhada de teste de significância.

## 13. Acurácia global na Task 2

**Página 6**

**Trecho grifado:**

> 77% accuracy,

**Comentário:**

RQ3/RQ4 — Task 2: acurácia global 77% (a) e 80% (b). Para hanseníase, consultar a diagonal da Figura 1: 12% e 13%. Não misturar Task 1 e Task 2.

## 14. Desempenho específico para hanseníase

**Página 7**

**Trecho grifado:**

> Fig 1. Task 2: Confusion matrices

**Comentário:**

RQ4 — LEITURA CRÍTICA: linha Leprosy, coluna Leprosy = 12,0% em (a) e 13,0% em (b). Como as linhas representam a classe real, interpretam-se como recall por classe. 66% e 64% das imagens de hanseníase foram classificadas como escabiose. Valores lidos da figura; não são acurácia global.

## 15. Generalização e PCA

**Página 8**

**Trecho grifado:**

> generalization ability to test images becomes poorer,

**Comentário:**

RQ7 — PCA evidencia qualitativamente menor separação das classes no teste. Não há teste externo nem gap quantitativo entre países ou tons de pele.

## 16. Limitações para hanseníase

**Página 9**

**Trecho grifado:**

> Leprosy

**Comentário:**

RQ3/RQ7 — Hanseníase: amostra pequena e apresentações heterogêneas. Autores relatam formas tuberculoide, borderline e lepromatosa, deformidades e feridas por neuropatia. Estratificação não produziu resultados significativos/interpretáveis devido à escassez de dados.

## 17. Combinação com dados clínicos

**Página 9**

**Trecho grifado:**

> loss of sensation

**Comentário:**

RQ1/RQ6 — Dados clínicos, especialmente perda de sensibilidade, são sugeridos na discussão. Não foram integrados experimentalmente ao classificador deste estudo.

## 18. Desbalanceamento e equidade

**Página 9**

**Trecho grifado:**

> Fairness issues

**Comentário:**

RQ5 — Discussão de desbalanceamento entre doenças; não representa medição de equidade por fototipo nem demonstração de disparidade racial.

## 19. Heterogeneidade das imagens

**Página 10**

**Trecho grifado:**

> lighting.

**Comentário:**

RQ3/RQ7 — Limitações: iluminação, fundos e condições de coleta heterogêneas. Possíveis fontes de erro são discutidas; não há experimento isolando cada causa.

## 20. Aplicação clínica proposta

**Página 10**

**Trecho grifado:**

> AI is not yet a replacement

**Comentário:**

RQ7 — Potencial de apoio à triagem é uma conclusão/proposta. Não foi demonstrado benefício clínico prospectivo nem prontidão para implantação.

## 21. Disponibilidade dos dados

**Página 1**

**Trecho grifado:**

> not publicly

**Comentário:**

RQ2 — Dados não são públicos por privacidade. O artigo informa acesso mediante contato institucional. Não considerar o dataset aberto.
