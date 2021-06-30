import csv
import pandas as pd
import numpy as np

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
data = pd.read_csv('./dataset/545966509.csv')
highlist=data.nlargest(4, 'Like')
print(highlist)
counter=data.value_counts('Uname')
print(counter.index[0], counter[0])
print(data.shape[0])
print(data['Uid'].unique().shape[0])
print(data.shape[0]/data['Uid'].unique().shape[0])
counter=data.value_counts('Content')
print(counter.index[0], counter[0])
