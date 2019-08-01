# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import Join
from scrapy.loader.processors import TakeFirst
import re

class PythonCsvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def transformar_url_imagen(texto): 
    return texto

def parse_money(texto): 
    return re.sub(r"[ $,]","",texto)

def parse_rating(texto): 
    texto = re.sub(r"icon.","",texto)
    return texto.replace("r","")

def strip_text(texto): 
    texto = f"{texto}"
    return texto.strip()

class InformacionActores(scrapy.Item):
    actors = scrapy.Field(
        output_processor = Join(separator="/")
    )
    directors = scrapy.Field(
        output_processor = Join(separator="/")
    )
    guionists = scrapy.Field(
        output_processor = Join(separator="/")
    )

class InformacionPelicula(scrapy.Item):
    releases_dates = scrapy.Field(
        output_processor = Join()
    )
    releases_formats = scrapy.Field(
        output_processor = Join()
    )
    name = scrapy.Field(
        input_processor = MapCompose(strip_text),
        output_processor = TakeFirst()
    )
    overview = scrapy.Field(
        output_processor = TakeFirst()
    )
    language = scrapy.Field(
        input_processor = MapCompose(strip_text),
        output_processor = TakeFirst()
    )
    runtime = scrapy.Field(
        output_processor = TakeFirst()
    )
    budget = scrapy.Field(
        input_processor = MapCompose(parse_money),
        output_processor = TakeFirst()
    )
    revenue = scrapy.Field(
        input_processor = MapCompose(parse_money),
        output_processor = TakeFirst()
    )
    url = scrapy.Field(
        output_processor = TakeFirst()
    )
    genres = scrapy.Field(
        output_processor = Join(separator="/")
    )
    user_score = scrapy.Field(
        input_processor = MapCompose(parse_rating),
        output_processor = TakeFirst()
    )
    actors = scrapy.Field(
        output_processor = Join(separator="/")
    )
    directors = scrapy.Field(
        output_processor = Join(separator="/")
    )
    writing = scrapy.Field(
        output_processor = Join(separator="/")
    )
