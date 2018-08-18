# -*- coding: utf-8 -*-
import scrapy
import json

from zhihu_user_api.items import ZhihuUserApiItem


class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']


    start_user = 'Hemerocallis-Yu'
    followers_url = "https://www.zhihu.com/api/v4/members/{url_token}/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20"

    def start_requests(self):
        yield scrapy.Request(self.followers_url.format(url_token=self.start_user), callback=self.parse)

    def parse(self, response):

        resp = json.loads(response.text)

        item = ZhihuUserApiItem()

        for info in resp.get('data'):
            item['name'] = info.get('name')
            item['headline'] = info.get('headline')
            item['answer_count'] = info.get('answer_count')
            item['follower_count'] = info.get('follower_count')
            item['gender'] = info.get('gender')
            item['article_count'] = info.get('article_count')
            item['id'] = info.get('id')
            item['url_token'] = info.get('url_token')
            item['badge'] = info.get('badge')
            yield item
            # 递归粉丝的粉丝
            yield scrapy.Request(self.followers_url.format(url_token=item['url_token']), callback=self.parse)

        # 判断是否有下一页
        if 'paging' in resp.keys() and resp.get('paging').get('is_end') == False:
            next_page = resp.get('paging').get('next')
            yield scrapy.Request(next_page, self.parse)


