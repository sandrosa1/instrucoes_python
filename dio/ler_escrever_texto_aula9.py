# w escreve na primeira linha
# a escreve na segunda linha e atualiza

def escrever_arquivo(texto):
    arquivo = open('teste.txt','w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open(nome_arquivo,'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquvo = open(nome_arquivo, 'r')
    aluno_nota = arquvo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media =[]
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda  notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    import shutil # voce pode importar global
    shutil.copy(nome_arquivo,'aqui vc insere o destino')

def move_arquivo(nome_arquivo):
    import shutil
    shutil.move(nome_arquivo, 'Lugar para onde deseja mover')


if __name__ == '__main__':
    move_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Primeira linha\n')
    #aluno = 'Felipe, 10, 9, 9, 8\n'
    #atualizar_arquivo('notas.txt',aluno)
    #ler_arquivo('teste.txt')