# -*- coding: utf-8 -*-
import scrapy


class ListShortSpider(scrapy.Spider):
    name = 'list_short'
    allowed_domains = ['seekingalpha.com']
    start_urls = ['https://seekingalpha.com/stock-ideas/short-ideas?page=' + str(i) for i in range(1,2)]

    def parse(self, response):
        for article in response.css('ul.articles-list li'):
            yield {
                'article_id': article.xpath('@article_id').extract(),
                'ticker': article.css('div.a-info span a::text').extract(),
                'company_name': article.css('div.a-info span a').xpath('@title').extract(),
                'info': article.css('div.a-info span::text').extract(),
                'author_id': article.xpath('@data-user-id').extract(),
                'author_name': article.css('div.a-info a::text').extract(), # cannot save this variable.
                'author_link': article.css('div.media-left a').xpath('@href').extract(),
                'article_link': article.css('a.a-title').xpath('@href').extract()
            }
