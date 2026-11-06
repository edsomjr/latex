---
tags: []
parent: 'Unveiling leprosy through machines: a review of artificial intelligence in a neglected tropical disease'
collections:
    - TCC_Leituras
$version: 419
$libraryID: 2
$itemKey: 452JPAJA

---
# Extração de dados — Unveiling leprosy through machines: a review of artificial intelligence in a neglected tropical disease

Revisão Evidentia 312 · TCC\_Leituras

**1. Título:** Unveiling leprosy through machines: a review of artificial intelligence in a neglected tropical disease

**2. Autores:** Aniket Goswami; Shikha Verma; Anita Marak

**3. Ano de publicação:** 2026

**4. Fonte de publicação:** Portuguese Journal of Dermatology and Venereology, 84(1):11–18. DOI: 10.24875/PJDV.25000080.

**5. Tipo de estudo:** Artigo de revisão narrativa e crítica: sintetiza estudos primários e revisões anteriores sobre diagnóstico, classificação, monitoramento e vigilância. Não apresenta busca/seleção sistemática, metanálise ou experimento próprio.

**6. Tipo de veículo de publicação:** Artigo de revisão em periódico.

**7. RQ1 Técnica de visão computacional utilizada:** Reconhecimento de padrões de forma, borda, cor e textura em imagens clínicas por CNNs; combinação de fotografias e metadados, few-shot learning e mapas de ativação Grad-CAM para explicabilidade. Dermatoscopia é discutida como possibilidade; a CNN híbrida com 96,1% citada para outras dermatoses não é resultado de diagnóstico de hanseníase.

**8. RQ2 Dataset utilizado:** Sem base própria. Nos estudos citados: AI4Leprosy (1.229 imagens + 585 entradas de metadados), Beesetty (368 imagens segundo a revisão), LeprosyNet (base própria do estudo primário, sem n na Tabela 1); em tarefas não visuais, registros brasileiros do SINAN e questionário LSQ. As revisões prévias de 21 e 30 estudos não são contagens de imagens.

**9. RQ2 Características da população / Doença ou manifestação dermatológica:** Estudos de hanseníase com lesões visíveis: manchas, placas, máculas, pápulas e nódulos, em geral em condições padronizadas ou repositórios. Alguns incorporam perda de sensibilidade e sintomas. Entre cinco fontes-chave analisadas, os autores não identificaram inclusão de reações tipo 1/2 ou hanseníase neural nos dados de treino. Não há coorte própria.

**10. RQ2 Quantidade de imagens:** Não informado ou não aplicável como total único. Deixar o campo inteiro vazio; ver dataset e população.

**11. RQ3 Avaliação de desempenho dos modelos:** Resultados secundários (sem estimativa agrupada): AI4Leprosy ≈90% de acurácia (Tabela 1) e AUC 96,46% (texto); few-shot CNN ≈73% de acurácia; LeprosyNet 98%. Em tarefas não visuais: classificação PB/MB com registros SINAN 94% de sensibilidade e 87% de especificidade; triagem por questionário/SVM 85,7% e 69,2%, respectivamente. Os resultados são de estudos e tarefas diferentes, sem comparação controlada.

**12. RQ4 Métricas utilizadas:** Acurácia, área sob a curva (AUC), sensibilidade e especificidade reportadas em estudos citados; sem métrica calculada pelos autores da revisão.

**13. RQ5 Informações sobre tom de pele:** Aponta variação de tom de pele em campo e risco de viés de bases geograficamente restritas. Não informa distribuição de fototipos, escala ou medida de pigmentação para uma amostra própria.

**14. RQ6 Comparação do desempenho entre tons de pele:** Não apresenta desempenho estratificado por tom de pele; menção a viés e variabilidade não constitui comparação.

**15. RQ7 Modelo ou Abordagem:** AI4Leprosy (CNN + regressão logística), CNN com aprendizado por poucos exemplos e LeprosyNet (CNN explicável/Grad-CAM). Cita também SVM, árvores, random forest e regressão logística com registros/questionários. Integração multimodal e treinamento federado são direções futuras, não modelos implementados na revisão.

**16. RQ8 Avaliação de generalização do modelo:** Não há teste externo conduzido pela revisão. Indica escassez de validação independente e discrepância entre bases selecionadas e campo, por diferenças de iluminação, câmera, tom de pele e geografia; recomenda estudos representativos.

**17. Método de validação:** Não aplicável para a revisão; sem hold-out/k-fold ou validação própria e sem protocolo único harmonizado para os estudos citados.

**18. Limitações e conclusões:** Bases pequenas, locais e heterogêneas, validade externa insuficiente, explicabilidade desigual e dúvidas sobre consentimento, privacidade e responsabilidade. Conclui que IA pode apoiar o reconhecimento e a classificação, mas precisa de avaliação em campo e supervisão clínica; sugere aprendizado federado e integração multimodal.

## Trechos grifados e comentários

**[p. 1](zotero://open-pdf/library/items/BF39V23G?page=1\&annotation=AQLXA26X)** — “REVIEW ARTICLE”\
Tipo de estudo: revisão narrativa em periódico (2026); os resultados quantitativos provêm dos trabalhos citados.

**[p. 7](zotero://open-pdf/library/items/BF39V23G?page=7\&annotation=M6QKHUSU)** — “This study does not involve personal patient data, medical records, or biological samples”\
RQ2: sem amostra, base ou total de imagens próprio; não somar as amostras dos trabalhos revisados.

**[p. 3](zotero://open-pdf/library/items/BF39V23G?page=3\&annotation=ZHQHIANM)** — “curated datasets of visible skin lesions, including patches, plaques, macules, papules, and nodules”\
População/manifestações: fontes-chave se concentram em lesões visíveis; o texto registra ausência de treinamento sobre reações hansênicas e hanseníase neural nas cinco fontes examinadas.

**[p. 3](zotero://open-pdf/library/items/BF39V23G?page=3\&annotation=FKWCNAD8)** — “the AI4Leprosy system, combining clinical photographs with metadata”\
RQ1/RQ7: AI4Leprosy combina fotografias e metadados. A Tabela 1 cita 1.229 imagens, 585 entradas de metadados, CNN e regressão logística. Acurácia \~90%; AUC 96,46%.

**[p. 3](zotero://open-pdf/library/items/BF39V23G?page=3\&annotation=8XA5MHMD)** — “few-shot learning on only 368 images”\
RQ2/RQ3: a revisão atribui ao método de Beesetty 368 imagens e cerca de 73% de acurácia. Não é experimento próprio.

**[p. 3](zotero://open-pdf/library/items/BF39V23G?page=3\&annotation=6N5F6MF3)** — “not only reached 98% accuracy but also opened the”\
RQ3/RQ7: LeprosyNet é a CNN explicável de Baweja com mapas Grad-CAM; 98% de acurácia conforme a revisão.

**[p. 4](zotero://open-pdf/library/items/BF39V23G?page=4\&annotation=YPJV7GXG)** — “model achieved 94% sensitivity and 87% specificity”\
RQ3/RQ4: classificação PB/MB por dados do SINAN, sem imagens. Não confundir com acurácia de detecção visual de hanseníase.

**[p. 6](zotero://open-pdf/library/items/BF39V23G?page=6\&annotation=FXWZ4UCH)** — “where lighting, camera quality, and skin tone vary widely.”\
RQ5/RQ6/RQ8: variações na iluminação, câmera e tom de pele são apontadas como possíveis fontes de erro; não há métricas por fototipo ou teste externo próprio.

**[p. 6](zotero://open-pdf/library/items/BF39V23G?page=6\&annotation=JIRDMY88)** — “Existing models are based on small pilot studies, use different input datasets, and lack sufficient validation for routine use.”\
Limitação: evidência em pilotos e populações restritas; faltam validação externa e bases mais representativas.
