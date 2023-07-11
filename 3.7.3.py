def main():
    pass


if __name__ == "__main__":
    main()
    word_count = int(input())
    word_list = []
    misspell_list = {}
    for i in range(word_count):
        word = str(input()).lower()
        word_list.append(word)

    string_count = int(input())
    for j in range(string_count):
        sentence = str(input()).lower().split()
        sentence = list(sentence)
        for n in sentence:
            if n not in word_list:
                misspell_list[n] = 0
    for key in misspell_list:
        print(key)
