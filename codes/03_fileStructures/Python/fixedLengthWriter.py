# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# Método 01: Escrita de registros de tamanho fixo com campos variados (|)
# input: anime.csv
# output: saida.txt

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

def FixedRecordWithVariableFields(animeRecords, outputFile = "output.txt", debugging = False):

    #removing header
    animeRecords.pop(0)
    if(debugging):
        print(animeRecords[0]) 

    # finding the max record size
    maxSIZE = len(max(animeRecords, key=len))
    if(debugging):
        print(maxSIZE)


    with open(outputFile, mode="w") as file:
        
        for record in animeRecords:
            
            #replacing , by |
            newrecord = record.replace(",", "|")
            newrecord = record.replace("\n", "")
            
            # adding not used space (showing with * character)
            diff = maxSIZE - len(newrecord)
            aux = "*" * diff
            newrecord = newrecord + aux + "\n"
         
            if(debugging):
                print(newrecord)
            file.write(newrecord)

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

if __name__ == "__main__":
    
    f = open("animes.csv", mode="r", encoding="utf-8")
    animeRecords = f.readlines()
    f.close()
    
    FixedRecordWithVariableFields(animeRecords=animeRecords, outputFile="fixedLength.txt", debugging=True)
    # Delimiters(animeRecords)
    
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
