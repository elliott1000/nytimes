import string
alets = list(string.ascii_lowercase)
with open('words.txt','r') as file:
    words = file.read().split('\n')
letters = input().split(' ')
must = letters[0]
ww4 = []
for i in range(len(words)):
    if len(words[i]) >= 4:
        ww4.append(words[i])
wwm = []
for i in range(len(ww4)):
    if must in ww4[i]:
        wwm.append(ww4[i])
bl = []
for i in range(len(alets)):
    for r in range(len(letters)):
        if letters[r] == alets[i]:
            break
    else:
        bl.append(alets[i])
fin = []
for i in range(len(wwm)):
    for r in bl:
        if r in wwm[i]:
            break
    else:
        fin.append(wwm[i])
for i in fin:
    print(i)
input()
