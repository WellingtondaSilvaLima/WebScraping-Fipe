'''

Algoritmo:
1. Abre o site https://veiculos.fipe.org.br/#carro-comum
2. Extrai os dados de carros, caminhões e motos
3. Exporta para uma planilha com três abas, uma para cada

'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd


caminho = r'C:\Users\wellington\Desktop\Suporte Atendimento\projetos\APIFipe\APIFipe\chromedriver-win64\chromedriver.exe'  # Path do chromedriver
servico = Service(caminho)  # Configura o serviço do ChromeDriver
navegador = webdriver.Chrome(service=servico)  # Cria o navegador
navegador.maximize_window()  # Deixa a janela maximizada

sleep(2)

navegador.get('https://veiculos.fipe.org.br/#carro-comum')
# sleep(10000000)
contador = 0
while contador < 3:
  try:
    sleep(2)
    try:
      navegador.find_element(By.XPATH, '//*[@id="mm-0"]/div[4]/div[2]/p')
      print('entrou para refrescar')
      navegador.refresh()
      sleep(5)
      navegador.find_element(By.XPATH, '//*[@id="fCAWs6"]/div/label/span[2]').click()
      print('clicou')
    except:
      campos = navegador.find_elements(By.CLASS_NAME, 'ilustra')
      print(f'Tem -> {len(campos)}')
      contador += 1
      break
  except Exception as e:
    contador += 1
    print(f'continuou. O erro foi \n{e}')
    continue

