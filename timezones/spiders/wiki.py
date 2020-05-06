import json
import logging

import pytz
import scrapy

from ..items import Timezone


class WikiSpider(scrapy.Spider):
    name = "wiki"
    start_urls = ["https://en.wikipedia.org/wiki/List_of_tz_database_time_zones"]

    def __init__(self, status="all", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status = status

    @staticmethod
    def _get_col(row, col, link=False, dash=False, strip=False):
        selector = f"td:nth-child({col}){'>a' if link else ''}::text"
        val = row.css(selector).get()
        if not val:
            return ""
        if dash:
            val = val.replace("\u2212", "-")
        if strip:
            val = val.strip()
        return val

    def parse(self, response: scrapy.http.Response):
        # Collecting data
        table = response.css("table.wikitable")[0]
        rows = table.css("tbody>tr")
        for row in rows[1:]:
            status = self._get_col(row, 5, strip=True)
            name = self._get_col(row, 3, link=True)
            yield Timezone(
                country_code=self._get_col(row, 1, link=True),
                lat_lng=self._get_col(row, 2, dash=True, strip=True),
                name=name,
                status=status,
                utc_offset=self._get_col(row, 6, link=True, dash=True),
                utc_offset_dst=self._get_col(row, 7, link=True, dash=True),
            )
