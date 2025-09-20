import pandas as pd

from __pycache__.overall import *
from scripts.graph.hist.hist_overall import * 



def init_csv():
    try:
        for i in range(0, 10):
            df = pd.read_excel('./data/raw/raw.xlsx', sheet_name=i)
            df.to_csv(f'./data/raw_{i}.csv', index=False)
        return True
    except Exception as e:
        print(f'Erro: gerar csv {i}')
        return False



if __name__== "__main__":
  