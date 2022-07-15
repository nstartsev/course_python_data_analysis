
import numpy as np

fin = open('input.csv')
arr = []
for line in fin:
    tmp_arr = line.rstrip().split(',')
    arr.append(tmp_arr)

fin.close()

float_arr = np.array(arr, dtype = int)

s1 = 0
s2 = 0
for str in float_arr:
    sr = np.std(str)
    if sr > 4 :
        s2 += 1
    else:
        s1 += 1

fout = open('output.txt', 'w')
if (s1 > s2):
    fout.write('1')
else:
    fout.write('2')

fout.close()
