valor = int(input("Digite "))# entrada de dados com numero inteiro, float da erro na soma
soma = 0 # declara variavel
while valor != 0: # enquanto diferente de zero, repete calculo
    soma = (valor % 10) + soma
    valor = valor // 10

print (soma)
          
