import json

import scrapy


class WikiSpider(scrapy.Spider):
    name = "wiki"
    start_urls = ["https://en.wikipedia.org/wiki/List_of_tz_database_time_zones"]

    def parse(self, response: scrapy.http.Response):
        self.log(f"Content length: {len(response.body)}")
        table = response.css("table.wikitable")[0]
        rows = table.css("tbody>tr")
        data = []
        for row in rows[1:]:
            status = (row.css("td:nth-child(5)::text").get() or "").rstrip()
            if status != "Canonical":
                continue
            item = {
                "country_code": row.css("td:nth-child(1)>a::text").get(),
                "lat_lng": row.css("td:nth-child(2)::text").get(),
                "title": row.css("td:nth-child(3)>a::text").get(),
                "status": status,
                "utc_offset": row.css("td:nth-child(6)>a::text").get(),
                "utc_offset_dst": row.css("td:nth-child(7)>a::text").get(),
            }
            for key in item:
                if item[key] and item[key].endswith("\n"):
                    item[key] = item[key].rstrip()
            data.append(item)
        with open("tz.json", "w") as f:
            json.dump(data, f, indent=2)
