import numpy as np

fin = open('input.csv')
arr = []
for line in fin:
    tmp_arr = line.rstrip().split(',')
    arr.append(tmp_arr)

fin.close()

float_arr = np.array(arr, dtype = float)
day = []
sr_arr = []
for j in range(len(float_arr[0])):
    for i in range(len(float_arr)):
        day.append(float_arr[i][j])
    sr = np.mean(day)
    sr_arr.append(sr)
    day = []
maxx = np.min(sr_arr)
ind = list(sr_arr).index(maxx)
fout = open('output.txt', 'w')
fout.write(str(ind+1))
fout.close()
