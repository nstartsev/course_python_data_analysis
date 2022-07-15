
import numpy as np

fin = open('input.txt')

arr = []

for line in fin:
    tmp_arr = line.split()
    for elem in tmp_arr:
        arr.append(float(elem))
fin.close()
float_arr = np.array(arr, dtype = int)
fout = open('output.txt', 'w')
med = np.median(float_arr)
mean = np.mean(float_arr)
std = np.std(float_arr)
fout.write("{:.2f} {:.2f} {:.2f}".format(med, mean, std))
fout.close()
