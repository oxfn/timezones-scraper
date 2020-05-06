# -*- coding: utf-8 -*-

BOT_NAME = "timezones"
LOG_LEVEL = "WARNING"
SPIDER_MODULES = ["timezones.spiders"]
NEWSPIDER_MODULE = "timezones.spiders"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"
)
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    "timezones.pipelines.TimezonesPipeline": 100,
}
