import scrapy
# Import the ItemObjects
from ..items import YahooscrapingItem

class MostactiveSpider(scrapy.Spider):
    name = 'mostactive_part1'
    def start_requests(self):
        urls = ['https://finance.yahoo.com/quote/MSFT?p=MSFT']  # Microsoft Stocks start URL
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #Declare the item objects
        items = YahooscrapingItem()
        #Save the extracted data in the item objects
        items['stock_name'] = response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').css('::text').extract()
        items['intraday_price'] = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]').css('::text').extract()
        items['price_change'] = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[2]').css('::text').extract()

        yield items