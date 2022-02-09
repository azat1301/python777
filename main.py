import csv

#import end as end

import pandas as pd
import re

df = pd.read_csv(r'C:\Users\Azat\Desktop\777-auto-input\data1.csv', encoding='utf-8')

for index, row in df.iterrows():
    if (((row['col 5'] == '切削 品') | (row['col 5'] == 'そ の 他 ( 製'))) & (row['col 8'] == '3'):
        buhinbango = df.iloc[index-1]['col 3']
        print(buhinbango)






# for i in i, i < 40, i + 2):
#     i = 1, 3, 5,
#     row = df[i]
#
#     if row['col 5'] == '切削 品' & row['col 8'] == '3':
#         buhinbango = row[i - 1]['col 3']
#         print(i)
