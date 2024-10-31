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
            
            # adicionando explicitamente espaços não usados (caracter *)
            diff = maiorTamanho - len(novoRegistro)
            aux = "*" * diff
            novoRegistro = novoRegistro + aux + "\n"
         
            if(debugging):
                print(novoRegistro)
            # gravando os registros no arquivo de saída padronizado            
            file.write(novoRegistro)

# -----------------------------------------------------------------------------------
# Função: principal (main)
# -----------------------------------------------------------------------------------

if __name__ == "__main__":
    
    # Abrindo o arquivo fonte
    f = open("animes.csv", mode="r", encoding="utf-8")
    
    # Lendo todos os registros e armazenando em uma lista (registrosAnime)
    registrosAnimes = f.readlines()
    
    #removendo o cabeçalho (header)
    registrosAnimes.pop(0)
    
    # fechando o arquivo
    f.close()
    
    # realizando a escrita dos registros em um arquivo com registros de tamanho fixo,
    #  e campos de tamanhos variados
    EscritaRegistrosFixosCamposVariados(registrosAnimes=registrosAnimes, 
        arquivoSaida="fixedLength.txt", debugging=True)
    
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
