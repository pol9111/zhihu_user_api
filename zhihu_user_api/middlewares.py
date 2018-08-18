# -*- coding: utf-8 -*-

class RandomProxy(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = "https://" + "101.236.43.153:8866"


