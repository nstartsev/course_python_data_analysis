ar = input().split()
arr1 = list(map(float, ar))
b1 = arr1[0]
q = arr1[1]
a = arr1[2]
n = 1
bn = b1
while bn <= a:
    bn *= q
    n += 1
print(n)
