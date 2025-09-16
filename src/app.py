import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def init_csv():
    try:
        for i in range(0, 10):
            df = pd.read_excel('./data/raw.xlsx', sheet_name=i)
            df.to_csv(f'./data/raw_{i}.csv', index=False)
        return True
    except Exception as e:
        print(f'Erro: gerar csv {i}')
        return False
    


def numbers_col():
    df = pd.read_csv('./data/raw_0.csv')
    numeric_cols =df.select_dtypes(include='number').columns
    for col in numeric_cols:
        plt.figure(figsize=(6,1))
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot de {col}')
        plt.show()

#consumo = df_0['Consumo']
#print(consumo)
#consumo_media = consumo.mean()
#print(consumo_media)
#consumo_mediana = consumo.median()
#print(consumo_mediana)
#consumo_moda = consumo.mode()
#print(consumo_moda)



def hist_consumo():
    df = pd.read_csv('./data/raw_0.csv')
    consumo = df['Consumo']
    fig, ax = plt.subplots(figsize=(6,8))

    ax.hist(consumo, bins=12)
    ax.set_xlabel('Consumo MW/h')
    ax.set_ylabel('Frequencia')
    plt.show()


if __name__== "__main__":
    pass