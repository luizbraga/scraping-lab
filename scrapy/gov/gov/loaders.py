import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from gov.items import DeputadoItem


def limpar_telefone(telefone):
    return ''.join(re.findall('(\d)', telefone))


def strip_texto(texto):
    return texto.strip()


clear_telefone = MapCompose(
    limpar_telefone)

clear_nome = MapCompose(
    strip_texto)


class DeputadoLoader(ItemLoader):
    default_item_class = DeputadoItem
    nome_out = clear_nome
    telefone_out = clear_telefone
