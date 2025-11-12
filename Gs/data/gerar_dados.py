import pandas as pd
import numpy as np
from datetime import datetime


index = pd.date_range(start=datetime(2025, 1, 1), periods=1440, freq='T')
consumo = 0.5 + 0.3 * np.sin(np.linspace(0, 6.28, 1440)) + np.random.normal(0, 0.05, 1440)

df = pd.DataFrame({
    'timestamp': index,
    'kW': consumo
})

# Salva o arquivo de dados
df.to_csv('consumo_sample.csv', index=False)

print("✅ Arquivo 'consumo_sample.csv' gerado com sucesso dentro da pasta data/")
