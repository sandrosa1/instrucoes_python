from datetime import date ,time, datetime, timedelta


def trabalhandoComDate():
    dataAtual = date.today()
    dataAtualStr = dataAtual.strftime('%A, %B, %Y')
    print(dataAtual) # aqui imprimi a data atual
    print(dataAtual.strftime('%d/%m/%Y')) # aqui no padrão brasileiro
    print(dataAtual.strftime('%A/%d/%B/%Y')) # aqui outro formato
    print(type(dataAtualStr))  # aqui vc verifica que a data converteu para string
    print(type(dataAtual))  # aqui ela e uma typo date


def trabalhandoComTime():
    horario = time(hour=15, minute=10, second=30)
    horarioStr = (horario.strftime('%H:%M:%S'))
    print(type(horario))
    print(horario)
    print(type(horarioStr))
    print(horarioStr)

def trabalhandoComDateTime():
    dataAtual =datetime.now()
    print(dataAtual)
    print(dataAtual.strftime('%H:%M'))
    print(dataAtual.strftime('%c'))
    print(dataAtual.month)
    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta','Sabádo','Domingo')
    print(tupla[dataAtual.weekday()])
    dataCriada = datetime(2018, 6, 20, 15, 30,20)
    print(dataCriada)
    datastr = '01/11/2019'
    dataConverte = datetime.strptime(datastr, '%d/%m/%Y')
    print(type(dataConverte))
    novaData = dataConverte - timedelta(days=365)
    print(novaData)



if __name__ == '__main__':
    #trabalhandoComDate()
    #trabalhandoComTime()
    trabalhandoComDateTime()
