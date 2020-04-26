def main():
    par = 0
    impar = 0
    n = int(input("dd "))
    while ( n != 0):
        if (n % 2 == 0):
            par = par + 1
        else:
            impar = impar + 1
        n = int(input("dd "))
    print(par)
    print(impar)
