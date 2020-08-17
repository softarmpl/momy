import scrapy


class AutosSpider(scrapy.Spider):
    name = 'autos'
    allowed_domains = ['sklep2.autos.com.pl']
    start_urls = ['http://sklep2.autos.com.pl/customer/articles']
    start_urls = ['http://sklep2.autos.com.pl/customer/articles/12710']

    def parse(self, response):
        categories_links = response.xpath("//a[@class='article-brand']/@href")
        
        print(categories_links)
        
