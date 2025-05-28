# -----------------------------------------------------------------------------------
# Função: Escrita de registros de tamanho fixo com campos variados (|)
# Params: 
#         - registrosAnime: lista com os registros de anime lidos na memória
#         - arquivoSaida: arquivo de saída com os registros gravados no padrão
#         - debugging: flag para mostrar ou não os passos intermediários da lógica
# -----------------------------------------------------------------------------------

def LeituraRegistrosFixosCamposVariados(arquivoDados, tamanhoRegistro, RRN, debugging = False):

        offset = RRN * tamanhoRegistro
        arquivoDados.seek(offset)
        registro = arquivoDados.readline()
        return(registro)

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------