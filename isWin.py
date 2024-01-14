def isWin(a,b,c,d,e,f,g,h,i):
    if a == b == c and  a != " ":
        print('Is a Win!!!')
        return True
    elif d == e == f and  d != " ":
        print('Is a Win!!!')
        return True
    elif g == h == i and  g != " ":
        print('Is a Win!!!')
        return True
    elif a == d == g and  a != " ":
        print('Is a Win!!!')
        return True
    elif b == e == h and  b != " ":
        print('Is a Win!!!')
        return True
    elif c == f == i and  c != " ":
        print('Is a Win!!!')
        return True
    elif a == e == i and  a != " ":
        print('Is a Win!!!')
        return True
    elif g == e == c and  g != " ":
        print('Is a Win!!!')
        return True
    elif " " not in [a,b,c,d,e,f,g,h,i]  :
        print("Is a TIE !!!")
        return 'tie' 
    else: 
        return False
