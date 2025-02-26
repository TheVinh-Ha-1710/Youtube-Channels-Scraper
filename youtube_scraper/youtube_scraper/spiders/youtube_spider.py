import scrapy
from youtube_scraper.items import YoutubeChannelItem

class YoutubeSpider(scrapy.Spider):
    name = "youtube_spider"
    custom_settings = {
        "ITEM_PIPELINES": {
            "youtube_scraper.pipelines.ChannelsCrawlerPipeline": 1,
        }
    }
    allowed_domains = ["us.youtubers.me", "youtube.com"]
    start_urls = [
        # "https://us.youtubers.me/viet-nam/autos-vehicles/top-1000-youtube-channels-in-viet-nam",
        # "https://us.youtubers.me/viet-nam/music/top-1000-youtube-channels-in-viet-nam",
        # "https://us.youtubers.me/viet-nam/pets-animals/top-1000-youtube-channels-in-viet-nam",
        # "https://us.youtubers.me/viet-nam/sports/top-1000-youtube-channels-in-viet-nam",
        # "https://us.youtubers.me/viet-nam/travel-events/top-1000-youtube-channels-in-viet-nam",
        # "https://us.youtubers.me/viet-nam/gaming/top-1000-youtube-channels-in-viet-nam",
        # "https://us.youtubers.me/viet-nam/people-blogs/top-1000-youtube-channels-in-viet-nam",
        # "https://us.youtubers.me/viet-nam/comedy/top-1000-youtube-channels-in-viet-nam",
        # "https://us.youtubers.me/viet-nam/entertainment/top-1000-youtube-channels-in-viet-nam",
        # "https://us.youtubers.me/viet-nam/news-politics/top-1000-youtube-channels-in-viet-nam",
        # "https://us.youtubers.me/viet-nam/howto-style/top-1000-youtube-channels-in-viet-nam",
        #"https://us.youtubers.me/viet-nam/education/top-1000-youtube-channels-in-viet-nam",
        "https://us.youtubers.me/viet-nam/science-technology/top-1000-youtube-channels-in-viet-nam"
    ]
    
    def parse(self, response):
        table = response.css("table.top-charts")[0]  # Get the table
        data_rows = table.css("tr")  
        data_rows.pop(0)    # Remove the header row
        
        for row in data_rows:
            item = YoutubeChannelItem()
            item["rank"] = row.css("td:nth-child(1)::text").get(default="").strip()
            item["channel_name"] = "".join(
                row.css("td:nth-child(2) a::text").getall()[1].strip()
            )
            item["slug"] = (
                row.css("td:nth-child(2) a::attr(href)").get(default="").strip().split("/")[-2]
            )
            item["subscribers"] = row.css("td:nth-child(3)::text").get(default="0").strip()
            item["video_views"] = row.css("td:nth-child(4)::text").get(default="0").strip()
            item["video_count"] = row.css("td:nth-child(5)::text").get(default="0").strip()
            item["category"] = row.css("td:nth-child(6) a::text").get(default="").strip()
            item["started"] = row.css("td:nth-child(7)::text").get(default="0").strip()
            redirect_url = f"https://us.youtubers.me/{item['slug']}/youtube"
            request  = scrapy.Request(
                redirect_url,
                callback=self.parse_channel_id,
                meta={"item": item}
            )
            yield request
            
    def parse_channel_id(self, response):
        item = response.meta["item"]
        item["channel_id"] = response.url.split("/")[-1]
        yield item