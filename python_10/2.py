def func(s):
    return round(9./5.*s +32)
import numpy as np
import pandas as pd
fin = open('input.csv')
arr = pd.read_csv('input.csv')
fin.close()
arr['temperature_f'] = arr["temperature_c"].apply(func)
fout = open('output.txt','w')
arr.to_csv('output.csv')
fout.close()
