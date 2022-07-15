file = open('input.txt')
s = file.readline()
arr = s.split()
begin = 0
end = len(arr) - 1
mid = (begin + end)//2
tmp = int(arr[mid])

while tmp != 1415:
    if tmp < 1415:
        begin = mid
    elif tmp > 1415:
        end = mid
    mid = (begin + end)//2
    tmp = int(arr[mid])
print(mid)
