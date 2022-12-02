#https://stackoverflow.com/questions/55955242/the-result-of-dataframe-mean-is-incorrect
#Trying to understand a bug that I had encountered (for another application) using pandas .mean()

import pandas as pd
import numpy as np

#df = pd.DataFrame(
#    np.array([['A', 1, 2, 3], ['A', 4, 5, np.nan], ['A', 7, 8, 9], ['B', 3, 2, np.nan], ['B', 5, 6, np.nan], ['B',5, 6, np.nan]]), 
#    columns=['a', 'b', 'c', 'd']
#)

df = pd.DataFrame(
    [['A', 1, 2, 3], ['A', 4, 5, np.nan], ['A', 7, 8, 9], ['B', 3, 2, np.nan], ['B', 5, 6, np.nan], ['B',5, 6, np.nan]],
    columns=['a', 'b', 'c', 'd']
)

mean1 = df[df.a == 'A'].c.mean()
mean2 = df[df.a == 'B'].c.mean()

median1 = df[df.a == 'A'].c.median()
median2 = df[df.a == 'B'].c.median()

print(mean1)
print(mean2)

print(median1)
print(median2)

print(df[df.a == 'B'].c)
print(df[df.a == 'B'].c.mean())