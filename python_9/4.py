import numpy as np
fin = open('input.csv')

arr = []
name = []
n = 0
for line in fin:
    if n == 0:
        name.append(line.rstrip().split(","))
        l = len(line.rstrip().split(","))
    else:
        arr.append(line.rstrip().split(","))
    n = n + 1

place = []
mean = []
sum = 0.
for i in range(l):
    for j in range(n-1):
        place.append(float(arr[j][i]))
        sum += float(arr[j][i])
    mean.append(np.mean(place))
    place = []

maximum = np.max(mean)
index = list(mean).index(maximum)


fin.close()

fout = open('output.txt', 'w')
if (sum >= 8000000):
    fout.write("1 ")
    fout.write(name[0][index])
else:
    fout.write('0')
fout.close()
