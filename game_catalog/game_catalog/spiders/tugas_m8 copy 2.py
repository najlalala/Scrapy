import scrapy
import pandas as pd

class CrawlingSpider(scrapy.Spider):
    name = "webcrawl"
    start_urls = ["https://store.playstation.com/en-id/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/"]
    
    def parse(self, response):
        product_links = response.css('a::attr(href)').getall()  

        for link in product_links:
            yield response.follow(link, callback=self.parse_item)

    def parse_item(self, response):
        titles = response.css("span.psw-t-body.psw-c-t-1.psw-t-truncate-2.psw-m-b-2::text").getall()
        prices = response.css("span.psw-m-r-3::text").getall()

        for title, price in zip(titles, prices):
            yield {
                "Nama Game": title.strip(),
                "Harga Game": price.strip()}