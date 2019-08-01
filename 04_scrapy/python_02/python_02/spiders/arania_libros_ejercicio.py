import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlUrl(CrawlSpider):
  name='crawl_libro'
  allowed_domains = [
    'books.toscrape.com'
  ]
  start_urls = [
    'http://books.toscrape.com/'
  ]
  regla_uno = (
      Rule(LinkExtractor(), callback='parse_page'),
  )

  url_segmento_permitido = (
    'catalogue/category/books/mystery_3/index.html',
    'catalogue/category/books/fantasy_19/index.html'
  )

  regla_dos = (
      Rule(
          LinkExtractor(
              allow_domains=allowed_domains,
              allow=url_segmento_permitido
          ), callback='parse_page'),
  )

  rules = regla_dos

  def parse_page(self, response):
    etiqueta_contenedor = response.css('article.product_pod')
    titulos = etiqueta_contenedor.css('h3 > a::attr(title)').extract()

    for titulo in titulos:
      with open('titulos.txt', 'a+') as archivo:
        archivo.write(titulo+'\n')
