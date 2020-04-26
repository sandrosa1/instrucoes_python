
i = int(input("quantidade a ser somada ")) # especifica quantidade de entradas
valor = 1 # declarando a variavel
cont = 1 # cont recebeu 1 por que i e menor igual, se i fosse menor, cont receberia 0
soma = 0 # declarando variavel
while cont <= i: # esta linha determina ate quando o ciclo vai se repetir
    valor = int(input("digite o valor para ser somado "))
    soma = valor + soma
    cont = cont + 1
   
print ("A soma dos",i," valores é:",soma)
