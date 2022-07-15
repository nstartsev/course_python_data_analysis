file = open('input.txt')
names = []
idd = []
for line in file:
    names.append(line.split()[1])
    idd.append(line.split()[0])
pairs = sorted(zip(idd, names), key = lambda pair: pair[0], reverse = True)
set_names = list(set(names))
filtered_names = sorted(set_names, key = lambda name: len(name), reverse = False)
res = ''
for name in filtered_names:
    mass_id = []
    for pair in pairs:
        if name == pair[1]:
            mass_id.append(pair[0])
    mass_id.sort()
    
    res = res + name + ': '
    for i in range(len(mass_id)):
        if i == len(mass_id) - 1:
            res = res + mass_id[i] + '\n'
        else:
            res = res + mass_id[i] + ', '    
print(res)
    
