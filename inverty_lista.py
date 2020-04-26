i = 0
inv = []
lista=[]
n = int(input("Digite um número: "))
if n != 0:
    lista.append(n)
    while True:
        i += 1
        n = int(input("Digite um número: "))
        if n == 0:
            break
        lista.append(n)
    for x in range ((len(lista) - 1), -1, -1):
        print (lista[x])
    
    
    
    
  
