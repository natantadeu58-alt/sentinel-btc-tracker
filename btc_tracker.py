import os
import time
from datetime import datetime
import requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def obter_preco_btc():
    url = "https://coingecko.com"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    preco = data["bitcoin"]["usd"]
    variacao = data["bitcoin"]["usd_24h_change"]
    return preco, variacao


def salvar_log(mensagem):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("sentinel_btc_logs.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{timestamp}] {mensagem}\n")


def ejecutar_sentinel():
    print("SENTINEL BITCOIN - Monitoramento Ativo...")
    salvar_log("Sistema iniciado e monitorando mercado.")

    while True:
        try:
            preco, variacao = obter_preco_btc()
            cor_variacao = "+" if variacao >= 0 else ""
            print(
                f"\nCheck: BTC a $ {float(preco):,.2f} ({cor_variacao}{float(variacao):.2f}%)"
            )

            if abs(variacao) > 0.1:
                prompt = f"O Bitcoin está custando ${preco} com variação de {variacao:.2f}% nas últimas 24h. Gere um insight rápido de mercado sobre este cenário."
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.3-70b-versatile",
                )
                insight = chat_completion.choices[0].message.content
                print(f"IA INSIGHT: {insight}")
                salvar_log(f"BTC: ${preco} | Var: {variacao:.2f}% | IA: {insight}")

            time.sleep(60)

        except requests.exceptions.RequestException as req_err:
            erro_msg = f"Erro de conexão/API: {req_err}"
            print(f" {erro_msg}")
            salvar_log(erro_msg)
            time.sleep(30)
        except Exception as e:
            erro_msg = f"Erro inesperado na execução: {e}"
            print(f" {erro_msg}")
            salvar_log(erro_msg)
            time.sleep(30)


if __name__ == "__main__":
    ejecutar_sentinel()
