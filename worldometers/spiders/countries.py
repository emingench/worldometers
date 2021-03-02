# -*- coding: utf-8 -*-
import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    country_name = ''

    def parse(self, response):
        countries = response.xpath('//td/a')

        for country in countries:
            name =  country.xpath('.//text()').get()
            link =  country.xpath('.//@href').get()

            # absolute_url = f'https://www.worldometers.info{link}'
            # absolute_url = response.urljoin(link)

            yield  response.follow(url=link, callback = self.parse_country, meta={'country_name': name})

    def parse_country(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")

        for row in rows:
            year =  row.xpath('.//td[1]/text()').get()
            population =  row.xpath('.//td[2]/strong/text()').get()
            yearly_change_percent =  row.xpath('.//td[3]/text()').get()
            yearly_change =  row.xpath('.//td[4]/text()').get()
            migrants =  row.xpath('.//td[5]/text()').get()
            median_age =  row.xpath('.//td[6]/text()').get()
            fertility_rate =  row.xpath('.//td[7]/text()').get()
            density =  row.xpath('.//td[8]/text()').get()
            urban_pop_percent =  row.xpath('.//td[9]/text()').get()
            urban_pop =  row.xpath('.//td[10]/text()').get()
            share_of_world_pop =  row.xpath('.//td[11]/text()').get()
            world_pop =  row.xpath('.//td[12]/text()').get()
            global_rank =  row.xpath('.//td[13]/text()').get()
            

            yield {
                'country_name':name,   
                'year' : year,
                'population': population,
                'yearly_change_percent': yearly_change_percent,
                'yearly_change': yearly_change,
                'migrants':migrants,
                'median_age':median_age,
                'fertility_rate':fertility_rate,
                'density_P_km2':density,
                'urban_pop_percent':urban_pop_percent,
                'urban_pop':urban_pop,
                'share_of_world_pop':share_of_world_pop,
                'world_pop':world_pop,
                'global_rank':global_rank

            }