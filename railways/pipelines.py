# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import logging

class RailwaysPipeline(object):
    def __init__(self):
        if not os.path.exists('img'):
            os.makedirs('img')

    def process_item(self, item, spider):
        # return item
        print(item['sha1'])
        
        logging.basicConfig(filename = 'railways.log', level = logging.DEBUG)
        logging.info(item['sha1'])

        # 刷新过快
        if (item['sha1'] == 'c2712a36ef0a1319da89eb931d4edac37a5f20ac'):
            return
        
        with open('./img/' + item['sha1'], 'wb') as fb:
            fb.write(item['raw'])
