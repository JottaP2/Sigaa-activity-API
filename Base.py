from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re


driver = webdriver.Chrome()
driver.get("https://sigaa.sig.ufal.br/sigaa/verTelaLogin.do")


login_box = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/form/table/tbody/tr[1]/td/input")
login_box.send_keys("")
time.sleep(5)

pass_box = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/form/table/tbody/tr[2]/td/input")
pass_box.send_keys("")
time.sleep(5)

login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/form/table/tfoot/tr/td/input")
login_button.click()
time.sleep(5)


linhas = driver.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/form/div/table/tbody/tr")


atividades_pendentes = []


datas_padrao = re.compile(r"\(\d+ dias\)|\(Hoje\)")



for linha in linhas:
  if datas_padrao.search(linha.text): 
        atividades_pendentes.append(linha.text)


print("\nAtividades Pendentes:")
for atividade in atividades_pendentes:
    print(atividade)


driver.quit()
