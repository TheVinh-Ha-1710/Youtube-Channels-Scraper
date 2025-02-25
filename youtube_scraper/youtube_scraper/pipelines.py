# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class ChannelsCrawlerPipeline:
    def process_item(self, item, spider):
        if (
            item["subscribers"] == "0"
            or item["video_views"] == "0"
            or item["video_count"] == "0"
        ):
            raise DropItem(f"Channel terminated or illegitimate: {item}")
        return item

class YoutubeScraperPipeline:
    def process_item(self, item, spider):
        return item
