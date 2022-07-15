from functools import reduce
file = open('the_calls.txt')
a = []
for line in file:
    line = line.rstrip('\n')
    a.append(line.split('\t'))
file.close()
a = sorted(a, key=lambda x: x[2])
a_count = reduce(
    lambda count, item: count + (item[2] == 'A'), a, 0)
b = sorted(a[0:a_count], key=lambda x: int(x[1]), reverse=True)
c = sorted(a[a_count:len(a)], key= lambda x: int(x[1]), reverse=True)

file = open('calls.txt','w')
for line in b:
    file.write('\t'.join(line))
    file.write('\n')
for line in c:
    file.write('\t'.join(line))
    file.write('\n')
file.close()
