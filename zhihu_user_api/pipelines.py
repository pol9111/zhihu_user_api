# -*- coding: utf-8 -*-
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item

class MongoPipeline(object):

    def __init__(self):
        self.mongo_uri = settings['MONGO_URI']
        self.mongo_db = settings['MONGO_DATABASE']

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db['users'].insert(dict(item))

