
import requests


def converter(origem, destino, valor):
    url = f"https://economia.awesomeapi.com.br/last/{origem}-{destino}"
    requisicao = requests.get(url)
    if (requisicao.status_code == 200):
        dados = requisicao.json()
        cotacao = float(dados[origem + destino]["bid"])
        valor_final = valor * cotacao
        print(f"Hoje o valor {valor} em {origem} equivale a {valor_final} em {destino}.")
    else:
        print("Erro na requisição!")


origem = input("Digite a moeda de origem (Ex: USD): ").upper()
destino = input("Digite a moeda de destino (Ex: BRL): ").upper()
valor = float(input(f"Digite o valor em {origem}: "))

converter(origem, destino, valor)