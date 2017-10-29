import requests
from bs4 import BeautifulSoup


URL = 'https://www25.senado.leg.br/web/senadores/em-exercicio'
response = requests.get(URL)

bs = BeautifulSoup(response.text)
for link in bs.find_all('a'):
    print(link.get_text())

# Filtro para obter apenas os links da tabela de senadores
tabela_senadores = bs.find('table', id="senadoresemexercicio-tabela-senadores")
for senador in tabela_senadores('a'):
    print(senador.text)

# Filtro de elementos não necessários
for senador in tabela_senadores('a', href=lambda x: x != '#'):
    print(senador.text)
