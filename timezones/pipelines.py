from scrapy.exceptions import DropItem


class TimezonesPipeline:
    def process_item(self, item, spider):
        if spider.status != "all" and item["status"].lower() != spider.status.lower():
            raise DropItem()
        return item
