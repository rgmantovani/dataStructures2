# ----------------------------------------------------
# ----------------------------------------------------

class IdxPrimario:

    # *** atributos
    __arquivoDados    = None   # string
    __arquivoIndices  = None   # string
    __hasException    = False
    __tabelaIndices   = list() # lista de tuplas ( RRN , CC )

    #-------------------------------------------------------
    #-------------------------------------------------------

    def __init__(self, dataFile = None, idxFile = None):

        print(" - Construindo uma Tabela de indices")
        if(dataFile == None or idxFile == None):
            raise Exception("Por favor, informe o nome dos arquivos de dados e indices")
            self.__hasException = True
            exit(1)
        else:
            # abrindo arquivo de dados
            try:
                print("* Arquivo de Dados: " + dataFile)
                self.__arquivoDados = open(dataFile, "r+")
            except FileNotFoundError as error:
                print(error)
                self.__hasException = True
                exit(1)

            #abrindo arquivo de indices
            try:
                print("* Arquivo de Indices: " + idxFile)
                self.__arquivoIndices = open(idxFile, "w+")
            except FileNotFoundError as error:
                print(error)
                self.__hasException = True
                exit(1)

            # imprimindo a lista de
            print("* Lista de Tuplas")
            print(self.__tabelaIndices)

            #criar a tabela de indices
            linhas = self.__arquivoDados.readlines()

            #  - percorrer o arquivo de dados
            # 0 até qtdeLinhas (len/size linhas)
            # header = linhas[0]
            for index in range(1, len(linhas)):
            #      * ler o registro da linha
                print(index,":",linhas[index])
            #      * criar chave canonica, RRN
                key = self.criaChaveCanonica(registro = linhas[index])
                print("Key: ", key)
            #      * gera tupla (RRN, CC)
                RRN = index - 1
                print("RRN: ", RRN)
            #      * add na lista
                tupla = (RRN, key)
                self.__tabelaIndices.append(tupla)

            # print(self.__tabelaIndices)
            self.imprimeTabelaIndices(tabela = self.__tabelaIndices)
            print("\n **** Depois do Sort ***** ")
            # ordenar a tabela de indices
            self.__tabelaIndices.sort(key = lambda tup: tup[1])
            self.imprimeTabelaIndices(tabela = self.__tabelaIndices)

    #-------------------------------------------------------
    #-------------------------------------------------------

    def criaChaveCanonica(self, registro):
        aux = registro.strip()
        tokens = aux.split("|")
        # print("Tokens: ", tokens)
        # ano, nome
        key = tokens[0] + tokens[4]
        key = key.upper()
        key = key.replace(" ", "")
        return (key)

    #-------------------------------------------------------
    #-------------------------------------------------------

    def imprimeTabelaIndices(self, tabela):
        for element in tabela:
            print(element)

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
        for elem in self.__tabelaIndices:
            self.__arquivoIndices.write(str(elem) + "\n")

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
