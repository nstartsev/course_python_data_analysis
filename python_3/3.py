if __name__ == '__main__':
    data = []
    file = open('input.txt')
    for line in file:
        data.append( line.strip() )
    for s in data:
        arr = s.split()
        arr_new = arr[::2]
        for elem in arr_new:
            print(elem, end=' ')
        print()
