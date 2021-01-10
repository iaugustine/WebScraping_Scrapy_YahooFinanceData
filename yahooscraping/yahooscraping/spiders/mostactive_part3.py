import scrapy
# Import the ItemObjects
from ..items import YahooscrapingItem

class MostactiveSpider(scrapy.Spider):
    name = 'mostactive_part3'
    def start_requests(self):
        urls = ['https://finance.yahoo.com/most-active/']  # Most active start URL
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_pages)

    def get_pages(self, response):
        count = str(response.xpath('// *[ @ id = "fin-scr-res-table"] / div[1] / div[1] / span[2] / span').css(
            '::text').extract())
        total_results = int(count.split()[-2])
        total_offsets = total_results // 25 + 1
        offset_list = [i * 25 for i in range(total_offsets)]
        for offset in offset_list:
            yield scrapy.Request(url=f'https://finance.yahoo.com/most-active?count=25&offset={offset}',
                                 callback=self.get_stocks)

    def get_stocks(self, response):
        # Get all the stock symbols
        stocks = response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody//tr/td[1]/a').css('::text').extract()
        for stock in stocks:
            # Follow the link to the stock details page.
            yield scrapy.Request(url=f'https://finance.yahoo.com/quote/{stock}?p={stock}', callback=self.parse)

    def parse(self, response):
        #Declare the item objects
        items = YahooscrapingItem()
        #Save the extracted data in the item objects
        items['stock_name'] = response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').css('::text').extract()
        items['intraday_price'] = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]').css('::text').extract()
        items['price_change'] = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[2]').css('::text').extract()
        yield items