def remove_repetidos(lista):
    lista1 = lista
    i = 1
    for j in (0, len(lista)-1, 1):
        for i in (j + 1, len(lista), 1):
            if lista[j] == lista[i]:
                del lista[i]
    return sorted(lista)
       
            
        
