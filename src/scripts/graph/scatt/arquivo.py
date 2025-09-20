import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def overall_scatt(columns):
    try:
        df = pd.read_csv('./data/raw/raw_0.csv')
        consumo = df['Consumo']
        col = df[columns]

        plt.figure(figsize=(8,6))
        sns.scatterplot(x=col, y=consumo, color='red', alpha=0.6)
        plt.xlabel(columns)
        plt.ylabel('Consumo (MW/h)')
        plt.title(f'Dispersão: Consumo x {columns}')
        plt.yscale('log')
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.savefig('./reports/scatt_consumo.png')
        plt.show()
    except Exception as e:
        print(f'Erro ao gerar scatter: {e}')
        return False
