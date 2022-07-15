fin = open('input.csv')
arr = []
n = 0
k = 0
for line in fin:
    if(n > 0):
        arr.append(line.rstrip().split(","))
        a = float(arr[n-1][0])
        b = float(arr[n-1][1])
        c = float(arr[n-1][2])
        if (a + b > c) and (a + c > b) and (b + c > a):
            k = k + 1
    n = n + 1
fin.close()

fout = open('output.txt','w')
fout.write(str(k))
fout.close()
