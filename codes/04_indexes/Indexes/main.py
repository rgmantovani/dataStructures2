from PrimaryIndex import *

if __name__ == "__main__":

    index = PrimaryIndex(dataFile = "animes50.txt")
    print("--------------------")
    index.print()
    print("--------------------")
    print("Records: " + str(index.getNumberOfRecords()))
    print("Valid Records: " + str(index.getNumberOfValidRecords()))
    print("Record length: " + str(index.getRecordLength()))
    print("--------------------")
    
    print(index.searchRecord(key="BLACKCLOVER"))
    print(index.searchRecord(key="ONEPIECE"))
    print(index.searchRecord(key="NARUTO"))