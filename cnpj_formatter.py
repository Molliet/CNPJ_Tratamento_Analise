import os
import pandas as pd




#Função para formatar dados originais de empresas do portal de dados abertos
def clean_empresa(file_path, file_name, num_y):
    df_empresa =None
    try:
        #Função carrega o arquivo em um dataframe para  melhor manipulçao
        print(f"Carregando {file_name}...")
        df_empresa = pd.read_csv(file_path, sep=";", dtype=str, encoding='latin1')
        
        #Devido formatação do portal foi necesario para melhor visualização
        colunas_empresa = [
        "CNPJ", 
        "Nome Empresarial", 
        "Natureza Jurídica", 
        "Código Qualificação", 
        "Capital Social", 
        "Porte", 
        "Observações"
        ]
        
        #Serie de ajustes para obter apena dados  de interesse
        print("Editando arquivo...")
        
        df_empresa.columns = colunas_empresa
        df_empresa = df_empresa.drop(columns="Observações")
        
        #Transformando Capital Social para float em caso de uso para calculos        
        df_empresa["Capital Social"] = (
        df_empresa["Capital Social"]
        .astype(str)
        .str.replace(",", ".", regex=True)
        .fillna("0")  
        .astype(float))
        
        #Formatando nome com ; para evitar problemas com o separador do CSV
        df_empresa["Nome Empresarial"] = (
            df_empresa["Nome Empresarial"]
            .astype(str)
            .str.replace(";",".", regex=True)
        )

        #Salva o arquivo com um nome mais simples e o numero de acordo com o nome do arquivo original de forma dinamica
        print("Salvando arquivo...")
        df_empresa.to_csv(f"csv_clean/empresa_p{num_y}.csv", index=False, sep=";", encoding='latin1')
    
    #Levanta Exception  em caso de erros
    except Exception as e:
        print(f"Erro ao processar {file_name}: {e}")   

    #Finally justifica declaração inicial do dt=None
    finally:
        print("Liberando epaço...")
        del df_empresa


#Função para formatar dados originais de estabelecimentos do portal de dados abertos
def clean_estabelecimento(file_path, file_name,  num_y):
    
    df_estabele =None
   
    try:
        print(f"Carregando {file_name}...")
        df_estabele = pd.read_csv(file_path, sep=";", dtype=str, encoding='latin1')
        colunas_estabele = [
        "CNPJ", 
        "Ordem", 
        "DV", 
        "M/F", 
        "Fantasia", 
        "Situação Cadastral", 
        "Data SC", 
        "Motivo SC", 
        "Nome cidade ex", 
        "Pais",
        "Data Início",
        "CNAE P",
        "CNAE S",
        "Tipo Logradouro",
        "Logradouro",
        "Número",
        "Complemento",
        "Bairro",
        "CEP",
        "UF",
        "Município",
        "DDD1",
        "Telefone1",
        "DDD2",
        "Telefone2",
        "DDD FAX",
        "FAX",
        "Correio Eletronico",
        "Situação Especial",
        "Data SE"
        ]
        
        
        
        print("Editando arquivo...")
        df_estabele.columns = colunas_estabele
        
        df_estabele["Endereço"] = df_estabele[["Tipo Logradouro", "Logradouro", "Número", "Complemento", "Bairro", "CEP"]].astype(str).agg(" ".join, axis=1)
        df_estabele = df_estabele.drop(columns=["Nome cidade ex", "Pais", "Tipo Logradouro", "Logradouro", "Número","Complemento","Bairro","CEP","DDD2", "Telefone2", "DDD FAX", "FAX","Situação Especial","Data SE"])
        df_estabele["Fantasia"] = df_estabele["Fantasia"].fillna("Sem nome")
        
        df_estabele["Fantasia"] = (
            df_estabele["Fantasia"]
            .astype(str)
            .str.replace(";",".", regex=True)
        )
        
        
        
        print("Salvando arquivo...")
        df_estabele.to_csv(f"csv_clean/estabelecimento_p{num_y}.csv", index=False, sep=";", encoding="latin1'")
        


    except Exception as e:  
        print(f"Erro ao processar {file_name}: {e}")
    finally:
        print("Liberando epaço...")
        del df_estabele  


    
def clean_socio(file_path, file_name,  num_y):
    
    df_sociocsv = None
    
    try:
        print(f"Carregando {file_name}...")
        df_sociocsv = pd.read_csv(file_path, sep=";", dtype=str, encoding='latin1')
        
        colunas_sociocsv = [
        "CNPJ",
        "ID Sócio",
        "Nome",
        "CPF",
        "Qualificação",
        "Data Entrada",
        "Pais",
        "Representante Legal",
        "Nome Representante",
        "Qualificação Rep",
        "Faixa Etária"
        ]
        
        
        
        print("Editando arquivo...")    
        df_sociocsv.columns = colunas_sociocsv
        
        df_sociocsv = df_sociocsv.drop(columns=["Pais", "Representante Legal", "Nome Representante", "Qualificação Rep"])
        
        
        
        print("Salvando arquivo...")
        df_sociocsv.to_csv(f"csv_clean/socio_p{num_y}.csv", index=False, sep=";", encoding="latin1'")
        
        
        
    except Exception as e:
        print(f"Erro ao processar {file_name}: {e}")
   
    finally:
        print("Liberando epaço...")
        del df_sociocsv
    


def format_csv_clean():
    DATA_DIR = "CSV"  


    if not os.path.exists(DATA_DIR):
        print(f"A pasta '{DATA_DIR}' não foi encontrada.")
        return

    #Roda todos os arquivos do  diretorio  indicado em busca dos arquivos e define sua formatação
    for file_name in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, file_name)
        
        parts = file_name.split(".")
        data_type = parts[-1]              
        num_y = parts[1].split("Y")[-1] 
        
        if data_type == "EMPRECSV":
            clean_empresa(file_path, file_name,  num_y)
            
        elif data_type == "ESTABELE":
            clean_estabelecimento(file_path, file_name,  num_y)
            
        elif data_type == "SOCIOCSV":
            clean_socio(file_path, file_name,  num_y)


format_csv_clean()