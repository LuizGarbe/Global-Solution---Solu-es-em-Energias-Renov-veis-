# 🌱 Global Solution – Soluções em Energias Renováveis e Sustentáveis

## 💡 Sobre o Projeto
Este projeto foi desenvolvido como parte da **Global Solution** do curso de **Ciência da Computação – 2° semestre de 2025**.  
O objetivo é demonstrar, de forma prática, como a **análise de dados e a simulação IoT** podem contribuir para a eficiência energética em ambientes corporativos, promovendo **sustentabilidade e otimização do consumo**.

---

## ⚙️ Estrutura do Projeto

Gs/
├── data/
│ ├── gerar_dados.py # Script que gera dados simulados de consumo
│ └── consumo_sample.csv # Dados gerados automaticamente
│
├── src/
│ ├── analise_consumo.py # Análise da média e do pico de consumo
│ └── iot_simulador.py # Simulação de leituras IoT em tempo real
│
├── docs/ # Documentos e relatórios do projeto
├── results/ # Resultados e gráficos (opcional)
└── requirements.txt # Dependências do projeto

---

## 🧠 Tecnologias Utilizadas
- **Python 3.11**
- **Pandas**
- **NumPy**
- **Time (biblioteca padrão do Python)**

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
   
2. **Instale as dependencias**
   pip install -r requirements.txt

3. **Gere os dados Simulados**
   python data/gerar_dados.py

4. **Execute a análise de Consumo**
   python src/analise_consumo.py

5. **Simule as leituras IOT**
   python src/iot_simulador.py

📊 Resultados Obtidos
Média de consumo aproximada: 0.49 kW
Pico de consumo: 0.91 kW
Simulação IoT exibiu leituras entre 0.5 e 1.1 kW
Esses resultados representam um cenário hipotético de consumo energético diário, com base em uma curva de variação sinusoidal e ruído aleatório, simulando o comportamento real de um sistema elétrico em operação contínua.

🌎 Impacto e Conexão com o Futuro do Trabalho
A proposta mostra como sistemas baseados em dados e IoT podem apoiar ambientes de trabalho sustentáveis, possibilitando:
Monitoramento contínuo de energia;
Identificação de picos e desperdícios;
Decisões mais inteligentes para economia e sustentabilidade.

👨‍💻 Autores
------
------
------
FIAP / SENAC – Ciência da Computação
2025

🎥 Vídeo Explicativo
🔗

🧾 Licença

Este projeto foi desenvolvido para fins acadêmicos e educacionais.
