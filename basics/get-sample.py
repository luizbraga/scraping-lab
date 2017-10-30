import requests
import json


response = requests.get('http://www.google.com.br')

cep = '52171900'
response = requests.get('http://api.postmon.com.br/v1/cep/{}'.format(cep))
response_json = json.loads(response.text)
