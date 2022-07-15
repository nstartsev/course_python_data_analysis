
if __name__ == '__main__':
    data = []
    file = open('input.txt')
    for line in file:
        data.append( line.split() )

    for line in data:
        for i in range(len(line)):
            print(line[i][::-1], end=' ')
