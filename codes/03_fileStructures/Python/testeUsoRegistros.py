# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

import os
import re

# -----------------------------------------------------------------------------------
# Função: remove registros (invalidar) por chave de consulta
# Params: 
#         - registroAnime: lista com os registros de anime lidos na memória
#         - chave: valor de consulta do registro que se deseja remover (chave canônica)
# -----------------------------------------------------------------------------------
def removeRegistroPorChave(registrosAnime, chave):
    pass

# -----------------------------------------------------------------------------------
# Função: remove registros (invalidar) por id (RRN)
# Params: 
#         - registrosAnime: lista com os registros de anime lidos na memória
#         - id: RRN do registro que será invalidado/removido
# -----------------------------------------------------------------------------------

def removeRegistrosPorRRN(registrosAnime, id):
   
    if(id >= len(registrosAnime)):
        print("Warning: indice invalido!")
    else:
        registro = registrosAnime[id]
        registro = "*|" + registro[2:]
        registrosAnime[id] = registro

# -----------------------------------------------------------------------------------
# Função: gera novo arquivo compacto só com registros válidos
# Params: 
#         - registrosAnime: lista com os registros de anime lidos na memória
# -----------------------------------------------------------------------------------

def compactacaoEspaco(registrosAnime):
    with open("storageCompaction.txt", mode="w") as file:
        for registro in registrosAnime:
            if(registro[0] != "*"):
                file.write(registro)

# -----------------------------------------------------------------------------------
# Função: Escrita de registros de tamanho fixo com campos variados (|)
# Params: 
#         - registrosAnime: lista com os registros de anime lidos na memória
#         - arquivoSaida: arquivo de saída com os registros gravados no padrão
#         - debugging: flag para mostrar ou não os passos intermediários da lógica
# -----------------------------------------------------------------------------------

def EscritaRegistrosFixosCamposVariados(registrosAnime, arquivoSaida = "output.txt", 
    debugging = False):

    if(debugging):
        print(registrosAnime[0]) 

    # descobrindo o tamanho do maior registro contido no arquivo
    maiorTamanho = len(max(registrosAnime, key=len))
    if(debugging):
        print(maiorTamanho)

    with open(arquivoSaida, mode="w") as file:
        
        for registro in registrosAnime:
            # substituindo virgula (,) por pipe (|)
            novoRegistro = registro.replace(",", "|")
            novoRegistro = novoRegistro.replace("\n", "")
            
            # TODO: remover caracteres especiais
            novoRegistro = re.sub(r'[?$!\"\'`’]',r'',novoRegistro)    
                    
            # adicionando explicitamente espaços não usados (caracter *)
            diff = maiorTamanho - len(novoRegistro)
            aux = "*" * diff
            novoRegistro = novoRegistro + aux + "\n"
         
            if(debugging):
                print(novoRegistro)
            # gravando os registros no arquivo de saída padronizado            
            file.write(novoRegistro)
            
    return maiorTamanho

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

def LeituraRegistrosFixoCampoVariado(arquivoAnimes, tamanhoRegistro, RRN, tamanhoArquivo):
    
    registro = None
    deslocamento = tamanhoRegistro * RRN
    print("deslocamento: "+ str(deslocamento))
    
    # verificar se o deslocamento é maior do que o numero de registros existentes, 
    # nesse caso, retorna nulo
    if(deslocamento > tamanhoArquivo):
        print("Warning: RRN invalido")
    else:     
        arquivoAnimes.seek(deslocamento)
        registro = arquivoAnimes.readline()
    return(registro)
    
# -----------------------------------------------------------------------------------
# Função: principal (main)
# -----------------------------------------------------------------------------------

if __name__ == "__main__":
    
    tamanhoRegistro = None
    
    # ---------------------------- 
    # cria o arquivo com os registros padronizados, se não existir
    if (not os.path.exists("animes_fixedLength.txt")):
        f = open("../../datasets/animes.csv", mode="r", encoding="utf-8")
        registrosAnime = f.readlines()
        registrosAnime.pop(0) #removendo o cabeçalho (header)
        f.close()
        tamanhoRegistro = EscritaRegistrosFixosCamposVariados(registrosAnime=registrosAnime, 
            arquivoSaida="animes_fixedLength.txt", debugging=False)
    # ---------------------------- 
     
    # # Abrindo arquivo para leitura via RRN
    arquivoAnimes = open("animes_fixedLength.txt", mode="r", encoding="utf-8")

    # descobrindo o tamanho do registro se já existir o arquivo de registros
    if(tamanhoRegistro == None):
        tamanhoRegistro = len(arquivoAnimes.readline())
    print("Tamanho Registro: " + str(tamanhoRegistro))
 
    # descobrindo o tamanho do arquivo, para evitar a consulta de registros que não existem
    arquivoAnimes.seek(0, os.SEEK_END)
    tamanhoArquivoAnimes = arquivoAnimes.tell()
    print("Tamanho do Arquivo: " + str(tamanhoArquivoAnimes))
 
    # query = [0, 5, 2, 10, 40, 4, 41, 42, 43]
    # for value in query:
    for value in range(150, 450):
        registro = LeituraRegistrosFixoCampoVariado(arquivoAnimes=arquivoAnimes, tamanhoRegistro=tamanhoRegistro, 
            RRN=value, tamanhoArquivo=tamanhoArquivoAnimes)
        print("RRN = " + str(value))
        print(registro)
    
    # fechando o arquivo de animes 
    arquivoAnimes.close()
    
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
