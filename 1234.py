line = input()
l = len(line)
num = ''
letter = ''
for char in line:
    if char.isalpha():
        if num != '':
            num = int(num)
            print(letter*num)
        letter = char
        num = ''
    if char.isdigit():
        num = num + char
print(letter*int(num))
#12345



