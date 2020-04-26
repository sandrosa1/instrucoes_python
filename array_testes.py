

def MinMax(temperaturas):
    print("A temperatura mínima foi: ", mínima(temperaturas), "C°")
    print("A temperatura máxima foi: ", máxima(temperaturas), "C°")

def máxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):  # i percore os elementos da array temps
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

def mínima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):  # i percore os elementos da array temps
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min



def teste_pontual(temp, valor_esperado):
    valor_calculado = mínima(temp)
    if valor_calculado != valor_esperado:
            print("O valor errado para array", temp)
            print ("Valor esperado: ", valor_esperado,". Valor calculado: " , valor_calculado )


def testa_mínima():
    print("Iniciando os testes")
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0], 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    teste_pontual([30, 27, 18, 33, 45, 38, 18, 19, 40, 41, 33, 33, 12, 14, 17], 12)
    teste_pontual([-1, -5, 29, -8, 30, -1], -8)
    print("Teste finalizados")
