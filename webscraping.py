import requests
from bs4 import BeautifulSoup

# Faz uma requisição HTTP para obter o conteúdo teperatura atual da página web
html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp').content


# Cria um objeto BeautifulSoup para analisar o conteúdo HTML
soup = BeautifulSoup(html, 'html.parser')


# Encontra o elemento HTML que contém a temperatura mínima
temp_min = soup.find(id='min-temp-1')
print(f' A temperatura mínima é: {temp_min.text}')


# Encontra o elemento HTML que contém a temperatura máxima
temp_max = soup.find(id='max-temp-1')
print(f' A temperatura máxima é: {temp_max.text}')


resumo = soup.find(class_='-gray -line-height-24 _center')
print(f'Resumo: {resumo.text}')


