# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YoutubeChannelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    channel_name = scrapy.Field()
    slug = scrapy.Field()
    subscribers = scrapy.Field()
    video_views = scrapy.Field()
    video_count = scrapy.Field()
    category = scrapy.Field()
    started = scrapy.Field()
    channel_id = scrapy.Field()
    
