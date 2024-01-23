
from flask import Flask, render_template, request, jsonify
import requests
import json
import os
import dotenv

dotenv.load_dotenv()

app = Flask(__name__, template_folder=r'C:\Users\Manuela.DESKTOP-H5K2INA\Desktop\PROGRAMAS\Python\portfolio\templates')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

openai_api_key = os.getenv("OPENAI_API_KEY")
url_gpt = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gerar_receita", methods=["POST"])
def gerar_receita():
    receita = request.form.get("receita")

    # Obter receita usando o GPT
    receita_gerada = obter_receita_gpt(receita)

    return jsonify({"receita": receita_gerada})

def obter_receita_gpt(receita):
    data_gpt = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Gere receitas culinárias"},
            {"role": "user", "content": receita}
        ],
        "temperature": 1,
        "max_tokens": 500,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    response_gpt = requests.post(url_gpt, headers=headers, data=json.dumps(data_gpt))
    recipe_result = response_gpt.json()
    return recipe_result["choices"][0]["message"]["content"]

if __name__ == "__main__":
    app.run(debug=True)
