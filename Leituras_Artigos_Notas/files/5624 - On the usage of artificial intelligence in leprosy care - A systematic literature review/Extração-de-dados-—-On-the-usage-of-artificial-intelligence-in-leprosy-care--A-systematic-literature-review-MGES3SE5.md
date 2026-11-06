---
tags: []
parent: 'On the usage of artificial intelligence in leprosy care: A systematic literature review'
collections:
    - TCC_Leituras
$version: 409
$libraryID: 2
$itemKey: MGES3SE5

---
# Extração de dados — On the usage of artificial intelligence in leprosy care: A systematic literature review

Revisão Evidentia 312 · TCC\_Leituras

**1. Título:** On the usage of artificial intelligence in leprosy care: A systematic literature review

**2. Autores:** Hilson Gomes Vilar de Andrade; Elisson da Silva Rocha; Kayo H. de Carvalho Monteiro; Cleber Matos de Morais; Danielle Christine Moura dos Santos; Dimas Cassimiro Nascimento; Raphael A. Dourado; Theo Lynn; Patricia Takako Endo

**3. Ano de publicação:** 2025

**4. Fonte de publicação:** PLOS Computational Biology

**5. Tipo de estudo:** Revisão sistemática da literatura com fluxograma PRISMA e avaliação de qualidade. Busca automática, manual e em citações; síntese descritiva de estudos primários, sem treinamento próprio ou metanálise.

**6. Tipo de veículo de publicação:** Artigo de periódico.

**7. RQ1 Técnica de visão computacional utilizada:** Nos trabalhos revisados predominam classificação de lesões em fotografias por redes neurais/CNN e SVM. Técnicas descritas incluem segmentação, normalização de iluminação, descritores texturais/contornos (por exemplo, WLD invariante a rotação), transferência de aprendizado e few-shot. A revisão não implementa uma técnica própria.

**8. RQ2 Dataset utilizado:** 30 estudos selecionados de 657 registros iniciais em ACM Digital Library, IEEE Xplore, PubMed, Scopus, ScienceDirect e Springer; busca complementar. Bases dos estudos incluem AI4leprosy, DermNet NZ, ISIC, Atlas Dermatológico, IEEE DataPort, SINAN e UniProt, além de bases clínicas privadas.

**9. RQ2 Características da população / Doença ou manifestação dermatológica:** Unidade da revisão: estudo. Inclui hanseníase/diagnósticos diferenciais, sinais cutâneos, contatos, vigilância, tratamento e epidemiologia. Há imagens de pacientes de hospitais em países endêmicos da África/Ásia, repositórios públicos e estudos com dados tabulares. Sem coorte própria ou total harmonizado de pacientes/imagens.

**10. RQ2 Quantidade de imagens:** Não informado ou não aplicável como total único. Deixar o campo inteiro vazio; ver dataset e população.

**11. RQ3 Avaliação de desempenho dos modelos:** Resultados secundários na Tabela 4, sem estimativa combinada: acurácia multiclasse de 73,12% a 97,1% para tarefas heterogêneas (o extremo superior é de dados tabulares/proteicos, não fotografia clínica). Ex.: Steyve 96%, Banerjee 91,38%, Beesetty 73,12%; binário de Baweja 98%, com tamanho da base não especificado. Não atribuir esses valores a um classificador treinado pela revisão nem comparar diretamente.

**12. RQ4 Métricas utilizadas:** Acurácia (22 trabalhos), sensibilidade/recall, especificidade, F1, precisão, ROC/AUC, MCC, Brier score e MSE; para agrupamento/seleção de atributos também análise de centroides e similaridade MS. Dois estudos não descrevem métricas.

**13. RQ5 Informações sobre tom de pele:** Não apresenta escala de tons de pele, fototipos ou distribuição harmonizada; procedência geográfica e diversidade de bases não equivalem a fototipo.

**14. RQ6 Comparação do desempenho entre tons de pele:** Não compara desempenho entre grupos de tom de pele.

**15. RQ7 Modelo ou Abordagem:** Famílias de IA sintetizadas: redes neurais, CNN (inclusive ResNet-50, Inception e modelos pré-treinados), SVM, árvores de decisão, random forest e outros classificadores. Há também abordagens de agrupamento, seleção de atributos e dados multimodais. Sem novo modelo da revisão.

**16. RQ8 Avaliação de generalização do modelo:** Sem teste externo próprio. Tabela 4 identifica necessidade de validação em outras regiões/contextos e dados diversos; bases pequenas, locais, não compartilhadas ou mal descritas e pré-processamentos distintos limitam transferibilidade e comparações.

**17. Método de validação:** Validação de modelo não aplicável à revisão. Triagem dos trabalhos por dois avaliadores independentes, terceiro para arbitragem, com critérios de qualidade. Não há protocolo único de validação preditiva nem reavaliação das bases primárias.

**18. Limitações e conclusões:** Predomínio de classificação de sinais e diagnóstico (16+7 trabalhos); vigilância 3, epidemiologia 2, tratamento 2. Autores apontam escassez de dados diversos/compartilhados, documentação e código, estudos pequenos e necessidade de métricas para desbalanceamento e de pesquisa sobre seguimento e adoção clínica.

## Trechos grifados e comentários

**[p. 1](zotero://open-pdf/library/items/PDHX32MC?page=1\&annotation=KAQFWZYV)** — “This systematic literature review (SLR) examines the state of the art”\
Tipo de estudo — Revisão sistemática sobre usos da IA no cuidado à hanseníase; não desenvolve um classificador.

**[p. 1](zotero://open-pdf/library/items/PDHX32MC?page=1\&annotation=CDSKA8H5)** — “From an initial 657 works from six scientific databases”\
RQ2 — Busca inicial de 657 registros em seis bases, resultando em 30 estudos incluídos; contagens de artigos, não de imagens.

**[p. 6](zotero://open-pdf/library/items/PDHX32MC?page=6\&annotation=ES5LMPI3)** — “Conflicts in inclusion/exclusion decisions were arbitrated by a third author.”\
Método — Dois revisores fizeram a triagem e um terceiro arbitrou discordâncias. Trata-se do método da revisão, não de validação de modelo.

**[p. 11](zotero://open-pdf/library/items/PDHX32MC?page=11\&annotation=IXB7C6R2)** — “The majority of the thirty included works (n=16) utilized skin lesion images as input data”\
RQ1/RQ2 — Fotografias de lesões cutâneas são o tipo de entrada mais comum (16 estudos). A revisão também inclui dados tabulares e híbridos; não há uma única população ou total de imagens.

**[p. 12](zotero://open-pdf/library/items/PDHX32MC?page=12\&annotation=4HLBE493)** — “summarizes all public datasets found in this SLR”\
RQ2 — Tabela 2: AI4leprosy, Atlas, ISIC, DermNet NZ, IEEE DataPort, SINAN e UniProt. As últimas incluem dados não fotográficos; não somar registros como total de imagens.

**[p. 19](zotero://open-pdf/library/items/PDHX32MC?page=19\&annotation=GSH4JNTB)** — “texture and edge information in a rotation-invariant manner”\
RQ1/RQ7 — Exemplo de técnica de estudo primário: descritor WLD invariante à rotação com SVM. As principais famílias da revisão são redes neurais, CNNs e SVMs.

**[p. 22](zotero://open-pdf/library/items/PDHX32MC?page=22\&annotation=WCJTDVHZ)** — “eleven metrics were used to evaluate the performance”\
RQ4 — Foram reunidas 11 categorias de métricas, de classificação, agrupamento ou seleção; duas publicações não informam as métricas dos modelos.

**[p. 25](zotero://open-pdf/library/items/PDHX32MC?page=25\&annotation=ULDCD96U)** — “with results ranging from 73.12%”\
RQ3 — Acurácias multiclasse de 73,12% a 97,1% resumem tarefas distintas; o estudo do extremo superior utiliza dados de proteínas, não lesões fotográficas. Sem metanálise.

**[p. 26](zotero://open-pdf/library/items/PDHX32MC?page=26\&annotation=HP9XH9NM)** — “Needs validation across different clinical contexts”\
RQ8 — Tabela 4 registra necessidade de validação em outros contextos; a revisão não testa um modelo externamente. Não há resultados estratificados por tom de pele.

**[p. 28](zotero://open-pdf/library/items/PDHX32MC?page=28\&annotation=5PG9SRWA)** — “This demands greater coordination and sharing of datasets”\
Limitações — Autores pedem compartilhamento de bases e maior detalhamento da configuração, seleção de atributos e métricas.
