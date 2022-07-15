file = open('med_research.txt')
a = []
for line in file:
    a.append(line.split())
file.close()
b = [[a[k][i] for k in range(len(a))] for i in range(len(a[0]))]
file = open('output.txt','w')
for i in range(len(b)):
    file.write(' '.join(b[i]))
    file.write('\n')
file.close()
