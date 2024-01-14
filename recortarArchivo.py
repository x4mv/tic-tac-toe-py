def recortarArchivo():

    with open('./gameStats.txt', mode  = 'r' ) as readFile :
            lineas = readFile.readlines()[1:6]
    
    return lineas 