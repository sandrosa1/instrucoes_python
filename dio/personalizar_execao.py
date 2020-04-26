class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True: # vai sempre perguntar
    try:
        x = int(input('Entre com numero de 0 a 10\n'))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0
            raise  InputError('Nota não pode ser menor que 0')
        break # se Não der erro vai parar
    except ValueError:  #se der erro cai no tratamento
        print('Valor invalido. Digite apenas numeros')
    except InputError as ex:
        print(ex)
