import os
import pandas as pd

def overall_describe():
    try:
        df = pd.read_csv('./data/raw/raw_0.csv')
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


def overall_group_average(coluna):
    try:
        df = pd.read_csv("./data/raw/raw_0.csv")
        show = (
            df.groupby(coluna)["Consumo"].agg(
                Quantidade="count",
                Media="mean",
                Mediana="median",
                Moda=lambda x: x.mode()[0] if not x.mode().empty else None,
                Maior_Consumo="max",
                Menor_Consumo="min",
            )
            .reset_index()
        )
        print(show)
        path = f"./data/processed/overall_{coluna.lower()}_average.csv"
        if not os.path.exists(path):
            show.to_csv(path, index=False)
    except Exception as e:
        print(f"Erro ao calcular estatísticas por {coluna}: {e}")
        return False

def overall_region_class_average():
    try:
        df = pd.read_csv('./data/raw/raw_0.csv')
        show = (
            df.groupby(['Regiao', 'Classe'])['Consumo']
            .agg(
                Quantidade='count',
                Media='mean',
                Mediana='median',
                Moda=lambda x : x.mode()[0] if not x.mode().empty else None,
                Maior_Consumo='max',
                Menor_Consumo='min',
            )
            .reset_index()
        )
        print(show)
        path = './data/processed/overall_region_class_average.csv'
        if not os.path.exists(path):
            show.to_csv(path, index=False)
    except Exception as e:
        print(f'Erro ao calcular overall por Regiao e Classe: {e}')
        return False

if __name__=='__main__':
    overall_region_class_average()