import numpy as np

fin = open('input.csv')
arr = []
for line in fin:
    tmp_arr = line.rstrip().split(',')
    arr.append(tmp_arr)

fin.close()

float_arr = np.array(arr, dtype = int)
fout = open('output.txt', 'w')

s1 = 0
s2 = 0
s3 = 0

for string in float_arr:
    s1 += string[0]
    s2 += string[1]
    s3 += string[2]
maxs = max(s1, s2, s3)
s = [s1, s2, s3]
ind = s.index(maxs)
fout.write(str(ind+1))
fout.close()
