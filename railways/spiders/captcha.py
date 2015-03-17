# -*- coding: utf-8 -*-
import scrapy
from railways.items import RailwaysItem
import hashlib
import random

class RailwaysSpider(scrapy.Spider):
    name = "railways"
    allowed_domains = ["kyfw.12306.cn"]
    url = 'https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&'

    def __init__(self):
        self.start_urls = [self.url + str(random.random())]

    def parse(self, response):
        item = RailwaysItem()
        item['raw'] = response.body
        item['sha1'] = hashlib.sha1(response.body).hexdigest()
        yield item
        yield scrapy.Request(self.url + str(random.random()), callback = self.parse)

