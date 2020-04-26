n = int(input("Digite numero inteiro "))
cont = 0
total = 0
while total < n:
    if cont % 2 == 1:
        total = total + 1
        print (cont)
    else:
        total = total + 0
    cont = cont + 1
