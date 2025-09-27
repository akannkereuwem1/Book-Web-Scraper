# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()#when using the upsert implementation, no need to update the bookitem becauuse it 
    #bypasses the item adapter and created document's_id directly when interacting with MongoDB
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
