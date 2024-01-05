
import requests
import json
from PIL import Image, ImageTk
import tkinter as tk
from io import BytesIO
import threading
from tkinter import scrolledtext


openai_api_key = "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"
url_dall_e = "https://api.openai.com/v1/images/generations"
url_gpt = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

cache_imagens = {}

def obter_receita_gpt(receita):
    data_gpt = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Gere receitas culinárias"},
            {"role": "user", "content": receita}
        ],
        "temperature": 1,
        "max_tokens": 356,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    response_gpt = requests.post(url_gpt, headers=headers, data=json.dumps(data_gpt))
    recipe_result = response_gpt.json()
    return recipe_result["choices"][0]["message"]["content"]


def obter_imagem_dall_e(receita):
    data_dall_e = {
        "model": "dall-e-2",
        "prompt": f"Quero uma imagem de capa da seguinte receita: {receita}",
        "size": "256x256",
        "quality": "standard",
        "n": 1,
    }

    response_dall_e = requests.post(url_dall_e, headers=headers, data=json.dumps(data_dall_e))

    if response_dall_e.status_code == 200:
        result_dall_e = response_dall_e.json()
        image_url = result_dall_e["data"][0]["url"]
        response_image = requests.get(image_url)
        image_bytes = BytesIO(response_image.content)
        return Image.open(image_bytes)
    else:
        print("Erro na solicitação DALL-E:", response_dall_e.status_code, response_dall_e.text)
        return None

def carregar_imagem_e_receita():
    receita = entrada_receita.get()
    thread_gpt = threading.Thread(target=obter_e_exibir_receita, args=(receita,))
    thread_dall_e = threading.Thread(target=carregar_imagem_assincronamente, args=(receita,))

    thread_gpt.start()
    thread_dall_e.start()

def obter_e_exibir_receita(receita):
    receita_gerada = obter_receita_gpt(receita)
    texto_receita.config(state=tk.NORMAL)
    texto_receita.delete(1.0, tk.END)
    texto_receita.insert(tk.END, receita_gerada)
    texto_receita.config(state=tk.DISABLED)

def carregar_imagem_assincronamente(receita):
    janela.after(100, lambda: carregar_imagem(receita))

def carregar_imagem(receita):
    imagem = obter_imagem_dall_e(receita)

    if imagem:
        tk_image = ImageTk.PhotoImage(imagem)
        label_imagem.config(image=tk_image)
        label_imagem.image = tk_image


janela = tk.Tk()
janela.title("Geração de Receita e Imagem")

entrada_receita = tk.Entry(janela, width=50, justify=tk.CENTER)
botao_gerar = tk.Button(janela, text="Gerar Receita e Imagem", command=carregar_imagem_e_receita)
label_imagem = tk.Label(janela)
texto_receita = scrolledtext.ScrolledText(janela, width=50, height=20, wrap=tk.WORD)



entrada_receita.pack(pady=10)
botao_gerar.pack(pady=10)
label_imagem.pack(pady=10)
texto_receita.pack(pady=10)


janela.mainloop()