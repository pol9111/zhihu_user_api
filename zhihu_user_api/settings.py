# -*- coding: utf-8 -*-

BOT_NAME = 'zhihu_user_api'

SPIDER_MODULES = ['zhihu_user_api.spiders']
NEWSPIDER_MODULE = 'zhihu_user_api.spiders'

ROBOTSTXT_OBEY = False

TELNETCONSOLE_PORT = [5005]

DOWNLOAD_DELAY = 2.5

COOKIES_ENABLED = True

DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'cookie': '',
    'upgrade-insecure-requests': '1',
    'X-Forwarded-For': '68.154.157.35',
    'user-agent': 'Mozilla/4.0 (compatible; GoogleToolbar 6.1.1518.856; Windows 5.2; MSIE 7.0.5730.13)',
}

DOWNLOADER_MIDDLEWARES = {
   'zhihu_user_api.middlewares.RandomProxy': 543,
}

MONGO_URI = 'localhost'
MONGO_DATABASE = 'zhihu'

ITEM_PIPELINES = {
   'zhihu_user_api.pipelines.DuplicatesPipeline': 200,
   'zhihu_user_api.pipelines.MongoPipeline': 300,
}


