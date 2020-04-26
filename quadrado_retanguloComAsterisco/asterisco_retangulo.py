largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
if altura == largura:
    cont = largura
    while altura > 0:
        while cont > 0:
            cont = cont - 1
            print("#", end= "")
        cont = largura
        print()
        altura = altura - 1
else:
     cont = largura
     cont2 = altura
     while cont2 > 0:
             while cont > 0:
                 cont = cont - 1
                 if cont2 == altura or cont2 == 1 :
                     print("#", end= "")
                 elif cont == largura - 1 or cont == 0:
                     print ("#", end="")
                 else:
                     print(" ",end="")
             cont = largura
             print()
             cont2 = cont2 - 1
        
             
             
             
     
          
