if __name__ == '__main__':
    data = []
    file = open('input.txt')
    for line in file:
        data.append( line.strip() )
    filtered_data = list(filter(lambda x: 'Ñ‘' in x, data))
    for s in filtered_data:
        print(s)
