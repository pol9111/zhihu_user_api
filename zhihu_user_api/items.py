# -*- coding: utf-8 -*-

import scrapy


class ZhihuUserApiItem(scrapy.Item):
    name = scrapy.Field()
    headline = scrapy.Field()
    answer_count = scrapy.Field()
    follower_count = scrapy.Field()
    gender = scrapy.Field()
    article_count = scrapy.Field()
    id = scrapy.Field()
    url_token = scrapy.Field()
    badge = scrapy.Field()


