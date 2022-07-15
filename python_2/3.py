



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = input()
    a = s.find('"')
    b = s.find('"', a+1)
    print(s[a+1:b])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
