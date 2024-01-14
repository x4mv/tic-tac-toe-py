def inputUser():
    
    print('\n')
    location = None
    flag = False
    rango = range(1,10)

    while location == None or flag == False:

        location = input('Porfavor ingresar un valor entre 1-9: ')

        #comprobamos que sea un digito 
        if location.isdigit() == False:
            print('El valor ingresado no es un digito!!! ')

        if location.isdigit():
            if int(location) not in rango:
                print('El valor esta fuera de los rangos!!!')
            else: 
                flag = True
    
    return int(location)

