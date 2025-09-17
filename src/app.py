import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geobr
import geopandas as gpd
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

def merge_consumo_region():
    try:
        df = pd.read_csv('./data/raw_0.csv')
        print('Regiões no CSV:', df['Regiao'].unique())
  
        df['Regiao'] = ( df['Regiao']
                        .str.strip()
                        .str.lower()
                        .str.replace(' ', '-', regex=True)
        )
        consumo_regiao = df.groupby('Regiao')['Consumo'].mean().reset_index()

        region = geobr.read_region()
        print('Regiões no geobr:', region['name_region'].unique())
        region["name_region"] = ( region['name_region']
                        .str.strip()
                        .str.lower()
                        .str.replace(' ','-', regex=True)
        )

    
        merged = pd.merge(region, consumo_regiao, left_on='name_region', right_on='Regiao', how='left')
        print('Regiões padronizadas no CSV:', consumo_regiao['Regiao'].unique())
        print('Regiões padronizadas no geobr:', region['name_region'].unique())
        return merged
    except Exception as e:
        print(f'Erro ao fazer merge: {e}')
        return False

def consumo_regiao_mean():
    try:
        df = pd.read_csv('./data/raw_0.csv')
        merged = merge_geobr_region()

        gdf = gpd.GeoDataFrame(merged, geometry='geometry')

        fig, ax = plt.subplots(figsize=(10,8))
        gdf.plot(column='Consumo', cmap='OrRd',ax=ax, legend=True)
        ax.set_title('Consumo de Energia por Região')
       
        plt.axis('off')
        plt.savefig('./reports/mapa_consumo_regiao.png')
        plt.show()
    except Exception as e:
        print(f'Erro no merged: {e}')
        return False

def overall_describe():
    try:
        df = pd.read_csv('./data/raw_0.csv')
        consumo = df['Consumo']
        mediana = consumo.median()
        moda = consumo.mode()[0]
        
        show = {
            "Median": [mediana],
            "Mode": [moda]
        }
        
        print(pd.DataFrame(show))
        print(consumo.describe())

    except Exception as e:
        print(f'Erro na descrição: {e}')
        return False
    

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

def corr_raw_0():
    df = pd.read_csv('./data/raw_0.csv')
    plt.figure(figsize=(8,6))
    numeric_df = df.select_dtypes(include='number')
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title('Matriz de correlação da tabela Raw_0')
    plt.show()


def overall_scatt(columns):
    try:
        df = pd.read_csv('./data/raw_0.csv')
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

if __name__== "__main__":
    overall_scatt('Consumidores')