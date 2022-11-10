# ----------------------------------------------------
# ----------------------------------------------------

class IdxPrimario:

    # *** atributos
    __arquivoDados    = None
    __arquivoIndices  = None
    __tabelaIndices   = list()

    #-------------------------------------------------------
    #-------------------------------------------------------

    def __init__(self, dataFile = None, idxFile = None):

        print(" - Construindo uma Tabela de indices")
        if(dataFile == None or idxFile == None):
            raise Exception("Por favor, informe o nome dos arquivos de dados e indices")
            exit(1)
        else:
            # abrindo arquivo de dados
            try:
                print("* Arquivo de Dados: " + dataFile)
                self.__arquivoDados = open(dataFile, "r+")
            except FileNotFoundError as error:
                print(error)
                exit(1)

            #abrindo arquivo de indices
            try:
                print("* Arquivo de Indices: " + idxFile)
                self.__arquivoIndices = open(idxFile, "w+")
            except FileNotFoundError as error:
                print(error)
                exit(1)

            # imprimindo a lista de
            print("* Lista de Tuplas")
            print(self.__tabelaIndices)

    #-------------------------------------------------------
    #-------------------------------------------------------

    #destrutor
    def __del__(self):
        print(" - Destruindo a tabela de Indices")
        print(" * salvando a tabela atual no arquivo de indices")
        self.gravarArqIdx()
        print(" * fechando os arquivos")
        self.__arquivoDados.close()
        self.__arquivoIndices.close()

    #-------------------------------------------------------
    #-------------------------------------------------------

    def gravarArqIdx(self):
        print("Uuuuuuhhhhh")

    #-------------------------------------------------------
    #-------------------------------------------------------

    def carregarArqIndice(self):
        pass

    def inserirRegistro(self, registro):
        pass

    def removerRegistro(self, chave):
        pass

    def pesquisarRegistro(self, chave):
        pass

    def atualizarIndice(self):
        pass

    def atualizarRegistro(self, registro):
        pass

    def criaChaveCanonica(self, registro):
        pass

    # RRN, byteOffset
    def lerRegistro(self, param, type='RRN'):
        pass

    def numeroRegistros(self):
        pass

    def ordenarTabelaIdx(self):
        # sort
        pass

# ----------------------------------------------------
# ----------------------------------------------------
