import requests
import json


response = requests.get('http://www.google.com.br')

cep = ''
response = requests.get('http://correiosapi.apphb.com/cep/{}'.format(cep))

response_json = json.loads(response.text)
