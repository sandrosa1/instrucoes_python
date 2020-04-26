i = int(input("Quantidade de numeros a ser multiplicado ")) # especifica quantidade de entradas

valor = 1 # declarando a variavel
cont = 1 # cont recebeu 1 por que i e menor igual, se i fosse menor, cont receberia 0
produto =1 # o valor neutro para um produto e 1

while cont <= i: # esta linha determina ate quando o ciclo vai se repetir
    valor = int(input("digite o valor para ser somado "))
    produto = valor * produto
    cont = cont + 1
   
print ("A soma dos",i," valores é:",produto)
