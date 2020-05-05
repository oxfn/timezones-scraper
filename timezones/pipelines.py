# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TimezonesPipeline:
    def process_item(self, item, spider):
        if spider.status != "all" and item["status"].lower() != spider.status.lower():
            raise DropItem()
        return item
