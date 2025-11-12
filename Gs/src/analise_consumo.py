import pandas as pd

df = pd.read_csv('data/consumo_sample.csv')
media = df['kW'].mean()
pico = df['kW'].max()
print(f"Média de consumo: {media:.2f} kW")
print(f"Pico de consumo: {pico:.2f} kW")