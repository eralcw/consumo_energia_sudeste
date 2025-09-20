import pandas as pd
import matplotlib.pyplot as plt
import geopandas
import geobr



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
        merged = merge_consumo_region()

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