from flask import Flask, request, jsonify, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from datetime import datetime

app = Flask(__name__)

def obter_atividades_pendentes(username, password):

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    driver = webdriver.Chrome(options=options)  

    try:
        driver.get("https://sigaa.sig.ufal.br/sigaa/verTelaLogin.do")


        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "user.login"))
        ).send_keys(username)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "user.senha"))
        ).send_keys(password)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
        ).click()

  
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table/tbody/tr"))
        )

        linhas = driver.find_elements(By.XPATH, "//table/tbody/tr")


        padrao = re.compile(r"\(\d+ dias\)|\(Hoje\)|\(Amanhã\)|[0-9]{1,2}/[0-9]{1,2}|Em breve")

        atividades_pendentes = []
        data_atual = datetime.now()

        for linha in linhas:
            texto = linha.text
            match = padrao.search(texto)

            if match:

                imagens = linha.find_elements(By.TAG_NAME, "img")
                concluida = any("/sigaa/img/check.png" in img.get_attribute("src") for img in imagens)

                if not concluida:  # Apenas adiciona se NÃO estiver concluída
                    if "Hoje" in texto or "Amanhã" in texto or "Em breve" in texto:
                        atividades_pendentes.append(texto)
                    else:
                        data_str = re.search(r"(\d{1,2}/\d{1,2})", texto)
                        if data_str:
                            try:
                                data_entrega = datetime.strptime(data_str.group(1), "%d/%m")
                                data_entrega = data_entrega.replace(year=data_atual.year)

                                if data_entrega >= data_atual:
                                    atividades_pendentes.append(texto)
                            except ValueError:
                                continue

        print("Atividades capturadas:", atividades_pendentes)

        return atividades_pendentes

    except Exception as e:
        return {"erro": str(e)}
    finally:
        driver.quit()

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"erro": "Usuário e senha são obrigatórios"}), 400

    atividades = obter_atividades_pendentes(username, password)

    if isinstance(atividades, dict) and atividades.get("erro"):
        return jsonify(atividades), 500

    return jsonify({"atividades_pendentes": atividades})

if __name__ == "__main__":
    app.run(debug=True)
