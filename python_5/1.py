file = open('weights.txt')
a = []
for line in file:
    a.append(line.split())
for i in range(len(a)):
    a[i][1] = float(a[i][1])
b = sorted(a, key=lambda x: x[1], reverse=True)
file.close()
file = open('team.txt', 'w')
for i in range(0,22,2):
    res = b[i][0] + ' ' + str(b[i][1]) + '\n'
    file.write(res)
for i in range(1,22,2):
    res = b[i][0] + ' ' + str(b[i][1]) + '\n'
    file.write(res)
file.close()
