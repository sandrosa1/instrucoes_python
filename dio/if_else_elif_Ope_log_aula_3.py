# a = input('Primeiro valor')
# b = input('Primeiro valor')
# c = input('Primeiro valor')
# if a > b and a > c:
#     resultado = a
# elif b > a and b > c:
#     resultdo = b
# else:
#     resultado = c
# print('O maior numero e {}'3.format(resultado))
# print('Fim do programa')

# or = ou
# or not = inverte a condição

n1 = int(input('Nota Primeiro Bimestre'))
while n1 > 10:
    n1 = int(input('Vocẽ digitou errado. Digite novamente'))
n2 = int(input('Nota Segundo Bimestre'))
while n2 > 10:
    n2 = int(input('Vocẽ digitou errado. Digite novamente'))
n3 = int(input('Nota Terceiro Bimestre'))
while n3 > 10:
    n3 = int(input('Vocẽ digitou errado. Digite novamente'))
n4 = int(input('Nota Quarto Bimestre'))
while n4 > 10:
    n4 = int(input('Vocẽ digitou errado. Digite novamente'))

media = (n1 + n2 + n3 + n4)/4
print('Media:{}' .format(media))

