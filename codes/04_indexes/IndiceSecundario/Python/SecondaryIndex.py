# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

import pickle
import os 
import io

from PrimaryIndex import *

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

class SecondaryIndex(PrimaryIndex):

    __secondaryIndexFile    = None   # string with the indexfile name
    __secondaryTable        = list() # list of tuples (secondary key, primary key)

    # -----------------------------------------------------------------
    # Constructor
    # -----------------------------------------------------------------
    def __init__(self, dataFile = None):

        super().__init__(dataFile)
        self.__secondaryIndexFile = "secondaryIndex.dat"
        self.__createSecondaryIndex()

    # -----------------------------------------------------------------
    # Destructor
    # -----------------------------------------------------------------
    
    def __del__(self):
        
         # save secondary index into secondaryIndexFile (using pickle)
        if(self.__secondaryIndexFile == None):
            self.__secondaryIndexFile = open("secondIndex.dat", mode="wb")
        pickle.dump(self.__secondaryTable, self.__secondaryIndexFile)
        
        # parent destructor
        super().__del__()
        self.__secondaryIndexFile.close()

    # -----------------------------------------------------------------
    # -----------------------------------------------------------------

    def __createSecondaryKey():
        pass

    # -----------------------------------------------------------------
    # -----------------------------------------------------------------

    def print():
        pass

    # -----------------------------------------------------------------
    # -----------------------------------------------------------------

    def insertRecord(self, record):
        pass

    # -----------------------------------------------------------------
    # -----------------------------------------------------------------

    def __multipleBinarySearch(self, key):
        pass

    # -----------------------------------------------------------------
    # -----------------------------------------------------------------

    def searchRecord(self, key):
        pass

    # -----------------------------------------------------------------
    # -----------------------------------------------------------------

    def deleteRecord(self, key):
        pass

    # -----------------------------------------------------------------
    # -----------------------------------------------------------------

    def updateRecord(self, record):
        return super().updateRecord(record)


    # -----------------------------------------------------------------
    # -----------------------------------------------------------------

    def __sortSecondaryTable(self):
         
        self.__secondaryTable.sort(key = lambda tup: tup[1])
        super().__sortPrimaryTable()

        pass

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
