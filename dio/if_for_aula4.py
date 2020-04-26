# a = int(input('Entre com um numero: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     if resto == 0:
#         div +=1
# if div == 2:
#     print('numero {} é primo'.format(a))
# else:
#     print('número {} não e primo'.format(a))



# a = int(input('Entre com um valor:'))
# for num in range(a):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             div +=1
#     if div == 2:
#          print('numero {} é primo'.format(num))


a = 0
while a <= 10:
    print(a)
    a+=1
#aqui chamamos o metodo contador_letras
#para importar outra função junto e so semparar com virgula
from contador_letras import contador_letras, teste

if __name__ == '__main__':
    lista = ['elefante','zebra','leão']
    print(contador_letras(lista))
    print(teste())

