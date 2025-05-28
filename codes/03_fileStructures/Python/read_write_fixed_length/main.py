# -----------------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------------

from RegistroTamanhoFixo import *
import subprocess

# -----------------------------------------------------------------------------------
# Função: principal (main)
# -----------------------------------------------------------------------------------

if __name__ == "__main__":
    
    # Output file 
    arquivoSaida = "arquivoDadosRegistrosFixos.txt"
    
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
        arquivoSaida=arquivoSaida, debugging=False)
    
    # ---------------------
    # ---------------------
    
    # Abrindo o arquivo com registros de tamanho fixo e campos variados
    arquivoDados = open(arquivoSaida, mode="r", encoding="utf-8")

    # descobrindo o tamanho do registro    
    registro = arquivoDados.readline()
    SIZE = len(registro)
 
    # descobrindo o numero de linhas do arquivo (quantidade de registros)
    numeroRegistros = int(subprocess.check_output(['wc', '-l', arquivoSaida]).split()[0])
    print(numeroRegistros)
   
    # Tentando ler todos os exemplos (0, linhas - 2)
    for i in range(0, numeroRegistros):
        reg = LeituraRegistrosFixosCamposVariados(arquivoDados=arquivoDados, 
                tamanhoRegistro=SIZE, RRN=i)
        print(reg)
    
    # fechando o arquivo de dados    
    arquivoDados.close()
    
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

