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

j = 0
while j <= 2:
  sleep(5)

  click(x,(y + 150))

  press('tab')
  press('down')
  press('enter')
  press('tab')
  press('tab')
  press('down')
  press('enter')

  sleep(5)

  elemento = navegador.find_element(By.ID, 'selectAnoModelocarro').click()

  montadoras = navegador.find_element(By.ID, 'selectMarcacarro').find_elements(By.TAG_NAME, 'option')
  ano = navegador.find_element(By.ID, 'selectAnocarro').find_elements(By.TAG_NAME, 'option')
  
  for z in range(len(ano)):
    if ano[z].text == '':
      print(5*'-' + '\n' + montadoras[j+1].text + ' | ' + ano[z+1].text + '\n' + 5*'-')
    else:
      print(5*'-' + '\n' + montadoras[j].text + ' | ' + ano[z].text + '\n' + 5*'-')


    veiculos = navegador.find_element(By.ID, 'selectAnoModelocarro').find_elements(By.TAG_NAME, 'option')

    for i in range(len(veiculos)):
      if veiculos[i].text == '':
        continue
      print(veiculos[i].text)
  
  j += 1