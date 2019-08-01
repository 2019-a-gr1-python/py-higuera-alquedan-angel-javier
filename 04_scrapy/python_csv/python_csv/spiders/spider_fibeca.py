import scrapy
from python_csv.items import ProductoFybeca
from scrapy.loader import ItemLoader

def generarUrls():
  urls = []
  pags = list(range(0,151,25))
  for page in pags:
    urls.append(f"https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s={page}&pp=25")
  return urls

class AraniaProductosFybeca(scrapy.Spider):
  name = 'arania_fybeca'

  def start_requests(self):
    urls = generarUrls()
    for url in urls:
      yield scrapy.Request(url=url)

  def parse(self, response):
    productos = response.css('div.product-tile-inner')

    print(f"\n\n{len(productos)}\n\n")

    for producto in productos:
      existe_producto = len(producto.css('div.detail'))
      if(existe_producto > 0):
        producto_loader = ItemLoader(
          item = ProductoFybeca(),
          selector = producto
        )
        producto_loader.add_css(
          'titulo',
					'a.name::text'
				  )
        producto_loader.add_xpath(
          'precio_1',
					'div[contains(@class,"detail")]/div[@class="side"]/div[@class="price-member"]/div/@data-bind'
				  )
        producto_loader.add_xpath(
          'precio_0',
					'div[contains(@class,"detail")]/div[@class="side"]/div[@class="price"]/@data-bind'
				  )
        producto_loader.add_xpath(
					'imagen',
					'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'
				  )
        yield producto_loader.load_item()
    
  

