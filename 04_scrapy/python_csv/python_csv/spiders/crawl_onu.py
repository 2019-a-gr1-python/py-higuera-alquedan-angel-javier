# import scrapy

# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor

# class AraniaCrawlUrl(CrawlSpider):
#   name='crawl_onu'
#   allowed_domains = [
#   'fybeca.com'
#   ]
#   start_urls = [
#   'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25'
#   ]
#   rules = (
#     Rule(
#       LinkExtractor(
#         allow_domains=allowed_domains,
#         allow=('cat=238')
#       ), callback='parse_page'),
#   )

#   def parse_page(self, response):
#     lista_programas= response.css('a.name::text').extract_first()
#     print(lista_programas)
