import pandas as pd
import numpy as np

def spread_overral():
    try:
        df =  pd.read_csv('./data/raw/raw_0.csv')
        consumo = df['Consumo']

        deviation = np.std(consumo, ddof=1)
        p25 = np.percentile(consumo, 25)
        p50 = np.percentile(consumo, 50)
        p75 = np.percentile(consumo, 75)

        show = {'Desvio': [deviation], 'P25': [p25], 'P50': [p50], 'P75': [p75]}

        print(pd.DataFrame(show))
        pd.DataFrame(show).to_csv('./data/processed/spread_overral.csv', index=False)
    except Exception as e:
        print(f'Erro ao calcular o desvio: {e}')
        return False

