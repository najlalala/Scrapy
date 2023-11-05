import scrapy
import pandas as pd

class nalaSpider(scrapy.Spider):
    name = "nala"

    def start_requests(self):
        base_url = "https://store.playstation.com/en-id/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/"
        for page in range(1, 17):
            url = f"{base_url}{page}"
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        titles = response.css("span.psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2::text").getall()
        prices = response.css("span.psw-m-r-3::text").getall()

        for title, price in zip(titles, prices):
            yield {'title': title.strip(), 'Price': price.strip()}
