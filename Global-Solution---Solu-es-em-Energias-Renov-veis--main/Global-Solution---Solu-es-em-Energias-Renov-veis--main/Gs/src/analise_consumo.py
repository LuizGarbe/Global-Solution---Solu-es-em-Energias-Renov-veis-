import os
import pandas as pd
import numpy as np

def load_csv():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    csv_path = os.path.join(base, 'data', 'consumo_sample.csv')
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Arquivo CSV não encontrado: {csv_path}")
    df = pd.read_csv(csv_path, parse_dates=['timestamp'])
    return df

def stats(df):
    s = {}
    s['media'] = df['kW'].mean()
    s['mediana'] = df['kW'].median()
    s['pico'] = df['kW'].max()
    s['minimo'] = df['kW'].min()
    s['desvio_padrao'] = df['kW'].std()
    s['p25'] = np.percentile(df['kW'], 25)
    s['p75'] = np.percentile(df['kW'], 75)
    s['qtd_amostras'] = len(df)
    return s

def main():
    df = load_csv()
    s = stats(df)
    print('--- Estatísticas ---')
    print(f"Quantidade de amostras: {s['qtd_amostras']}")
    print(f"Média: {s['media']:.3f} kW")
    print(f"Mediana: {s['mediana']:.3f} kW")
    print(f"Pico (máx): {s['pico']:.3f} kW")
    print(f"Mínimo: {s['minimo']:.3f} kW")
    print(f"Desvio padrão: {s['desvio_padrao']:.3f}")
    return df, s

if __name__ == '__main__':
    main()
