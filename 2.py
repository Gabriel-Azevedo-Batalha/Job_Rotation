def isFibbonaci(num):
    seq = [0, 1]
    while seq[1] <= num:
        if num in seq:
            return True
        seq = [seq[1], seq[0]+seq[1]]
    return False

if __name__ == "__main__":
    print("Insira um número")
    num = int(input())
    if isFibbonaci(num):
        print("O número", num, "pertence a sequência de Fibbonaci")
    else:
        print("O número", num, "não pertence a sequência de Fibbonaci")