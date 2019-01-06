# -*-coding: utf-8 -*-  
#author:
#data:2019-01-10
#description:this program just to get qq news,we'll get the news title and content

import sys,os
#reload(sys)

from scrapy.spider import Spider  
from dushu_com2.items import QQNews
from scrapy.http import Request
from scrapy.selector import Selector

class QQNewsSpider(Spider):
    name = 'qq_news'
    allow_domain = 'https://new.qq.com/'
    start_urls= ["https://new.qq.com/ch/milite/"]

    def parse(self,response):
        news_urls = Selector(response)
        for start_url in news_urls.xpath('//a[@class=\"picture\"]/@href').extract():
            #print(start_url)
            yield Request(url=start_url,callback=self.second_parse) 

    def second_parse(self,response):
        detail_sel = Selector(response)
        content = ""
        item = QQNews()
        item['title'] =  detail_sel.xpath('//div[@class=\"LEFT\"]/h1/text()').extract()
        item['content'] = ''.join(detail_sel.xpath('//div[@class=\"content-article\"]/p/text()').extract())#�δ��Ƕ��p��ǩ
        #print(item['title'])
        #print(item['content'])

        yield item