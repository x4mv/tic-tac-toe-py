from recortarArchivo import recortarArchivo
def gameStats(player1,player2 , winner, count1,count2,countTie):

    if winner == player1:
        count1 += 1
    else:
        count2 +=1


    gameSetUp = {
        'GAME' : player1 + ' VS ' + player2,
        player1: str(count1),
        player2: str(count2),
        'TIE': countTie
    }

    """
    GAME: x4mv VS GG VENGANZA 
        x4mv : 3
        GGvenganza : 2
    
    GAME: TEREREPY VS addstation
        TEREREPY: 2
        addstation: 5
    """

    with open('./gameStats.txt', mode = 'w') as myFile :
        myFile.write(f'\n EL JUEGO : {gameSetUp["GAME"]} \n'    
                     f'{player1}: {gameSetUp[player1]} \n'    
                     f'{player2}: {gameSetUp[player2]} \n'
                     f'TIE: {gameSetUp["TIE"]}\n')
        
    
    lineasArchivo = recortarArchivo()
    print(lineasArchivo[0])
    print(lineasArchivo[1])
    print(lineasArchivo[2])
    print(lineasArchivo[3])
    
    print('Juego Guardado')
        