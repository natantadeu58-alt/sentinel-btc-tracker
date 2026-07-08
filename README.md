# 🪙 Sentinel BTC Tracker

Uma ferramenta inteligente em Python projetada para o monitoramento contínuo do preço do Bitcoin (BTC), integração de dados financeiros em tempo real e geração automatizada de insights analíticos utilizando Inteligência Artificial.

## 🚀 Funcionalidades

- **Monitoramento Financeiro:** Consumo automatizado da cotação e variação percentual diária do Bitcoin através da API pública do **CoinGecko**.
- **Insights com IA:** Integração com os modelos de linguagem de altíssima velocidade do **Groq** (`llama-3.3-70b-versatile`) para analisar cenários de mercado e gerar relatórios instantâneos quando ocorrem oscilações relevantes.
- **Auditoria de Logs:** Sistema persistente de gravação de logs locais (`sentinel_btc_logs.txt`) que registra o histórico de preços, variações e as análises geradas pela IA.
- **Arquitetura Segura:** Isolamento completo de credenciais confidenciais e chaves de API por meio de variáveis de ambiente (`.env`).

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Requests** (Consumo estruturado da API HTTP do CoinGecko)
- **Groq SDK** (Processamento dos prompts analíticos de IA)
- **Python-Dotenv** (Gerenciamento e proteção de variáveis de ambiente)

## 🔧 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de possuir o Python instalado em sua máquina e uma chave de acesso válida do [Groq Console](https://groq.com).

### 2. Clonar o Repositório
```bash
git clone https://github.com
cd sentinel-btc-tracker
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do diretório do projeto e insira sua credencial de autenticação:
```env
GROQ_API_KEY=sua_chave_real_aqui
```

### 5. Iniciar o Monitoramento
```bash
python btc_tracker.py
```

---
💡 *Desenvolvido como projeto prático de portfólio focado em Engenharia de Software, integração de APIs e FinTech.*
