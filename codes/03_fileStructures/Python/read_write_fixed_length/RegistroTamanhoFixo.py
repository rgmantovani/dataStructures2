# -----------------------------------------------------------------------------------
# Função: Remove caractere do arquivo
# Params: 
#         - registro: registro a ser limpo
# -----------------------------------------------------------------------------------
 
def limpaString(registro):
    registro = registro.replace("`", "'")
    registro = registro.replace("’", "'")
    registro = registro.replace("ü", "u")
    registro = registro.replace("í", "i")
    registro = registro.replace("Ô", "O")
    registro = registro.replace("á", "a")
    return(registro)
    
# -----------------------------------------------------------------------------------
# Função: Escrita de registros de tamanho fixo com campos variados (|)
# Params: 
#         - registrosAnime: lista com os registros de anime lidos na memória
#         - arquivoSaida: arquivo de saída com os registros gravados no padrão
#         - debugging: flag para mostrar ou não os passos intermediários da lógica
# -----------------------------------------------------------------------------------

def EscritaRegistrosFixosCamposVariados(registrosAnimes, arquivoSaida = "output.txt", 
    debugging = False):

    if(debugging):
        print(registrosAnimes[0]) 

    # descobrindo o tamanho do maior registro contido no arquivo
    maiorTamanho = len(max(registrosAnimes, key=len))
    if(debugging):
        print(maiorTamanho)

    with open(arquivoSaida, mode="w") as file:
        
        for registro in registrosAnimes:
            
            # substituindo virgula (,) por pipe (|)
            novoRegistro = registro.replace(",", "|")
            novoRegistro = novoRegistro.replace("\n", "")
            novoRegistro = limpaString(registro=novoRegistro)
            
            # adicionando explicitamente espaços não usados (caracter *)
            diff = maiorTamanho - len(novoRegistro)
            aux = "*" * diff
            novoRegistro = novoRegistro + aux + "\n"
         
            if(debugging):
                print(novoRegistro)
            # gravando os registros no arquivo de saída padronizado            
            file.write(novoRegistro)

# -----------------------------------------------------------------------------------
# Função: Leitura de registros de tamanho fixo com campos variados (|)
# Params: 
#         - arquivoDados: arquivo de dados com os registros gravados no padrão
#         - tamanhoRegistro: tamanho dos registros de tamanho fixo
#         - RRN: relative record number, indice do registro que será lido
#         - debugging: flag para mostrar ou não os passos intermediários da lógica
# Retornos:
#         - registro: registro lido com todos os campos disponíveis
# -----------------------------------------------------------------------------------

def LeituraRegistrosFixosCamposVariados(arquivoDados, tamanhoRegistro, RRN):
    
        offset = RRN * tamanhoRegistro
        arquivoDados.seek(offset)
        registro = arquivoDados.readline()
        return(registro)

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------