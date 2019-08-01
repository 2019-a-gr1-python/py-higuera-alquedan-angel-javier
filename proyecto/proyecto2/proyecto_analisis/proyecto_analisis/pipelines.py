# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import re

class RepararReleases(object):
  def process_item(self, item, spider):
    dates = item["releases_dates"]
    dates = dates.replace("\n", "")
    dates = dates.strip()
    dates = re.sub(r"  +","/",dates)
    item["releases_dates"]=dates
    dates = item["releases_formats"]
    dates = dates.strip()
    dates = re.sub(r" +","/",dates)
    item["releases_formats"]=dates
    return item
