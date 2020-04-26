def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n -1
    return fat

def numero_binominal(n,k):
    return fatorial(n) // (fatorial(k) * fatorial(n - k))



def testa_fatorial():
    if fatorial (1) == 1:
        print ("Funciona para 1")
    else:
        print ("Não funciona")
    if fatorial (2) == 2:
        print ("Funciona para 2")
    else:
        print ("Não funciona 2")
    if fatorial (0) == 1:
        print ("Funciona para 0")
    else:
        print ("Não funciona 0")
    if fatorial (5) == 120:
        print ("Funciona para 5")
    else:
        print ("Não funciona 5")

def testa_numero_binominal():
    if numero_binominal (5, 2) == 10 :
        print("Funciona para 5, 2")
    else:
        print("5, 2 não funciona")
    if numero_binominal (10, 8) == 45 :
        print("Funciona para 10, 8")
    else:
        print("10, 8 não funciona")
        
