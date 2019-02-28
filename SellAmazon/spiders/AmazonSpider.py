import scrapy
from scrapy.loader import ItemLoader
from SellAmazon.items import ProductItem
import logging

logger=logging.getLogger()

class AmazonSpider(scrapy.Spider):
    name='amazon'
    custom_settings = {'LOG_FILE':'product.log'}
    start_urls=['https://www.amazon.com/s?k=nike+shoes+men&crid=2QDDJJDW5ZD79&sprefix=Nike%2Caps%2C723&ref=nb_sb_ss_i_2_4']


    def parse(self,response):
        products=response.xpath('//div[contains(@class,"s-result-list")]//a[contains(@class,"a-link-normal")]/@href').getall()
        for product in products:
            logger.debug('get item url={0}'.format(product))
            yield response.follow(product,callback=self.parse_product)

    def parse_product(self,response):
        loader=ItemLoader(item=ProductItem(),response=response)
        loader.add_xpath('name','//div[@id="titleBlock"]//*[@id="productTitle"]/text()')
        loader.add_value('last_updated','today')
        return loader.load_item()
