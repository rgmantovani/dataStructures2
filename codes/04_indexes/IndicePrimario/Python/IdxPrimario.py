# ----------------------------------------------------
# ----------------------------------------------------

class IdxPrimario:

    # *** atributos
    __arquivoDados    = None   # string
    __arquivoIndices  = None   # string
    __tabelaIndices   = list() # lista de tuplas ( RRN , CC )

    #-------------------------------------------------------
    #-------------------------------------------------------

    def __init__(self, dataFile = None, idxFile = None, debug = False):

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
            print("* Arquivo de Indices: " + idxFile)
            self.__arquivoIndices = open(idxFile, "w+")

            # imprimindo a lista de
            print("* Lista de Tuplas")
            print(self.__tabelaIndices)

            #criar a tabela de indices
            linhas = self.__arquivoDados.readlines()

            #  - percorrer o arquivo de dados
            # 0 até qtdeLinhas (len/size linhas) - header = linhas[0]
            for index in range(1, len(linhas)):
                key = self.criaChaveCanonica(registro = linhas[index])
                RRN = index - 1
                tupla = (RRN, key)
                self.__tabelaIndices.append(tupla)
                if(debug == True):
                    print(index,":",linhas[index])
                    print("RRN: ", RRN)
                    print("Key: ", key)

            # ordenar a tabela de indices
            self.__tabelaIndices.sort(key = lambda tup: tup[1])
            if(debug == True):
                print("\n **** Depois do Sort ***** ")
                self.imprimeTabelaIndices(tabela = self.__tabelaIndices)

    #-------------------------------------------------------
    #-------------------------------------------------------

    def criaChaveCanonica(self, registro):
        aux = registro.strip()
        tokens = aux.split("|")
        key = tokens[0] + tokens[4]  # ano +  nome
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
        for elem in self.__tabelaIndices:
            self.__arquivoIndices.write(str(elem) + "\n")

    #-------------------------------------------------------
    #-------------------------------------------------------

    def carregarArqIndice(self):
        pass

    def inserirRegistro(self, registro):
        print(" *** Inserindo um novo registro")
        key = self.criaChaveCanonica(registro = registro)
        # 1. Verifica se ja existe registro na Tabela de Indices
        #      - Se existir, já termina (não insere)
        output = [item for item in self.__tabelaIndices if item[1] == key]
        if(len(output) == 0):
            print(" - Não existe o elemento, inserindom ...")
            # 2. Verifica se existe opção/posição p reuso
            #      - Se tiver posicao (TOP = X)
            #           - escrever o registro na posicao X
            #      - Senão: append no final do arquivo
            self.__arquivoDados.write(registro)
            # 4. Cria a nova entrada na Tabela de Indices
            newEntry = (len(self.__tabelaIndices), key)
            # print(newEntry)
            self.__tabelaIndices.append(newEntry)
            # 5. Reordenação da Tabela de Indices
            self.__tabelaIndices.sort(key = lambda tup: tup[1])
            # print("-----------------------------------------")
            # self.imprimeTabelaIndices(tabela = self.__tabelaIndices)
        else:
            print("- Elemento já existe. Não inserindo!")

    def removerRegistro(self, chave):
        # 1. Verificar se existe a chave na Tabela de indices
        #      - se não existir: é tetra (acabou!)
        # 2. Se existir
        #      - Invalida/remove o registro no arquivo de indices
        #      - Opçoes:
        #          * A: remove a tupla da tabela de Indices
        #          * B: invalidação da tupla na tabela de Indices
        pass

    def pesquisarRegistro(self, chave): # [retornar 1 registro ou nada]
        # 1. Pesquisa/busca binária na Tabela de indices
        # na coluna Chave Canonica
        # 2a. Falhou -> return None
        # 2b. Encontrei: (Caralho! É isso)
        #   - acessar o RRN (tupla)
        #   - fazer a leitura do registro no arquivo de dados (via RRN)
        #   - retornar (registro)
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
