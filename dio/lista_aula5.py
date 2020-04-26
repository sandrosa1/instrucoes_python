lista = [1,3,5,7]
listaAnimal = ['cachorro','gato','elefante']

print(type(listaAnimal))

print(listaAnimal[1])

for x in listaAnimal:
    print(x)

soma = 0

for x in lista:
    print(x)
    soma += x
print('Soma=',soma)
#soma a lista
print(sum(lista))
#Maior valor da lista
print(max(lista))
#menor valor lista
print(min(lista))
#maior letra do alfabeto
print(max(listaAnimal))
#menor letra do alfabeto
print(min(listaAnimal))

'''
x = str(input('Incluir animal '))
if x in listaAnimal:
    print('Tem')
else:
    print('Não tem')
    #vai incluir o animal na lista
    listaAnimal.append('lobo')
    print('Nova lista',listaAnimal)'''
# rei
listaAnimal.pop()
print(listaAnimal)