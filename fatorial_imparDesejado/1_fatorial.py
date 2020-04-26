cont = int(input("Digite numero para saber seu fatorial "))
fat = cont
if cont == 0:
    fat = 1
else:
    while cont != 1:
        cont = cont - 1
        fat = (fat * cont)
print (fat)   
   
    
