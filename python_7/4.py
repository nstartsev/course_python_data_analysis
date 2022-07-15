import numpy as np
fin = open('input.txt')
fout = open('output.txt', 'w')
file = []
for line in fin:
    file = file + line.split()

first = float(file[0])
last = float(file[1])
days = int(file[2])
    
data = np.linspace(first, last, days)

for i in range(days):
    if (i + 1) % 7 == 1:
        data [i] = round(data[i]/3, 2)
    if (i + 1) % 7 == 5:
        data [i] = round(data[i]*2, 2)
    if (i + 1) % 7 != 1 and (i + 1) % 7 != 5:
        data [i] = round(data[i], 2)
    if i == days - 1:
        fout.write(str("%.2f" % data[i]))
    else:
        fout.write(str("%.2f" % data[i]) + '\n')
fout.close()
fin.close()
