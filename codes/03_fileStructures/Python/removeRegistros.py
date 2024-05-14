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
# Função: principal (main)
# -----------------------------------------------------------------------------------
   
if __name__ == "__main__":   
    
    # Abrindo o arquivo fonte
    f = open("animes.csv", mode="r", encoding="utf-8")
    
    # Lendo todos os registros e armazenando em uma lista (registrosAnime)
    registrosAnime = f.readlines()
    
    # removendo cabecalho (primeiro registro com meta-dados)
    registrosAnime.pop(0)
    
    # fechando o arquivo
    f.close()
    
    # testes de remoção de registros válidos
    removeRegistrosPorRRN(registrosAnime = registrosAnime, id = 0)
    removeRegistrosPorRRN(registrosAnime = registrosAnime, id = 10)
    removeRegistrosPorRRN(registrosAnime = registrosAnime, id = 15)
    removeRegistrosPorRRN(registrosAnime = registrosAnime, id = 12)
    removeRegistrosPorRRN(registrosAnime = registrosAnime, id = 17)
    
    # remoção de indice/posição inválida
    removeRegistrosPorRRN(registrosAnime = registrosAnime, id = 50)
    
    # debug: mostrando a lista alterada, com os registros invalidados
    print(registrosAnime)
    
    # gravando um novo arquivo com os dados removidos/invalidados
    with open("depoisRemocao.txt", mode="w") as file:
        for registro in registrosAnime:
            file.write(registro)
    
    # gerando novo arquivo compacto, só com os registros válidos
    compactacaoEspaco(registrosAnime)

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------