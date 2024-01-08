import requests
import json
import tkinter as tk
from tkinter import scrolledtext
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
url_gpt = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

def obter_receita_gpt(receita):
    data_gpt = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Gere receitas culinárias"},
            {"role": "user", "content": receita}
        ],
        "temperature": 1,
        "max_tokens": 400,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    response_gpt = requests.post(url_gpt, headers=headers, data=json.dumps(data_gpt))
    response_data = response_gpt.json()

    # Verifique se 'choices' está presente na resposta
    if 'choices' in response_data:
        return response_data["choices"][0]["message"]["content"]

    else:
        return "Erro na resposta da API: 'choices' não encontrado."

def carregar_receita():
    receita = entrada_receita.get()
    texto_receita.config(state=tk.NORMAL)
    texto_receita.delete(1.0, tk.END)
    texto_receita.insert(tk.END, obter_receita_gpt(receita))
    texto_receita.config(state=tk.DISABLED)

janela = tk.Tk()
janela.title("Geração de Receita")

entrada_receita = tk.Entry(janela, width=50, justify=tk.CENTER)
botao_gerar = tk.Button(janela, text="Gerar Receita", command=carregar_receita)
texto_receita = scrolledtext.ScrolledText(janela, width=50, height=20, wrap=tk.WORD)

entrada_receita.pack(pady=10)
botao_gerar.pack(pady=10)
texto_receita.pack(pady=10)

janela.mainloop()