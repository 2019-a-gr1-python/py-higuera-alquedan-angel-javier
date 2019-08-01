import scrapy

import numpy as np
import pandas as pd
import os

class IntroSpider(scrapy.Spider):
  name = 'introduccion_spider'

  def start_requests(self):
    urls = [
      'http://books.toscrape.com/catalogue/category/books_1/page-1.html'
    ]

    for url in urls:
      yield scrapy.Request(url=url)
  
  def parse(self, response):
    etiqueta_contenedor = response.css('article.product_pod')
    titulos = etiqueta_contenedor.css('h3 > a::attr(title)').extract()
    raw_stocks = etiqueta_contenedor.css( 'div.product_price > p.instock::text').extract()
    stocks = list(filter(lambda x: x != '\n    ', raw_stocks))
    stocks = list(map(lambda x: x.replace("\n    \n        ", "").replace("\n    \n", ""), stocks))
    precios = etiqueta_contenedor.css('div.product_price > p.price_color::text').extract()

    data_frame = pd.DataFrame({
      'titulos': titulos,
      'stock': stocks,
      'precios': precios
    })

    data_frame.to_csv('data.csv')
    
    print(data_frame)

