from itertools import product
a = '01'
b = '01'
c = '01'

res = ""
for p in product(a, b, c):
    x1 = int(p[0])
    x2 = int(p[1])
    x3 = int(p[2])

    val = ((not x1) and x2 and (not x3))or((not x1) and x2 and x3)or(x1 and (not x2) and (not x3))
    s = ''.join(p)
    if val == 1:
        if (x1 == 1 and x2 ==1 and x3 == 1):
            res = res + "True True True"
        else:
            if x1 == 1:
                res = res + "True" + " "
            else:
                res = res + "False" + " "
            if x2 == 1:
                res = res + "True" + " "
            else:
                res = res + "False" + " "
            if x3 == 1:
                res = res + "True" + " "
            else:
                res = res + "False" + " "
            res = res + '\n'
            
#    print(bool(x1),bool(x2),bool(x3))
print(res)
