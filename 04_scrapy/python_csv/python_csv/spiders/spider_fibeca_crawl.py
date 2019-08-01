# import scrapy
# from python_csv.items import ProductoFybeca
# from scrapy.loader import ItemLoader
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor


# class AraniaProductosFybecaCrawl(CrawlSpider):
#   name = 'arania_fybeca_crawl'

#   allowed_domains = [
#     'fybeca.com'
#   ]
#   start_urls = [
#   'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25'
#   ]

#   regla = (
#     Rule(
#       LinkExtractor(
#         allow_domains=allowed_domains,
#         allow=('?cat=238')
#       ), callback='parse_page'),
#   )

#   rules = regla

#   def parse_page(self, response):
#     productos = response.css('div.product-tile-inner')
#     for producto in productos:
#       existe_producto = len(producto.css('div.detail'))
#       if(existe_producto > 0):
#         producto_loader = ItemLoader(
#           item = ProductoFybeca(),
#           selector = producto
#         )
#         producto_loader.add_css(
#           'titulo',
# 					'a.name::text'
# 				  )
#         producto_loader.add_xpath(
# 					'imagen',
# 					'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'
# 				  )

#         yield producto_loader.load_item()
# 				# producto_imprimir = product_loader.load_item()
# 				# print(producto_imprimir)
