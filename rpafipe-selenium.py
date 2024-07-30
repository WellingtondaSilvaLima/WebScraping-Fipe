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

while True:
  try:
    if navegador.find_element(By.CLASS_NAME, 'modal alert'):
      navegador.refresh()
    else:
      campos = navegador.find_elements(By.CLASS_NAME, 'ilustra')
      print(len(campos))
      break
  except:
    continue

