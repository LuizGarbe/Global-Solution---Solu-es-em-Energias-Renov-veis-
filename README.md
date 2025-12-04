🌱 Global Solution – Soluções em Energias Renováveis e Sustentáveis (SERS)

FIAP – Ciência da Computação – 2025

---

📘 Sobre o Projeto

Este projeto foi desenvolvido para a Global Solution – SERS 2025.
O objetivo central é mostrar como dados, análise computacional e IoT podem ser aplicados para monitorar e otimizar o consumo de energia, conectando tecnologia com sustentabilidade e o futuro do trabalho.

A solução utiliza dados simulados para representar um dia completo de consumo energético, analisa padrões importantes (como média, pico, variação e dispersão) e simula sensores IoT realizando leituras em tempo real.

O projeto permite visualizar desperdícios, entender horários de maior demanda e apoiar decisões para reduzir custos e impactos ambientais.

---

🧩 Funcionalidades Implementadas
✔️ 1. Geração de Dados (Simulação)

Criação automática de 1440 amostras (1 por minuto – 24h).
Dados representando consumo energético (kW) com variação realista.
Saída salva como:
/data/consumo_sample.csv

---

✔️ 2. Análise de Consumo

Cálculo de:
-> Média
-> Mediana
-> Pico (máximo)
-> Mínimo
-> Desvio-padrão
-> Quantidade total de amostras
-> Gera um arquivo com todas as estatísticas:
/results/estatisticas.txt

---

✔️ 3. Visualização de Dados

Geração automática de gráficos dentro da pasta /results:
* Gráfico de Série Temporal → serie_temporal.png
* Histograma da Distribuição → histograma.png
* Boxplot (dispersão do consumo) → boxplot.png

---

✔️ 4. Simulação IoT

Simulação de leituras de sensores, gerando valores reais do dataset:
Saída salva em:
/results/leituras.txt
Isso demonstra como sensores monitorariam o consumo em tempo real.

---

📂 Estrutura Completa do Repositório

Global-Solution/
│
├── data/
│ └── consumo_sample.csv
│
├── results/
│ ├── boxplot.png
│ ├── estatisticas.txt
│ ├── histograma.png
│ ├── leituras.txt
│ └── serie_temporal.png
│
├── src/
│ ├── analise_consumo.py
│ ├── gerar_dados.py
│ ├── iot_simulador.py
│ └── relatorio_gerador.py 
│
├── requirements.txt
└── README.md

---

⚙️ Tecnologias Utilizadas

-> Python 3.11
-> NumPy
-> Pandas
-> Matplotlib
-> Time
-> GitHub

---

🚀 Como Executar o Projeto

1. Instale as dependências:
pip install -r requirements.txt

2. Gere os dados de consumo:
python src/gerar_dados.py

3. Faça a análise dos dados:
python src/analise_consumo.py

4. Gere gráficos e arquivos de resultados:
python src/relatorio_gerador.py

5. Simule sensores IoT:
python src/iot_simulador.py
Todos os resultados aparecerão automaticamente na pasta:
📁 /results


---

📊 Resultados Obtidos

Com base nos dados simulados, o projeto conseguiu identificar:
Consumo médio aproximado: ~0.49 kW
Pico de consumo: ~0.91 kW
Variação moderada ao longo do dia
Leituras IoT entre 0.50 e 1.10 kW
Os gráficos mostram claramente a distribuição do consumo e sua evolução ao longo de um dia.

---

🔮 Impacto e Conexão com o Futuro do Trabalho

A proposta mostra como ferramentas digitais podem:
* Monitorar ambientes corporativos de forma inteligente
* Reduzir desperdício energético
* Automatizar análise e tomada de decisão
* Criar ambientes sustentáveis e eficientes
* Aplicar IoT em situações reais de trabalho
* O uso de dados e automação já é uma das bases do trabalho moderno — e este projeto demonstra o primeiro passo para um sistema real de eficiência energética.

---

👨‍💻 Autores
- Luiz Eduardo
- Eduardo Luiz
- Emanuel Nabarrete

#### FIAP – Ciência da Computação – 2025

---

🧾 Licença
Este projeto foi desenvolvido exclusivamente para fins acadêmicos e educacionais.
