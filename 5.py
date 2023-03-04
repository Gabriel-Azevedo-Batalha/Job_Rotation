if __name__ == "__main__":
    print("Insira uma string")
    word = input()
    reversedWord = ""
    # print(word[::-1])
    for c in word:
        reversedWord = c + reversedWord
    print(reversedWord)