from random import choice
def quienInicia(player1, player2):
    lista = [player1, player2]

    #Elige quien va a ir primero
    first = choice(lista)

    return first

