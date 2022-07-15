a = input()
fr = []
arr = []
for num in range(10):
    freq = a.count(str(num))
    fr.append(freq)
    arr.append(num)    
s = sorted(zip(arr, fr), key=lambda pair: pair[1], reverse =  True )

print(s[0][0])
