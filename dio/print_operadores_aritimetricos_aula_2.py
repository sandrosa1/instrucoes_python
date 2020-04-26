a = int(input('Entre com o primeiro valor '))
b = int(input('Entre com o segundo valor '))
soma = a + b
subtracao = a - b
mutiplicacao = a * b
divisao = a / b
resto = a % b
potencia = a ** b

print('soma:{}'.format(soma))
# Passa o resultado para uma string
print('Multiplcação:'+str(mutiplicacao))
print('Divisao:'+ str(divisao))
print('Resto da divisão = '+ str(resto))
print('Subtração = '+str(subtracao))
# precisa manter mesma ordem
print('Soma: {}. Subtração {}. Potência 10⁵ {} '.format(soma, subtracao, potencia))
# Não precisa mater a mesma ordem
print('Soma: {soma}. Subtraçaão: {subtracao}. Potência 10⁵: {potencia} '.format(soma=soma, subtracao=soma, potencia=potencia))

print('Soma: {}.'
      '\nSubtração: {}'
      '.\nPotência 10⁵: {} '.format(soma,
                                    subtracao, potencia))
x = '3'
soma2 = int(x) + 1
print('soma2=', soma2)
