a = int(input("Digite um numero inteiro "))

resto = a % 3
resto2 = a % 5
if resto == 0 and resto2 == 0:
	print("FizzBuzz")
else:
	print(a)
