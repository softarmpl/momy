import scrapy


class TrojmiastoSpider(scrapy.Spider):
    name = 'trojmiasto'
    allowed_domains = ['trojmiasto.pl']
    start_urls = ['https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/mieszkanie/e1i,12_17_14_13_18_16_82_92_24_98_19_25_6_10_11_9_15_23_61_20_21_84,ikl,101,qi,62_80.html']

    def parse(self, response):
        pass
