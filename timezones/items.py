import scrapy


class Timezone(scrapy.Item):
    name = scrapy.Field()
    country_code = scrapy.Field()
    status = scrapy.Field()
    lat_lng = scrapy.Field()
    utc_offset = scrapy.Field()
    utc_offset_dst = scrapy.Field()
