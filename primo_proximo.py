def maior_primo(x):
        cont = 2
        while cont != x:
            if ( x % cont == 0 ):
                x = x - 1
            else:
                cont = cont + 1
        if x == cont:
            print(x)

                
                
        
