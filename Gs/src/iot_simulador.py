import time, random

while True:
    leitura = round(random.uniform(0.4, 1.2), 3)
    print(f"Leitura simulada: {leitura} kW")
    time.sleep(60)