def main():

    n = int(input("Digite n: "))
    m = int(input("Digite m: "))

    anterior  = n
    atual     = m

    resto = atual % anterior
    while resto != 0:
        resto = anterior % atual;
        anterior = atual;
        atual = resto;

    print("mdc(%d,%d)=%d" %(n,m,anterior))

#-------------------------------------------------
main()
