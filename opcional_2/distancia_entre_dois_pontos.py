import math
x1= float(input("Digite a 1⁰ coordenada x "))
y1= float(input("Digite a 1⁰ coordenada y "))
x2= float(input("Digite a 2⁰ coordenada x "))
y2= float(input("Digite a 2⁰ coordenada y "))

distancia= math.sqrt ( ( x1 - x2 ) **2 + ( y1 - y2 ) **2 )

if distancia >= 10:
    print ("longe")
else:
    print ("perto")
