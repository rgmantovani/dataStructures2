from PrimaryIndex import *

if __name__ == "__main__":

    index = PrimaryIndex(dataFile = "animes50.txt")
    index.printStats()
           
    print(index.searchRecord(key="BLACKCLOVER"))
    print(index.searchRecord(key="ONEPIECE"))
    print(index.searchRecord(key="NARUTO"))
    
    newRecord = "Gintama|https://www.crunchyroll.com/gintama|https://img1.ak.crunchyroll.com/i/spire2/54c15675670ba44c1f98c3e11ba0cddf1515030877_full.jpg|379|11435|55745|4.87|133|47|124|509|10622|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0***********************************************************************************************************************************"
    index.insertRecord(record = newRecord)
    index.printStats()
    
    newRecord = "BORUTO: NARUTO NEXT GENERATIONS|https://www.crunchyroll.com/boruto-naruto-next-generations|https://img1.ak.crunchyroll.com/i/spire1/ffe5a84ffeafce5f20693f7e9b6ff0151579221442_full.jpg|148|893|2865|3.21|237|127|80|111|338|1.0|1.0|0.0|0.0|0.0|1.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|1.0|0.0|0.0|0.0|0.0*****************************************************************************************"
    index.insertRecord(record = newRecord)
    index.printStats()
    
    keys = ["REBORN", "BLEACH", "DEMONKINGDAIMAO"]
    for removeKey in keys:
        index.deleteRecord(key=removeKey)
        index.printStats()