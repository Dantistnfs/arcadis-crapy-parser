# -*- coding: utf-8 -*-
import scrapy

from aracdis.items import AracdisItem

class CitiesIndexSpider(scrapy.Spider):
	name = "cities-index"
	allowed_domains = ["arcadis.com"]
	start_urls = ('https://www.arcadis.com/en/global/our-perspectives/sustainable-cities-index-2016/comparing-cities/?tf=tab-profit&sf=all&r=all&c=all',)

	def parse(self, response):
		item = AracdisItem()
		get_graphs = response.xpath('//div[@class="scroll-wrap"]/div')

		for graph in get_graphs[1:len(get_graphs)]:
			item['graph_type'] = graph.xpath("@class").extract()[0].split(" ")[1]
			
			cities_list = graph.xpath('div[@class="graph_wrap"]/div')
			for city in cities_list:
				location = city.xpath('@class').extract()[0].split(" ")
				item['city_name'] = location[-1]
				try:
					item['city_region'] = location[-2]
				except Exception:
					item['city_region'] = ' '
				city_data = city.xpath('div[@class="bars"]/div/span')
				for data in city_data:
					item['value'] = data.xpath('@data-width').extract()[0] #percent value
					try:
						item['value_name'] = data.xpath('@class').extract()[0].split(" ")[-1] #name of value
					except Exception:
						item['value_name'] = 'all'
					yield item
