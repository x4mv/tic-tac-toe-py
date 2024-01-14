"""
Crear una aplicacion de tictactoe

X La aplicacion debera de ser capaz de registrar 2 usuarios 
X. La aplicacion debera de ser capaz de realizar el juego tictactoe
    X Solucionar un bug el q empieza es x o 
    - Solucionar cuando usa una casilla ocupada
3. La aplicacion debera de ser capaz de guardar un registro de las partidas en un archivo
    3.1 - Debera almacenar los juegos 
    X - Y la puntuacion de cada jugador 

"""
from registarUser import registrarUser
from quienInicia import quienInicia
from extraerStats import extraerStats
from game import game

#contadores para registrar la partida
count1 = 0 
count2 = 0
countTie = 0 



player1, player2 = registrarUser()
first = quienInicia(player1, player2)

#extraer los valores del archivo 
count1, count2, countTie = extraerStats(player1,player2)

game(player1,player2,first, count1, count2, countTie)



