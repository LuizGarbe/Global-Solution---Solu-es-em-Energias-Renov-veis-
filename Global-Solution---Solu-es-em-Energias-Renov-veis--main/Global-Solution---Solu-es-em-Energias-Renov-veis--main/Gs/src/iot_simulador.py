import os, time
import pandas as pd

def read_csv():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    csv_path = os.path.join(base, 'data', 'consumo_sample.csv')
    df = pd.read_csv(csv_path, parse_dates=['timestamp'])
    return df

def simulate_live_readings(df, n=10, delay=0.5):
    leituras = []
    for i in range(n):
        val = float(df['kW'].sample(1).values[0])
        leituras.append(val)
        print(f"Leitura simulada: {val:.3f} kW")
        time.sleep(delay)
    return leituras

def save_readings(leituras):
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    outdir = os.path.join(base, "results")
    os.makedirs(outdir, exist_ok=True)

    path = os.path.join(outdir, "leituras_iot.txt")
    with open(path, "w") as f:
        f.write("LEITURAS IoT SIMULADAS\n")
        f.write("-------------------------\n")
        for i, v in enumerate(leituras):
            f.write(f"{i+1}. {v:.3f} kW\n")

    print("Leituras salvas em:", path)

if __name__ == '__main__':
    df = read_csv()
    leituras = simulate_live_readings(df, n=7, delay=0.3)
    save_readings(leituras)