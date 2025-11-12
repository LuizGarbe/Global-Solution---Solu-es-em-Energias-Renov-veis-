import os
import pandas as pd

# Caminho absoluto até o CSV dentro da pasta 'data'
csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'consumo_sample.csv')

df = pd.read_csv(csv_path)

media = df['kW'].mean()
pico = df['kW'].max()

print(f"Média de consumo: {media:.3f} kW")
print(f"Pico de consumo: {pico:.3f} kW")
