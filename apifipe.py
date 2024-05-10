import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import *

servico = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

navegador = webdriver.Chrome(options=options, service=servico)

navegador.implicitly_wait(20)

# while True:
  # try:
navegador.get('https://veiculos.fipe.org.br/#carro-comum')
# sleep(5)

elemento = navegador.find_element(By.XPATH, '//*[@id="front"]/div[1]/div[1]/ul/li[1]/a')

print(elemento.is_displayed())

EC.element_to_be_clickable((elemento))



# sleep(5)

navegador.find_element('xpath', '//*[@id="selectMarcacarro"]').click()

# sleep(5)

modelos = navegador.find_element(By.ID, 'selectMarcacarro').find_elements(By.TAG_NAME, 'option')

# sleep(5)

carros = []
for i in range(1, len(modelos)):
  if modelos[i].text == '':
    break
  carros.append(modelos[i].text)

select = Select(navegador.find_element(By.ID, 'selectMarcacarro'))
select.select_by_visible_text(carros[0])

select_ano = navegador.find_element(By.ID, 'selectAnocarro').find_elements(By.TAG_NAME, 'option')
print(select_ano[0][1].text)

# ano = []
# for i in range(1, len(select_ano)):
#   ano.append(select_ano[i].text)



# sleep(5)
    # break
  # except:
  #   navegador.get('https://google.com.br')
  #   continue
# dicionario = {'modelo': carros}
# print(dicionario)