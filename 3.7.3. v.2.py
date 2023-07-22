






def correct_words(word_count):
    word_list = []
    for i in range(word_count):
        word = str(input()).lower()
        word_list.append(word)
    return word_list


def test_words(word_list, string_count):
    misspell_list = {}
    for j in range(string_count):
        sentence = str(input()).lower().split()
        sentence = list(sentence)
        for n in sentence:
            if n not in word_list:
                misspell_list[n] = 0
    return misspell_list


def print_result(misspell_list):
    for key in misspell_list:
        print(key)



def main():
    word_list = correct_words(int(input()))
    misspell_list = test_words(word_list, int(input()))
    print_result(misspell_list)



if __name__ == "__main__":
    main()