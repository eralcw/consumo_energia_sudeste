import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_0 = pd.ExcelFile('./data/raw.xlsx').sheet_names
print(len(df_0))

for i in range(len(df_0)):
    df = pd.read_excel('./data/raw.xlsx', sheet_name=i)
    df.to_csv(f'./data/raw_{i}.csv', index=False)