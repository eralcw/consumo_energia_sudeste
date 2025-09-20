import pandas as pd
import matplotlib.pyplot as plt


def overall_hist():
    try: 
        df = pd.read_csv('./data/raw_0.csv')
        consumo = df['Consumo']
        fig, ax = plt.subplots(figsize=(8,6))

        ax.hist(consumo, bins=10, color='skyblue', edgecolor='red')
        ax.set_xlabel('Consumo MW/h')
        ax.set_ylabel('Frequência')
        ticks = ax.get_xticks()
        labels = [f'{t/1000000:.1f}M' for t in ticks]
        ax.set_xticks(ticks)
        ax.set_xticklabels(labels)
        plt.savefig('./reports/hist_consumo.png')
        plt.show()
    except Exception as e:
        print(f'Erro ao gerar histograma: {e}')
        return False