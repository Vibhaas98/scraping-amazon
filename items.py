# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DynotifyItem(scrapy.Item):
    mobile_name = scrapy.Field()
    mobile_price = scrapy.Field()
    price_discount = scrapy.Field()
    mobile_rating = scrapy.Field()
    mobile_image = scrapy.Field()
