file = open('poe_unpublished.txt')
a = []
for line in file:
    a.append(line.split())
file.close()
a = sorted(a, key= lambda x: len(x))
for i in range(len(a)):
    a[i] = sorted(a[i], key= lambda x: len(x))
file = open('poe_decode_attempt.txt','w')
for line in a:
    file.write(' '.join(line))
    file.write('\n')
