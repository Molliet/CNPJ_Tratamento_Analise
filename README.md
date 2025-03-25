# CNPJ Tratamento e Analise

Projeto de leitura, tratamento e análise de dados com Python


## Descrição
Este projeto tem como objetivo o tratamento e análise de dados de CNPJs obtidos a partir do portal de dados abertos do governo. Ele processa arquivos de empresas, estabelecimentos e sócios, realizando a limpeza e estruturação dos dados para facilitar a análise posterior. Já a análise consiste em uma leitura dos dados, com gráficos de interativos com plotly e navegação pela network de relações sócio-empresa utilizando networkx para criar uma mapa em camadas a partir do cnpj inicial.


## Funcionalidades
- **Padronização dos dados**
- **Conversão de valores**
- **Tratamento de caracteres especiais**
- **Agrupamento de informações**
- **Exportação de dados limpos**
- **Visualização de Gráficos interativos**
- **Visualização de network entre sócios e empresas em camadas**


## Utilização

### Baixe os registros de de CNPJ na página: https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/
Em meu caso, utilizei os registros de 2025-02 para uma leitura atualizada

### Utilize o cnpj_formatter.py para formatar os dados:
Para utilizar o arquivo é necessário que tenha uma pasta CSV_RAW e CSV_CLEAN no diretório, o programa irá procurar pelas pastas ao fazer a formatação

### Utilize o mount_db.py para montar o banco de dados local com SQLite
Com os arquivos formatados corretamente pelo cnpj_formatter, o arquivo irá montar o banco de dados com 3 tabelas referentes aos tipos de arquivos fornecidos pela receita federal

### Utilize o readings_db_graphs.ipynb para realizar leituras do banco de dados com queries
O arquivo contém diversas leituras do banco de dados como exemplos além da construção de networks entre empresas e sócios


## Leituras

### Distribuição de Estabelecimentos Ativos por Estado:

![image](https://github.com/user-attachments/assets/0532af9a-cc06-4fc2-81aa-9bcee41e1ac3)

Iniciei as leituras utilizando Matplotlib para gerar um gráfico simples para ter uma noção de atividade no Brasil, através de queries pesquisando apenas pelos estabelecimentos ativos nos estados foi possivel identificar em ordem decrescente os núcleos de estabelecimentos para focar as próximas leituras.

### Distribuição de TOP 10 CNAE nos TOP 7 estados com mais estabelecimentos:

![image](https://github.com/user-attachments/assets/8fb9f20c-a4d8-474e-a861-d3132a5b2420)

![image](https://github.com/user-attachments/assets/45cbdc88-4ca3-4d07-a1ad-a92c74ff99c8)

![image](https://github.com/user-attachments/assets/6980ddd6-72da-4e40-a977-dfab9537dec1)

Após identificar os TOP 7 estados com mais estabelecimentos, iniciei a pesquisa dos TOP 10 CNAE mais frequentes por estado para poder entender melhor a distribuição de serviçoes oferecidos por estado e ainda sendo possível observar a diferença de quantidade de estabelecimentos. Para criar esse gráfico, optei por utilizar o plotly para gráficos interativos e mais estilosos, em que posso selecionar os CNAES que desejo ver a vontade.


### Rede de relações em camadas:

#### Relações nível 1
![image](https://github.com/user-attachments/assets/256b160d-ffcf-4989-bb94-baf1beff6688)

#### Relações nível 2
![image](https://github.com/user-attachments/assets/74d53336-2474-413a-9ad5-59feeaaa8a1b)

#### Relações nível 3
![image](https://github.com/user-attachments/assets/5ed9ad50-6e13-42c0-848a-3f4c694cd3bd)



