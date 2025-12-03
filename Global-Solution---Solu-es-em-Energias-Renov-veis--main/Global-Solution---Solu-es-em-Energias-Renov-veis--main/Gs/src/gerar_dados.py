import os
import numpy as np
import pandas as pd
from datetime import datetime

def main():
    # Gera 1440 pontos (1 dia, 1 por minuto)
    idx = pd.date_range(start=datetime(2025,1,1), periods=1440, freq='min')
    consumo = 0.5 + 0.35 * np.sin(np.linspace(0, 2*np.pi, 1440)) + np.random.normal(0, 0.05, 1440)
    df = pd.DataFrame({'timestamp': idx, 'kW': consumo})
    out_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'consumo_sample.csv')
    out_path = os.path.abspath(out_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)
    print('Arquivo gerado:', out_path)
    return out_path

if __name__ == '__main__':
    main()
