# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YahooscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    stock_name = scrapy.Field()
    intraday_price = scrapy.Field()
    price_change = scrapy.Field()
    current_timestamp = scrapy.Field()
    prev_close = scrapy.Field()
    open = scrapy.Field()
    bid = scrapy.Field()
    ask = scrapy.Field()
    range_day = scrapy.Field()
    range_52weeks = scrapy.Field()
    volume = scrapy.Field()
    volume_avg = scrapy.Field()
    market_cap = scrapy.Field()
    beta_5yr_monthly = scrapy.Field()
    pe_ratio = scrapy.Field()
    eps = scrapy.Field()
    earnings_date = scrapy.Field()
    fwd_div_yield = scrapy.Field()
    exp_div_date = scrapy.Field()
    est_yr_target = scrapy.Field()
