import numpy as np
import pandas as pd
fin = open('input.csv')
arr = pd.read_csv('input.csv')
fin.close()
arr.dropna(subset = ['name'], axis=0, inplace=True)
arr.fillna(np.mean(arr['score']), inplace = True)
print(arr)
fout = open('output.txt','w')
arr.to_csv('output.csv')
fout.close()
