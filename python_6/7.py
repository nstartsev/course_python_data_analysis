file = open('input.txt')
names = []
for line in file:
    names.append(line.split() [1])
set_names = list(set(names))
freq_name = []
for name in set_names:
    freq_name.append(names.count(name))
sort = sorted(zip(set_names, freq_name), key = lambda pair: pair[1], reverse = True)
res = ''
for i in range(len(sort)):
    if i == len(sort) - 1:
        res = res + sort[i][0] + ' - ' + str(sort[i][1])
    else:
        res = res + sort[i][0] + ' - ' + str(sort[i][1]) + '\n'       
print(res)
