
if __name__ == "__main__":
    with open("faturamento") as f:
        linhas = f.read().split('\n')

    faturamento = {}
    total = 0
    for linha in linhas:
        temp = linha.split()
        valor = ""
        for c in temp[2][2:]:
            if c != '.':
                if c == ',':
                    valor += '.'
                else:
                    valor += c
        faturamento[temp[0]] = float(valor)
        total += faturamento[temp[0]]
    print(faturamento)

    for estado, valor in faturamento.items():
        print("Estado:", estado, "- Participação(%):", 100*valor/total)
