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

def entra_no_form(identificador:str):
  campos_carros = navegador.find_element(By.CLASS_NAME, 'form')
  seletor = campos_carros.find_element(By.ID, identificador)
  carros = seletor.find_elements(By.TAG_NAME, 'option')
  print(seletor)
  print(len(carros))

  print(15*'=')

identificador = ['selectMarcacarro', 'selectMarcacaminhao', 'selectMarcamoto']
campos = navegador.find_elements(By.CLASS_NAME, 'ilustra')
campos[0].click()
sleep(3)
entra_no_form(f'{identificador[0]}')
sleep(3)
campos[1].click()
sleep(3)
entra_no_form(f'{identificador[1]}')
sleep(3)
campos[2].click()
sleep(3)
entra_no_form(f'{identificador[2]}')
sleep(3)


