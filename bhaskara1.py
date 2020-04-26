import math # importa dados matemâticos
a = float(input("Digite o valor de a: "))#entrada dos dados
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c #achar o delta

if delta == 0: # delta igual a zero
	raiz1 = (-b + math.sqrt(delta)) / (2 *a)
	print("A ùnica raiz é: ", raiz1)
else:
	if delta < 0: # delta menor que zero
		print("Não existe raizes reais")
	else: # senão
		raiz1 = (-b + math.sqrt(delta)) / (2 *a)
		raiz2 = (-b - math.sqrt(delta)) / (2 *a)
		print ("As raizes são: x¹=", raiz1,"e x²=",raiz2) 
