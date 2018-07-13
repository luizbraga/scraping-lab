# -*- coding: utf-8 -*-
import scrapy
from gov.loaders import DeputadoLoader

DEPUTADO_XPATH = (
    '//div[@id="content"]//div[@class="bloco clearedBox"]/ul/li[{x}]/text()')


class DeputadoSpider(scrapy.Spider):
    name = 'deputado'
    allowed_domains = ['http://www2.camara.leg.br/deputados/pesquisa']
    start_urls = ['http://www2.camara.leg.br/deputados/pesquisa/']

    def parse(self, response):
        value_deputados = response.xpath(
            '//select[@id="deputado"]/option/@value')
        for value in value_deputados:
            url_deputado = (
                'http://www.camara.leg.br/internet/'
                'Deputado/dep_Detalhe.asp?id={}')
            id_deputado = value.re('\?(.*)')
            if id_deputado:
                yield scrapy.Request(
                    url=url_deputado.format(id_deputado[0]),
                    dont_filter=True,
                    callback=self.pagina_deputado)

    def pagina_deputado(self, response):
        # @todo Loader not working properly
        loader = DeputadoLoader(response=response)
        loader.add_xpath('nome', DEPUTADO_XPATH.format(x=1))
        loader.add_xpath('telefones', DEPUTADO_XPATH.format(x=4))
        yield loader.load_item()
