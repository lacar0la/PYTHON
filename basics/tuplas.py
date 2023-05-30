def reflejar_imagen(M:list)->list:
    aux = M
    alto = len(M)
    ancho = len(M[0])
    i = 0
    x = alto
    y = ancho

    for i in range(0, int(alto/2)):
        j = 0
        x = alto-1
        for j in range(0, ancho):
            M[i][j] = M[x][j]
            j= j +1
        i = i + 1
        x=x-1
    
        
    return (M)
