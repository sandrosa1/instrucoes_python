largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
cont = largura
while altura > 0:
    while cont > 0:
        cont = cont - 1
        print("#", end= "")
    cont = largura
    print()
    altura = altura - 1
    
    
