
# Análise e Tratamento de Dados de CNPJ

Projeto de leitura, tratamento e análise de dados de CNPJs utilizando Python.

---

## Descrição
Este projeto oferece uma solução prática e elegante para tratamento e análise de grandes volumes de dados de CNPJs disponibilizados pelo portal de dados abertos do governo. O sistema permite processar informações detalhadas de empresas, estabelecimentos e sócios, realizando limpeza, padronização e estruturação para facilitar análises profundas e visualizações impactantes.

A análise é complementada por gráficos interativos gerados com Plotly, proporcionando insights rápidos e atraentes, além de uma visualização dinâmica da rede de relações entre sócios e empresas utilizando NetworkX, explorando conexões em múltiplas camadas a partir de um CNPJ inicial.

---

## Funcionalidades
- **Padronização automática dos dados**
- **Conversão inteligente de valores**
- **Tratamento eficaz de caracteres especiais**
- **Agrupamento estruturado de informações**
- **Exportação simples e rápida dos dados limpos**
- **Gráficos interativos e elegantes**
- **Visualização de redes de relacionamento entre sócios e empresas por camadas**

---

## Como utilizar

### 1. Download dos dados
Baixe os arquivos de dados atualizados diretamente no [Portal de Dados Abertos da Receita Federal](https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/).

*Nota: Utilizei os dados mais recentes disponíveis (2025-02).*

### 2. Formatação dos dados
Execute o script `cnpj_formatter.py` para limpar e estruturar os arquivos baixados. Certifique-se de criar as pastas:
- `CSV_RAW` (para arquivos originais)
- `CSV_CLEAN` (para os arquivos processados)

O script cuidará automaticamente do restante, porque ninguém merece fazer isso à mão.

### 3. Montagem do Banco de Dados SQLite
Rode o arquivo `mount_db.py`. Ele criará um banco de dados local, organizado em três tabelas correspondentes aos tipos de arquivos disponibilizados pela Receita Federal. Simples e prático, quase mágica.

### 4. Análise Exploratória
Abra e execute o notebook `readings_db_graphs.ipynb`. Este notebook contém diversos exemplos de consultas SQL úteis, além de gráficos interativos e a construção dinâmica das redes de relacionamento entre empresas e sócios.

---

## Exemplos de Análise

### Distribuição de Estabelecimentos Ativos por Estado:

![image](https://github.com/user-attachments/assets/0532af9a-cc06-4fc2-81aa-9bcee41e1ac3)

Gráfico simples com Matplotlib para identificação inicial das regiões mais ativas economicamente. Um bom começo antes de mergulhar em análises mais detalhadas.

### TOP 10 CNAEs nos 7 Estados com mais Estabelecimentos:

![image](https://github.com/user-attachments/assets/8fb9f20c-a4d8-474e-a861-d3132a5b2420)

![image](https://github.com/user-attachments/assets/45cbdc88-4ca3-4d07-a1ad-a92c74ff99c8)

![image](https://github.com/user-attachments/assets/6980ddd6-72da-4e40-a977-dfab9537dec1)

Após determinar os estados líderes em número de estabelecimentos, foi possível realizar uma análise detalhada dos setores econômicos predominantes (CNAEs). Os gráficos interativos com Plotly permitem uma exploração intuitiva e visualmente agradável dos dados.

### Redes de Relacionamento em Camadas:

A visualização em camadas permite explorar progressivamente as conexões indiretas entre empresas e sócios, facilitando a descoberta de vínculos e padrões que seriam difíceis de perceber em uma análise superficial.

**Camada 1 – Relações diretas**
![image](https://github.com/user-attachments/assets/256b160d-ffcf-4989-bb94-baf1beff6688)

**Camada 2 – Relações indiretas (um nível de distância)**
![image](https://github.com/user-attachments/assets/74d53336-2474-413a-9ad5-59feeaaa8a1b)

**Camada 3 – Relações expandidas (dois níveis de distância)**
![image](https://github.com/user-attachments/assets/5ed9ad50-6e13-42c0-848a-3f4c694cd3bd)

Explore as redes sociais empresariais com profundidade e veja quem está mais conectado do que influencer em festa de lançamento.

---

## Melhorias Futuras
- **Otimização de desempenho para grandes volumes de dados**
- **Integração com outras bases governamentais para cruzamento de informações**
- **Interface web para facilitar a interação com usuários menos técnicos**
- **Automatização de atualizações periódicas dos dados**
- **Análises preditivas utilizando Machine Learning**

**Agora, mãos à obra e bons insights!** 🚀📊
