from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pyautogui import *
from time import *
from tkinter import messagebox
import pandas as pd

servico = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

navegador = webdriver.Chrome(options=options, service=servico)

navegador.get('https://veiculos.fipe.org.br/#carro-comum')

messagebox.showinfo(title='Início', message='Deixe aberto o site e com a aba dos carros na tela.')

PAUSE = 3

localizacao = locateOnScreen('imagens/carro.png')

x,y = center(localizacao)

click(x,y)

montadoras_ano_carros = []

ciclo = 0
while ciclo <= 2:
  sleep(5)

  #  Clica dentro da caixa
  click(x,(y + 150))

  #  Seleciona o primeio campo, Marca do Veículo
  press('tab')
  
  #  Seleciona a Marca
  press('down')
  press('enter')

  #  Seleciona o Ano
  press('tab')
  press('tab')
  press('down')
  press('enter')

  sleep(5)

  #  Pega uma lista com todas as montadoras
  montadoras = navegador.find_element(By.ID, 'selectMarcacarro').find_elements(By.TAG_NAME, 'option')

  #  Pega uma lista com todos os anos da montadora selecionada
  ano = navegador.find_element(By.ID, 'selectAnocarro').find_elements(By.TAG_NAME, 'option')

  #  Pega todos os modelos do ano selecionado
  modelos = navegador.find_element(By.ID, 'selectAnoModelocarro').find_elements(By.TAG_NAME, 'option')

  print(10*'-')

  for ciclo_ano in range(len(ano)):
    for carro in range(len(modelos)):
      if ano[ciclo_ano].text == '' or modelos[carro].text == '':
        continue
      # montadoras_ano_carros.append()
      print(f'{montadoras[ciclo+1].text} | {ano[ciclo_ano].text} - {modelos[carro].text}')
  
  print(10*'-')
  
  ciclo += 1