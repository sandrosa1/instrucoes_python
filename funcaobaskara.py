import math

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def main():
     a = float(input("Digite o valor de a:"))
     b = float(input("Digite o valor de b:"))
     c = float(input("Digite o valor de c:"))
     imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        raiz1 = ( -b + math.sqrt(d)) / (2 * a)
        print("A unica raiz è: ",raiz1)
    else:
        if d < 0:
            print("Ésta equação não possui raiz")
        else:
            raiz1 = ( -b + math.sqrt(d)) / (2 * a)
            raiz2 = ( -b - math.sqrt(d)) / (2 * a)
            print(" A raiz um e: ", raiz1 ,"e a raiz 2 e: ",raiz2) 
