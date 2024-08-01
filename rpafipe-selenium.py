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
navegador.set_window_size(930,1014)  # Define o tamanho da tela


def extrai_veiculos(veiculos:list):
  '''
  Inicia a extração dos veículos da tabela FIPE

  Parâmetros:
    - veiculos: é uma das posições da tabela de veículos da FIPE (carros, caminhões ou motos)
  
  Retorno:
    - Não retorna nada
  '''
  veiculos.click()
  carros = veiculos.find_element(By.CLASS_NAME, 'horizontal')
  artigos_html = carros.find_elements(By.TAG_NAME, 'article')
  formulario = artigos_html[0].find_element(By.CLASS_NAME, 'form')
  step_1 = formulario.find_element(By.CLASS_NAME, 'step-1')
  step_2 = formulario.find_element(By.CLASS_NAME, 'step-2')
  entrada_carros = step_1.find_element(By.CLASS_NAME, 'input')

  entrada_carros.click()

  seletor = entrada_carros.find_element(By.TAG_NAME, 'select')
  opcoes_carros = seletor.find_elements(By.TAG_NAME, 'option')

  lista_montadoras = []
  for op in opcoes_carros:
    if op.text == '': continue

    lista_montadoras.append(op.text)
    op.click()
    seleciona_ano(step_2)


def seleciona_ano(step_2):
  entradas = step_2.find_elements(By.CLASS_NAME, 'input')

  entradas[1].click()

  seletor = entradas[1].find_element(By.TAG_NAME, 'select')
  opcoes_ano = seletor.find_elements(By.TAG_NAME, 'option')

  lista_anos = []
  for op in opcoes_ano:
    if op.text == '': continue

    lista_anos.append(op.text)
    op.click()
    seleciona_modelo(entradas[2])


def seleciona_modelo(entrada):
  entrada.click()

  seletor = entrada.find_element(By.TAG_NAME, 'select')
  opcoes_modelo = seletor.find_elements(By.TAG_NAME, 'option')

  lista_modelos = []
  for op in opcoes_modelo:
    if op.text == '': continue

    lista_modelos.append(op.text)

  return {
        'Modelo': lista_modelos
        }


sleep(2)

navegador.get('https://veiculos.fipe.org.br/#carro-comum')

messagebox.showinfo(title='Início', message='Pode iniciar?')

tabela_veiculos = navegador.find_element(By.CLASS_NAME, 'tab-veiculos')
veiculos = tabela_veiculos.find_elements(By.CLASS_NAME, 'ilustra')

lista_montadoras = []
lista_anos = []
lista_modelos = []

extrai_veiculos(veiculos[0], lista_montadoras, lista_anos, lista_modelos)

