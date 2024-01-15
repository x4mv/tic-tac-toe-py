from inputUser import inputUser
def updateValues(a,b,c,d,e,f,g,h,i,player1,turno):
    
    pos_jugada = inputUser()
    if turno == player1 : 
        if pos_jugada == 1 and a == " ": 
            a = 'X'
        elif pos_jugada == 2 and b == " ": 
            b = 'X'
        elif pos_jugada == 3 and c == " ": 
            c = 'X'
        elif pos_jugada == 4 and d == " ": 
            d = 'X'
        elif pos_jugada == 5 and e == " ": 
            e = 'X'
        elif pos_jugada == 6 and f == " ": 
            f = 'X'
        elif pos_jugada == 7 and g == " ": 
            g = 'X'
        elif pos_jugada == 8 and h == " ": 
            h = 'X'
        elif pos_jugada == 9 and i == " ": 
            i = 'X'
        
    else:
        if pos_jugada == 1 and a == " ": 
            a = 'O'
        elif pos_jugada == 2 and b == " ": 
            b = 'O'
        elif pos_jugada == 3 and c == " ": 
            c = 'O'
        elif pos_jugada == 4 and d == " ": 
            d = 'O'
        elif pos_jugada == 5 and e == " ": 
            e = 'O'
        elif pos_jugada == 6 and f == " ": 
            f = 'O'
        elif pos_jugada == 7 and g == " ": 
            g = 'O'
        elif pos_jugada == 8 and h == " ": 
            h = 'O'
        elif pos_jugada == 9 and i == " ": 
            i = 'O'
    return a,b,c,d,e,f,g,h,i



