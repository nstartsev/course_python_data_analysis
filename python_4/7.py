labels = "Месяц!Сумма на вкладе!Начисление".split('!')
ar = input().split()
amount = int(ar[0])
period = int(ar[1])
rate = float(ar[2])
inc = amount * rate/100.0/12.0
amount += inc
n = 1
data = []
while n <= period * 12:
    data.append([n, round(amount, 2), round(inc, 2)])
    n += 1
    inc = amount * rate / 100 / 12
    amount += inc
with open('output.csv', 'w') as csv_file:
    print(','.join(labels), file=csv_file)
    for row in data:
        print(f"{row[0]},{row[1]:0.2f},{row[2]:0.2f}", file=csv_file)
