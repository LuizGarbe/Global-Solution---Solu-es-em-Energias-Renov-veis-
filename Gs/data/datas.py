import pandas as pd
import numpy as np

idx = pd.date_range('2025-01-01', periods=1440, freq='T')
consumo = 0.5 + 0.3*np.sin(np.linspace(0,6.28,1440)) + np.random.normal(0,0.05,1440)

df = pd.DataFrame({'timestamp': idx, 'kW': consumo})
df.to_csv('data/consumo_sample.csv', index=False)