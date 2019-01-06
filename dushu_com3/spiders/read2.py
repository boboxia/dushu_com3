# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider  # 导入RedisCrawlSpider
from dushu_com3.items import DushuCom3Item

import redis
class Read2Spider(RedisCrawlSpider):  # 继承的父类修改一下
    name = 'read2'  # 爬虫名字
    # start_urls = ['https://www.dushu.com/book/1081.html']  # 初始url,这里不这样用
    # 键名称的一般规则  爬虫名字:start_urls
    redis_key = 'read2:start_urls'  
    # 这里写的redis_key关系到redis 客户端 lpush时写什么
    # 由主机(即部署scrapy-redis的master端)提供
    #r = redis.Redis(host='192.168.0.103',port=6379,db=0)
    
    # 指定了页面内，链接的提取规则，会被父类自动调用
    rules = (
        Rule(LinkExtractor(allow=r'/book/1081_\d+.html'), callback='parse_item', follow=False),
    )
    # 页面数据解析函数
    # 可以自定义，只要保证callback的参数与这个函数名一致即可
    def parse_item(self, response):
        # 每页的图书列表
        book_list = response.xpath('//div[@class="bookslist"]//li')
        for each in book_list:
            #i = {}
            item = DushuCom3Item()
            item['title'] = each.xpath('.//h3//@title').extract_first()
            item['img_url'] = each.xpath('.//img/@src').extract_first()
            print(item['title'],item['img_url'])
            yield item
            

    
    