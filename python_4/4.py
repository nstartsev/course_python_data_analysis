from fractions import Fraction as fr

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
fra = fr(a[0], a[1])
frb = fr(b[0], b[1])
frc = fr(c[0], c[1])
res = frb/fra + frb/(fra + frc) - frc/(frc - fra)
print(round(float(res), 4))
