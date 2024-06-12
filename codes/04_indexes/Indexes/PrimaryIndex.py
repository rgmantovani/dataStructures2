# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

import pickle
import os 
import io

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

# TODO:
#   - fix RRN counting when creating index from file (after some deletions)
#   - add reuse (metadata, headers, and so on)
#   - implement update functions

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
            print("@ Creating table")
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
            print("@ Loading previous table")
            self.__loadExistingIndexFile()
            
            # setting the number of records
            self.__numberOfRecords = len(self.__primaryTable)
            self.__numberOfValidRecords = len(self.__primaryTable)
            self.__recordLength = len(self.__dataFile.readline())
              
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def __loadExistingIndexFile(self):
        self.__primaryIndexFile = open("index.dat", mode="rb+")
        unpickler = pickle.Unpickler(self.__primaryIndexFile)
        self.__primaryTable = pickle.load(self.__primaryIndexFile)
      
    # -----------------------------------------------------------------
    # Storage Compaction of a file
    # -----------------------------------------------------------------
    
    def __storageCompaction(self):
        storageFile = open("dataCompacted.txt", mode="w")
        self.__dataFile.seek(0, io.SEEK_SET)
        for record in self.__dataFile:
            if(record[0] != "*"):
                storageFile.write(record)
            else:
                print(record)
      
    # -----------------------------------------------------------------
    # Destructor
    # -----------------------------------------------------------------
    
    def __del__(self):
        # storage compaction of the datafile
        self.__storageCompaction()
      
        # save primary index into primaryIndexFile (using pickle)
        if(self.__primaryIndexFile == None):
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
        # add new record if there is no previous key with the same value
        key = self.__createPrimaryKey(record)
        existingRecord = self.searchRecord(key)
        if( existingRecord == []):
            # adding new tuple to the primary table
            newTuple = (self.__numberOfValidRecords, key)
            self.__primaryTable.append(newTuple)
            self.__sortPrimaryTable()
            # updating statistics
            self.__numberOfValidRecords = self.__numberOfValidRecords + 1
            self.__numberOfRecords = self.__numberOfRecords + 1
            # writing in the file 
            self.__dataFile.seek(0, io.SEEK_END)
            self.__dataFile.write("\n" + record)
            print("New record was added!")       
        else:
            print("There is also a record with this key. Not inserting")
    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def __binarySearch(self, key): 
        start, end = 0, len(self.__primaryTable) - 1
        while(start <= end):
            midpoint = (start + end)//2
            midtuple = self.__primaryTable[midpoint]
            if(midtuple[1] == key):
                return (True, midpoint, midtuple[0])
            elif (key < midtuple[1]):
                end = midpoint-1
            else:
                start = midpoint+1
        return (False, None, None)
    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def searchRecord(self, key):
        [status, _, RRN] = self.__binarySearch(key)
        if(not status): # not found, does not exist
            return([])
        else: # read from file, using seek method
            record = self.__readRecordByRRN(RRN=RRN)
            return(record)
    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def __readRecordByRRN(self, RRN):
        offset = RRN * self.__recordLength
        self.__dataFile.seek(offset)
        record = self.__dataFile.readline()
        return(record)
    
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    
    def deleteRecord(self, key):
        [status, id, RRN] = self.__binarySearch(key)
        if(not status):
            print("There is nothing to remove!")
        else:        
            # invalidate record in datafile
            offset = self.__recordLength * RRN
            self.__dataFile.seek(offset)
            self.__dataFile.write("*|")
        
            #remove tuple from the primary table
            self.__primaryTable.pop(id)
            self.__numberOfValidRecords = self.__numberOfValidRecords - 1
            print("Record removed!") 
    
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
  
    def printStats(self):  
        print("--------------------")
        print("Records: " + str(self.getNumberOfRecords()))
        print("Valid Records: " + str(self.getNumberOfValidRecords()))
        print("Record length: " + str(self.getRecordLength()))
        print("--------------------")
    
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
    