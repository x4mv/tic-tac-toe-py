from recortarArchivo import recortarArchivo
def extraerStats(player1,player2):

    texto = recortarArchivo()
    if texto == []:
        return 0,0,0

    count1Txt = texto[1]
    count2Txt = texto[2]
    countTieTxt = texto[3]


    #Extraer w de p1
    for letter in count1Txt.strip():
        if letter.isdigit():
            count1 = int(letter)
        else:
            pass
    
    #Extraer w de p2
    for letter in count2Txt.strip():
        if letter.isdigit():
            count2 = int(letter)
        else:
            pass
    
    #Extraer tie 
    for letter in countTieTxt.strip():
        if letter.isdigit():
            countTie = int(letter)
        else:
            pass


    
    return count1,count2,countTie
