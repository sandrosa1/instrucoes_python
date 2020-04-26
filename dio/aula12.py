import requests
def retorna_dados_cep(cep):

    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.text)
    print(type(response.text))
    print(response.json())
    print(type(response.json()))
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_responce(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    #retorna_dados_cep('18135310')
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon)
    #print(dados_pokemon['sprites']['front_shiny'])
    response = retorna_responce() # tras o html da pagina
    print(response)