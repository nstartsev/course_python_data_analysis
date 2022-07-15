file = open('input.txt')
names = []
gender = []
for line in file:
    names.append(line.split()[1])   
    gender.append(line.split()[2])
sortnames = sorted(zip(names, gender), key = lambda pairs: pairs[0] , reverse = False)

set_male = []
set_female = []
for pair in sortnames:
    if pair[1] == 'male':
        set_male.append(pair[0])
    if pair[1] == 'female':
        set_female.append(pair[0])


filtered = list(set(set_male) & set(set_female))
if filtered == []:
    print(0)
else:
    sortnames = sorted(filtered, key = lambda elem: len(elem) , reverse = False)
    res = ''
    for i in range(len(filtered)):
        if i == len(filtered) - 1:
            res = res + sortnames[i]
        else:
            res = res + sortnames[i] + '\n'   
    print(res)
