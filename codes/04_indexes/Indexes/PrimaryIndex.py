# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

import pickle
import os 

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
    
class PrimaryIndex:
     
    __dataFile             = None   # string with the datafile name
    __primaryIndexFile     = None   # string with the indexfile name
    __primaryTable         = list() # list of tuples (RRN, primary key)
    __numberOfRecords      = 0      # counting the number of records in the datafile 
    __numberOfValidRecords = 0      # counting the number of valid records in the datafile
    __recordLength         = None   # the length of the records in dataFile
    
    # -----------------------------------------------------------------
    # Constructor
    # -----------------------------------------------------------------
    
    def __init__(self, dataFile = None):
        
        try: # try to open files
            self.__dataFile = open(dataFile, mode="r+")
        except FileNotFoundError as error:
            print(error)
            exit(1)
        
        # --------------------------
        # mod 01: if not exists an index file already saved
        # --------------------------

        if(not os.path.exists("index.dat")):
            print("creating table")
            # iterating all lines and creating index Table
            RRN = 0
            for line in self.__dataFile:
                if(self.__recordLength == None):
                    self.__recordLength = len(line)

                key = self.__createPrimaryKey(record = line)
                tuple = (RRN, key)
                self.__primaryTable.append(tuple)
                RRN = RRN+1

            # setting the number of records
            self.__numberOfRecords = RRN
            self.__numberOfValidRecords = RRN
            # sorting the table
            self.__sortPrimaryTable()
        
        # --------------------------
        # mod 2: index.dat file exists (load its values)
        # --------------------------
        else:
            print("Loading previous table")
            self.__primaryIndexFile = open("index.dat", mode="rb+")
            unpickler = pickle.Unpickler(self.__primaryIndexFile)
            self.__primaryTable = pickle.load(self.__primaryIndexFile)
            
            # setting the number of records
            self.__numberOfRecords = len(self.__primaryTable)
            self.__numberOfValidRecords = len(self.__primaryTable)
            self.__recordLength = len(self.__dataFile.readline())
              
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def __loadExistingIndexFile(self):
        pass
      
      
    # -----------------------------------------------------------------
    # Storage Compaction of a file
    # -----------------------------------------------------------------
    
    def __storageCompaction(self):
        pass
    
    # -----------------------------------------------------------------
    # Destructor
    # -----------------------------------------------------------------
    
    def __del__(self):
        # storage compaction of the datafile
        self.__storageCompaction()
        # save primary index into primaryIndexFile (using pickle)
        if(self.__primaryIndexFile == None):
            print("aqui")
            self.__primaryIndexFile = open("index.dat", mode="wb")
        pickle.dump(self.__primaryTable, self.__primaryIndexFile)
        self.__dataFile.close()
        self.__primaryIndexFile.close()
    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def __createPrimaryKey(self, record):
        aux = record.strip()
        tokens = aux.split("|")
        key = tokens[0]
        key = key.upper()
        key = key.replace(" ", "")
        return (key)    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def print(self):
        for element in self.__primaryTable:
            print(element)
    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def insertRecord(self, record):
        pass
    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def __binarySearch(self, key):
        pass
    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    
    def searchRecord(self, key):
        # 1. Pesquisa/busca binária na Tabela de indices
        # na coluna Chave Canonica
        # 2a. Falhou -> return None
        # 2b. Encontrei: (Caralho! É isso)
        #   - acessar o RRN (tupla)
        #   - fazer a leitura do registro no arquivo de dados (via RRN)
        #   - retornar (registro)
        pass
    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def deleteRecord(self, key):
        # 1. Verificar se existe a chave na Tabela de indices
        #      - se não existir: é tetra (acabou!)
        # 2. Se existir
        #      - Invalida/remove o registro no arquivo de indices
        #      - Opçoes:
        #          * A: remove a tupla da tabela de Indices
        #          * B: invalidação da tupla na tabela de Indices
        pass
    
    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def updateRecord(self, record):
        pass
    
    # -----------------------------------------------------------------
    # Sort Primary Table
    # -----------------------------------------------------------------
    
    def __sortPrimaryTable(self):
        self.__primaryTable.sort(key = lambda tup: tup[1])
    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def getNumberOfRecords(self):
        return(self.__numberOfRecords)
    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def getNumberOfValidRecords(self):
        return(self.__numberOfValidRecords)
    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def getRecordLength(self):
        return(self.__recordLength)
    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    