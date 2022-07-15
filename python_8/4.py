
import numpy as np

fin = open('input.csv')
arr = []
for line in fin:
    tmp_arr = line.rstrip().split(',')
    arr.append(tmp_arr)

fin.close()

float_arr = np.array(arr, dtype = float)

for i in range(len(float_arr)):
    for j in range(len(float_arr[i])):
        if (i+j) % 2 != 0 :
            float_arr[i][j] /= 2
fout = open('output.csv', 'w')


for i in range(len(float_arr)):
    for j in range(len(float_arr[i])):
        if i == len(float_arr)-1:
            if j == len(float_arr[i])-1:
                fout.write(str("%g" % float_arr[i][j]))
            else:
                fout.write(str("%g" % float_arr[i][j] + ','))
        else:
            if j == len(float_arr[i])-1:
                fout.write(str("%g" % float_arr[i][j] + '\n'))
            else:
                fout.write(str("%g" % float_arr[i][j] + ','))
fout.close()
