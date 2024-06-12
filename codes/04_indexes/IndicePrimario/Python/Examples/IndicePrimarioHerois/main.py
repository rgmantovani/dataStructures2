# ----------------------------------------------------
# ----------------------------------------------------

from IdxPrimario import *
# from Games import Game

# ----------------------------------------------------
# ----------------------------------------------------

if __name__ == '__main__':
    print("holla que tal?")
    # obj = IdxPrimario(idxFile = "idxFile.txt")
    obj = IdxPrimario(dataFile = "games.txt", idxFile = "idxFile.txt")
    newRecord = "The Legend of Zelda - Phantom Hourglass|Nintendo|Action-adventure|Nintendo DS|2007|Everyone10+|200.00|Digital|0.09"
    print(newRecord)
    obj.inserirRegistro(registro = newRecord)

# ----------------------------------------------------
# ----------------------------------------------------
