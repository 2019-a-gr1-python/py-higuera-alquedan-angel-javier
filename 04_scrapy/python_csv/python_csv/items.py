# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst


class PythonCsvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def transformar_url_imagen(texto): 
    url = 'https://www.fybeca.com' 
    cadena_a_reemplazar = '../..'   
    return texto.replace(cadena_a_reemplazar,url)

def transformar_precio_float(texto): 
    numero = float(texto.replace("text:'$' + (", "").replace(").formatMoney(2, '.', ',')", ""))
    return numero

class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(transformar_url_imagen),
        output_processor = TakeFirst()
    )
    titulo = scrapy.Field(
        output_processor = TakeFirst()
    )
    precio_1 = scrapy.Field(
        input_processor = MapCompose(transformar_precio_float),
        output_processor = TakeFirst()
    )
    precio_0 = scrapy.Field(
        input_processor = MapCompose(transformar_precio_float),
        output_processor = TakeFirst()
    )