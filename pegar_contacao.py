import requests as rq

def pegar_contacao_moeda(moeda_origem, moeda_destino):
    link = f'https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}'
    requisicao = rq.get(link)

    cotacao = requisicao.json()[f'{moeda_origem}{moeda_destino}']['bid']
    print(cotacao)
    return cotacao