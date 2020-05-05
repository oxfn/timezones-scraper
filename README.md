Python + Scrapy bot which helps to **load the list of IANA timezones names** from
[corresponding Wikipedia page](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
and store it in any handy and machine-readable format supported by Scrapy.

It grabs the following fields:

- Standardized name
- Country code
- Latitude / longitude
- Timezone status (Canonical / Alias / Deprecated)
- UTC offset
- UTC offset for [DST](https://en.wikipedia.org/wiki/Daylight_saving_time)

## Installation

1. Initialize virtual environment
   
   `python3 -m venv venv`

2. Activate virtual environment
   
   `source venv/bin/activate`

3. Install required packages
   
   `pip install -r requirements.txt`

## Usage

### Generic usage

`scrapy crawl wiki [-o file.<json|csv|xml|...>] [-a status=<all|canonical|alias|deprecated>]`
