import os
import pandas as pd

def overall_describe():
    try:
        df = pd.read_csv('./data/raw_0.csv')
        consumo = df['Consumo']

        mediana = consumo.median()
        moda = consumo.mode()[0]
        media = consumo.mean()
        max = consumo.max()
        min = consumo.min()

        
        show = {
            "Mediana": [mediana],
            "Moda": [moda],
            "Media": [media],
            "Maximo": [max],
            "Minimo": [min]

        }
        
        print(pd.DataFrame(show))
        path = './data/processed/overall_average.csv'
        if not os.path.exists(path):
            pd.DataFrame(show).to_csv(path, index=False)
    except Exception as e:
        print(f'Erro na descrição: {e}')
        return False
overall_describe()