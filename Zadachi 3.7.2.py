ishodn = str(input())
konechn = str(input())
shifrov = str(input())
rashifr = str(input())
a = list(ishodn)
b = list(konechn)
c = list(shifrov)
d = list(rashifr)
kod = {}
kod1 = {}
x = 0
n = 0
l = 0
n1 = 0
for char in range(len(ishodn)):
    kod[ishodn[x]] = konechn[x]
    x += 1
for char1 in range(len(konechn)):
    kod1[konechn[l]] = ishodn[l]
    l += 1
for i in shifrov:
    if i in kod:
        c[n] = kod[i]
        n += 1
for j in rashifr:
    if j in kod1:
        d[n1] = kod1[j]
        n1 += 1
print(''.join(c))
print(''.join(d))

