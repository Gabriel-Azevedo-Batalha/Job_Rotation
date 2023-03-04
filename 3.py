import json

def parseJSON(file):
    with open(file) as f:
        parsedJson =  json.loads(f.read())
    return parsedJson

if __name__ == "__main__":
    dados = parseJSON('dados.json')

    #print(dados)

    menor = None
    maior = None
    total = 0
    for dia in dados:
        total += dia['valor']
        if menor == None or dia['valor'] < menor:
            menor = dia['valor']
        if maior == None or dia['valor'] > maior:
            maior = dia['valor']
    media = total/len(dados)

    total = 0
    for dia in dados:
        if dia['valor'] >= media:
            total += 1 

    print("1)", menor)
    print("2)", maior)
    print("3)", total)
