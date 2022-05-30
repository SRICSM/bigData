import pandas as pd

df = pd.read_csv('./2.csv')
print(df)
print(df.pivot(index=['Name', 'Title'], columns='type'))

