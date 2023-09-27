a = open('pr.txt').readline()

b = a.lower()
k = 0
for i in range(len(b)):
    if b[i] in 'eyuioa':
        k += 1
print(k)