import math # importa as funções matematicas
a= float(input(" Digite o valor para [ a ] " ))
b= float(input(" Digite o valor para [ b ] " ))
c= float(input(" Digite o valor para [ c ] " ))
delta = (b**2) - (4*a*c) #calcula o delta
if delta < 0: 
    print ("esta equação não possui raízes reais")# idententar sempre multiplos 4 espaços
    
elif delta == 0: # elif tem que especificar para executar somente o bloco
    x = -b / ( 2 * a )
    print ("a raiz desta equação é", x)
else:
    x1 = (-b + math.sqrt(delta)) / ( 2 * a )
    x2 = (-b - math.sqrt(delta)) / ( 2 * a )
    if x1 < x2 :
        print ("as raízes da equação são", x1,"e", x2)
    else:
        print ("as raízes da equação são", x2,"e", x1)			

              


