jugadas = []


def inputUser():
    location = None
    flag = False
    rango = range(1,10)
        
    print('\n')

    while location == None or flag == False:

        location = input('Porfavor ingresar un valor entre 1-9: ')

        #comprobamos que sea un digito 
        if location.isdigit() == False:
            print('El valor ingresado no es un digito!!! ')

        if location.isdigit():
            if int(location) not in rango:
                print('El valor esta fuera de los rangos!!!')
        
        if int(location) in jugadas:
            print('La casilla ya esta ocupada!!!')
        else: 
            jugadas.append(int(location))
            flag = True

    
    return int(location)

