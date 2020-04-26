contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachoro','cavalo','galo' ]
total = contador_letras(lista_animais)



soma = lambda a,b: a + b

print(soma(5,10))
print('Total de letras {}:'.format(total))
# criando calculadora com dicionario
calculadora ={
    'soma':         lambda a, b: a + b,
    'subtracao':    lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisão':      lambda a, b: a / b
}
#Ela e do tipo dicionario
print(type(calculadora))
# acionando a
soma = calculadora ['soma']
multiplicacao = calculadora ['multiplicacao']
print('A soma e {};'.format(soma(10,5)))
print(multiplicacao(2,4))
