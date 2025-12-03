import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar dados
def load_data():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    csv_path = os.path.join(base, 'data', 'consumo_sample.csv')
    df = pd.read_csv(csv_path, parse_dates=['timestamp'])
    return df

# 2. Gráficos
def make_plots(df, outdir):
    os.makedirs(outdir, exist_ok=True)

    # Série temporal
    plt.figure(figsize=(10, 4))
    plt.plot(df['timestamp'], df['kW'])
    plt.title('Consumo de Energia (kW) - Série Temporal')
    plt.xlabel('Tempo')
    plt.ylabel('kW')
    serie_path = os.path.join(outdir, 'serie_temporal.png')
    plt.tight_layout()
    plt.savefig(serie_path, dpi=150)
    plt.close()

    # Histograma
    plt.figure(figsize=(6, 4))
    plt.hist(df['kW'], bins=40)
    plt.title('Histograma do Consumo (kW)')
    plt.xlabel('kW')
    plt.ylabel('Frequência')
    hist_path = os.path.join(outdir, 'histograma.png')
    plt.tight_layout()
    plt.savefig(hist_path, dpi=150)
    plt.close()

    # Boxplot
    plt.figure(figsize=(4, 4))
    plt.boxplot(df['kW'])
    plt.title('Boxplot do Consumo (kW)')
    box_path = os.path.join(outdir, 'boxplot.png')
    plt.tight_layout()
    plt.savefig(box_path, dpi=150)
    plt.close()

    return serie_path, hist_path, box_path

# 3. Estatísticas
def compute_stats(df):
    return {
        "media": df['kW'].mean(),
        "mediana": df['kW'].median(),
        "pico": df['kW'].max(),
        "min": df['kW'].min(),
        "std": df['kW'].std(),
        "qtd": len(df)
    }

# 4. Salvar estatísticas
def save_stats(stats, outdir):
    os.makedirs(outdir, exist_ok=True)
    txt_path = os.path.join(outdir, "estatisticas.txt")

    with open(txt_path, "w") as f:
        f.write("RELATÓRIO DE ESTATÍSTICAS DO CONSUMO\n")
        f.write("----------------------------------------\n")
        f.write(f"Média: {stats['media']:.3f} kW\n")
        f.write(f"Mediana: {stats['mediana']:.3f} kW\n")
        f.write(f"Pico: {stats['pico']:.3f} kW\n")
        f.write(f"Mínimo: {stats['min']:.3f} kW\n")
        f.write(f"Desvio Padrão: {stats['std']:.3f}\n")
        f.write(f"Total de Amostras: {stats['qtd']}\n")

    print("Arquivo salvo em:", txt_path)
    return txt_path

# 5. MAIN

def main():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    df = load_data()
    stats = compute_stats(df)
    outdir = os.path.join(base, "results")

    make_plots(df, outdir)
    save_stats(stats, outdir)


if __name__ == "__main__":
    main()