import os
import sqlite3
import pandas as pd


conn = sqlite3.connect("cnpj_data.db")
cursor = conn.cursor()


MAPA_TABELAS = {
    "empresas": "empresa",
    "estabelecimentos": "estabelecimento",
    "socios": "socio"
}


TABELAS_SQL = {
    "empresas": """
        CREATE TABLE IF NOT EXISTS empresas (
            CNPJ TEXT PRIMARY KEY,
            Nome_Empresarial TEXT,
            Natureza_Juridica TEXT,
            Codigo_Qualificacao TEXT,
            Capital_Social REAL,
            Porte TEXT
        );
    """,
    "estabelecimentos": """
        CREATE TABLE IF NOT EXISTS estabelecimentos (
            CNPJ TEXT,
            Ordem TEXT,
            DV TEXT,
            Matriz_Filial TEXT,
            Fantasia TEXT,
            Situacao_Cadastral TEXT,
            Data_SC TEXT,
            Motivo_SC TEXT,
            Data_inicio TEXT,
            CNAE_P TEXT,
            CNAE_S TEXT,
            UF TEXT,
            Municipio TEXT,
            DDD TEXT,
            Telefone TEXT,
            Email TEXT,
            Endereco TEXT,
            FOREIGN KEY (CNPJ) REFERENCES empresas(CNPJ)
        );
    """,
    "socios": """
        CREATE TABLE IF NOT EXISTS socios (
            CNPJ TEXT,
            ID_Socio TEXT,
            Nome TEXT,
            CPF_CNPJ TEXT,
            Qualificacao TEXT,
            Data_Entrada TEXT,
            Faixa_Etaria TEXT,
            FOREIGN KEY (CNPJ) REFERENCES empresas(CNPJ)
        );
    """
}


for tabela, sql in TABELAS_SQL.items():
    cursor.execute(sql)


PASTA_CSV = "csv_clean/"


def carregar_arquivos(tabela, prefixo):
    arquivos_carregados = 0

    for arquivo in os.listdir(PASTA_CSV):
        if arquivo.startswith(prefixo) and arquivo.endswith(".csv"):
            caminho_arquivo = os.path.join(PASTA_CSV, arquivo)
            print(f"arregando {caminho_arquivo} para {tabela}...")

            try:
                df = pd.read_csv(caminho_arquivo, sep=";", dtype=str, encoding='latin1', on_bad_lines='skip')
                df.columns = [col.strip().replace("/", "_") for col in df.columns]
                df.to_sql(tabela, conn, if_exists="append", index=False)
                arquivos_carregados += 1
                print(f"- {arquivo} carregado com sucesso!")
            except Exception as e:
                print(f"Erro ao carregar {arquivo}: {e}")

    if arquivos_carregados == 0:
        print(f"Nenhum arquivo correspondente ao prefixo '{prefixo}' encontrado!")


for tabela, prefixo in MAPA_TABELAS.items():
    carregar_arquivos(tabela, prefixo)

print("Todos os arquivos disponíveis foram carregados com sucesso no SQLite!")


cursor.execute("CREATE INDEX IF NOT EXISTS idx_cnpj_empresas ON empresas (CNPJ);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_cnpj_estabelecimentos ON estabelecimentos (CNPJ);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_cnpj_socios ON socios (CNPJ);")


conn.commit()
conn.close()

print("Banco de dados atualizado com sucesso e índices criados!")