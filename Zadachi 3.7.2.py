def encrypt(original_text, final_text):
    original_text = list(original_text)
    final_text = list(final_text)
    kod = {}
    kod1 = {}
    x = 0
    l = 0
    for char in range(len(original_text)):
        kod[original_text[x]] = final_text[x]
        x += 1
    for char1 in range(len(final_text)):
        kod1[final_text[l]] = original_text[l]
        l += 1
    return kod, kod1


def decrypt(encrypted_text, decrypted_text, kod, kod1):
    encrypted_text = list(encrypted_text)
    decrypted_text = list(decrypted_text)
    n = 0
    n1 = 0
    for i in encrypted_text:
        if i in kod:
            encrypted_text[n] = kod[i]
            n += 1
    for j in decrypted_text:
        if j in kod1:
            decrypted_text[n1] = kod1[j]
            n1 += 1
    return encrypted_text, decrypted_text


def print_result(encrypted_text, decrypted_text):
    print(''.join(encrypted_text))
    print(''.join(decrypted_text))


def main():
    original_text = str(input())
    final_text = str(input())
    kod, kod1 = encrypt(original_text, final_text)
    encrypted_text = str(input())
    decrypted_text = str(input())
    encrypted_text1, decrypted_text1 = decrypt(encrypted_text, decrypted_text, kod, kod1)
    print_result(encrypted_text1,decrypted_text1)


if __name__ == '__main__':
    main()
