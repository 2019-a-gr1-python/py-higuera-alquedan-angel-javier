import scrapy
from proyecto_analisis.items import InformacionPelicula
from proyecto_analisis.items import InformacionActores
from scrapy.loader import ItemLoader

def generarUrls():
  urls = []
  pags = list(range(1,100))
  for page in pags:
    urls.append(f"https://www.themoviedb.org/movie?page={page}")
  return urls

class AraniaProductosFybeca(scrapy.Spider):
  name = 'arania_peliculas'
  url_base = "https://www.themoviedb.org"

  def start_requests(self):
    urls = generarUrls()
    for url in urls:
      yield scrapy.Request(url=url)

  def parse(self, response):
    links = response.css('div.flex')
    print(f"\nLinks encontrados: {len(links)}\n")
    for link in links:
      movie_link = link.xpath('a/@href').extract_first()
      absolute_link = f"{self.url_base}{movie_link}"
      yield scrapy.Request(absolute_link, callback=self.parse_movie)

  def parse_movie(self, response):
    movie_loader = ItemLoader(
        item=InformacionPelicula(),
        selector=response,
        response=response
    )
    actors_url = response.xpath("//section[contains(@class, 'top_billed')]/p/a/@href").extract_first()
    actors_url = f"{self.url_base}{actors_url}"
    movie_loader.add_value('url', response.url)
    movie_loader.add_xpath('name', "//h2/text()")
    movie_loader.add_xpath('releases_dates', "//ul[@class='releases']/li/text()")
    movie_loader.add_xpath('releases_formats', "//ul[@class='releases']/li/div[@class='certification']/text()")
    movie_loader.add_xpath('language', "//section[contains(@class,'left_column')]/p[strong/bdi[text()='Original Language']]/text()")
    movie_loader.add_xpath('runtime', "//section[contains(@class,'left_column')]/p[strong/bdi[text()='Runtime']]/text()")
    movie_loader.add_xpath('budget', "//section[contains(@class,'left_column')]/p[strong/bdi[text()='Budget']]/text()")
    movie_loader.add_xpath('revenue', "//section[contains(@class,'left_column')]/p[strong/bdi[text()='Revenue']]/text()")
    movie_loader.add_xpath('runtime', "//section[contains(@class,'left_column')]/p[4]/text()")
    movie_loader.add_xpath('budget', "//section[contains(@class,'left_column')]/p[5]/text()")
    movie_loader.add_xpath('revenue', "//section[contains(@class,'left_column')]/p[6]/text()")
    movie_loader.add_xpath('overview', "//div[@class='overview']/p/text()")
    movie_loader.add_xpath('genres', "//a[contains(@href,'genre')]/text()")
    movie_loader.add_xpath('user_score', "//div[@class='percent']/span/@class")
    yield scrapy.Request(actors_url, callback=self.parse_actors, meta={'movie':movie_loader})

  def parse_actors(self, response):
    item = response.meta['movie']
    actors = response.xpath("//div[@class='split']/ol/li/div/div/p/a/text()").extract()
    directors = response.xpath("//div[@class='split']/div[h4[text()='Directing']]/ol/li/div/div/span/p/a/text()").extract()
    writing = response.xpath("//div[@class='split']/div[h4[text()='Writing']]/ol/li/div/div/span/p/a/text()").extract()
    item.add_value('actors', actors)
    item.add_value('directors', directors)
    item.add_value('writing', writing)
    return item.load_item()
