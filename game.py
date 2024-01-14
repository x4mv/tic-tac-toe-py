from displayBoard import displayBoard
from updateValues import updateValues
from isWin import isWin
from gameStats import gameStats


def game(player1, player2, first, count1, count2,countTie):
    # Valores default del tablero
    a = ' '
    b = ' '
    c = ' '
    d = ' '
    e = ' '
    f = ' '
    g = ' '
    h = ' '
    i = ' '

    #Determinar de quien es el turno 
    turno = first
    #Banderas para parar el juego
    isWinBandera = False
    flag = True
    


    displayBoard(a,b,c,d,e,f,g,h,i,flag)
    flag = False
    print(f'El jugador {first} inicia la partida')

    while isWinBandera == False:

        print('\n')
        print(f'El turno es de: {turno} ')
        a,b,c,d,e,f,g,h,i = updateValues(a,b,c,d,e,f,g,h,i, player1, turno)
        displayBoard(a,b,c,d,e,f,g,h,i,flag)
        isWinBandera = isWin(a,b,c,d,e,f,g,h,i)
        if isWinBandera == True:
            winner = turno
            print(f'El ganador es: {turno}')
        elif isWinBandera == 'tie':
            countTie +=1
            winner = None
            
        if turno == player1 :
            turno = player2
        else: 
            turno = player1
    
    displayBoard(a,b,c,d,e,f,g,h,i,flag)
    gameStats(player1, player2, winner, count1, count2, countTie)



