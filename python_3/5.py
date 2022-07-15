
import itertools as it
if __name__ == '__main__':
    data = []
    file = open('studygroup.txt', 'r')
    for line in file:
        str = line.split()
    for x, y, z in it.combinations(str, 3):
        print("1:",x,"2:", y, "3:",  z, sep=' ', end='\n')
