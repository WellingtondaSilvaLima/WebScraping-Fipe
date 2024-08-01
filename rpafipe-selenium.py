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
from tkinter import messagebox


caminho = r'C:\Users\wellington\Desktop\Suporte Atendimento\projetos\APIFipe\APIFipe\chromedriver-win64\chromedriver.exe'  # Path do chromedriver
servico = Service(caminho)  # Configura o serviço do ChromeDriver
navegador = webdriver.Chrome(service=servico)  # Cria o navegador
navegador.maximize_window()  # Deixa a janela maximizada

sleep(2)

navegador.get('https://veiculos.fipe.org.br/#carro-comum')

messagebox.showinfo(title='Início', message='Pode iniciar?')

identificador = ['selectMarcacarro', 'selectMarcacaminhao', 'selectMarcamoto']
tabela_veiculos = navegador.find_element(By.CLASS_NAME, 'tab-veiculos')
veiculos = tabela_veiculos.find_elements(By.CLASS_NAME, 'ilustra')

veiculos[0].click()
carros = veiculos[0].find_element(By.CLASS_NAME, 'horizontal')
artigos_html = carros.find_elements(By.TAG_NAME, 'article')
formulario = artigos_html[0].find_element(By.CLASS_NAME, 'form')
step_1 = formulario.find_element(By.CLASS_NAME, 'step-1')
entrada_carros = step_1.find_element(By.CLASS_NAME, 'input')
sleep(1)
entrada_carros.click()
sleep(1)
seletor = entrada_carros.find_element(By.TAG_NAME, 'select')
opcoes_carros = seletor.find_elements(By.TAG_NAME, 'option')
primeiro = opcoes_carros[1]

print(primeiro.text)
# for op in opcoes_carros:
#   print(op.text)



