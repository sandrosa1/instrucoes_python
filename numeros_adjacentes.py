numero = int(input("Digite numero"))
b = 10
a = 11
i = 0
j = 0
while True:
    while True:
        if ( a == b ):
            print( a, "e",b, "são iguais")
            j = j + 1
        elif (numero == 0) and (j != 0):
            break
        elif (numero == 0):
            print("O numero digitado não tem adjacentes")
            break
        aux = numero % 10
        numero = numero // 10
        if ( i % 2 == 0 ):
            a = aux
            i = i + 1
        else:
            b = aux
            i= i + 1
    if(numero == 0):
        break
        
    
    
