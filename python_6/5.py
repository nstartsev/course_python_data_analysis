file = open('input.txt')
names = []
for line in file:
    names.append(line.split()[1])    
new = list(set(names))
sortnames = sorted(new, key = lambda elem: len(elem) , reverse = False)

new = list(set(sortnames))
res = ''
for i in range(len(new)):
    if i == len(new) - 1:
        res = res + sortnames[i]
    else:
        res = res + sortnames[i] + '\n' 
        
print(res)
