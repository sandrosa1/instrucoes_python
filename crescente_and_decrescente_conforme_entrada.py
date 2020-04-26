decrescente = True
anterior = int(input("Digite o primeiro numero"))# recebe a primeira variavel fora do ciclo para funcionamento do while

valor= 1 # recebe valor um para incio

while valor != 0 and decrescente:
    valor = int(input("Digite o proximo numero"))
    if valor > anterior:
        decrescente = False
    anterior = valor
if decrescente:
    print ("A sequencia esta em ordem crescente! :-)")
else:
    print("A sequecia esta decrecente! :-( ")
