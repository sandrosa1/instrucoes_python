
lista = [1, 10]
arquivo = open('teste.txt','r')
try:
    texto = arquivo.read()
    divisão = 10 /1
    numero = lista[1]
    x = lista
except ZeroDivisionError:
    print('Não e possivel realizar uma divisão por zero')
except IndexError:
    print('Erro por acessar um indice invalido na lista')
except BaseException as ex:
    print('Erro desconhecido. Erro {}'.format(ex))
else:
    print('Executa quando não tenho erro')
finally:
    print('Sempre executa')
    print('Fechado arquivo')
    arquivo.close()