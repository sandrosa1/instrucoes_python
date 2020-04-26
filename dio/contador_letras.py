def contador_letras(lista_palavars):
    contador =[]
    for x  in lista_palavars:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

def teste ():
    return 'teste'

if __name__ == '__main__':
    lista = ['cachorro','gato']
    print(contador_letras(lista))
    print(teste())


