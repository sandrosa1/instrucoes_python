numero= int(input("Digite um numero para saber se ele e primo "))
if numero == 1:
    print("nao primo")
else:
    cont = 2
    while cont != numero:
        if ( numero % cont == 0 ):
            print ("não primo")
            break
        else:
            cont= cont + 1
    if cont == numero:
        print("primo")


    
    
    
