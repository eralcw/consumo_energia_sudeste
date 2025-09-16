import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def create_raw_csv_files():
    for i in range(0, 10):
        df = pd.read_excel('./data/raw.xlsx', sheet_name=i)
        df.to_csv(f'./data/raw_{i}.csv', index=False)

df_0 = pd.read_csv('./data/raw_0.csv')

consumo = df_0['Consumo']
print(consumo)
consumo_media = consumo.mean()
print(consumo_media)
consumo_mediana = consumo.median()
print(consumo_mediana)
consumo_moda = consumo.mode()
print(consumo_moda)
    def hist_consumo:
fig, ax = plt.subplots(figsize=(6,8))

ax.hist(consumo, bins=12)
ax.set_xlabel('Consumo MW/h')
ax.set_ylabel('Frequencia')
plt.show()


if __name__== "__main__":
    pass