# -*- coding: utf-8 -*-
import scrapy
import pandas as pd


class ArticleShortSpider(scrapy.Spider):
    name = 'article_short'

    def start_requests(self):
        df = pd.read_csv('article_url.csv')
        url_lst = df.article_url[0:11]
        for url in url_lst:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for article in response.css('article'):
            yield {
                'article_id': article.css('div.top div::attr(data-subject-id)').extract(),
                'article_title': article.css('h1::text').extract(),
                'authur_id': article.css('div.top div::attr(data-id)').extract(),
                'author_name': article.css('span.name::text').extract(),
                'author_bio': article.css('div[class="bio hidden-print"]::text').extract(),
                'date': article.css('header time::attr(datetime)').extract(),
                'summary': article.css('div.a-sum p::text').extract(),
                'paragraph_titles': article.css('div[class="sa-art article-width"] h3::text').extract(),
                'body': article.css('div[class="sa-art article-width"] p::text').extract(),
                'disclosure': article.css('p[id="a-disclosure"] span::text').extract(),
                #'num_likes': article.css('span[class="like hide-btn"] div::attr(data-likers)').extract()
                #'num_likes': article.css('div.likers.show-likers.only-one').xpath('@data-likers').extract()
                'num_likes': article.css('div[class="like"] div[class="likers show-likers only-one"]').xpath('@data-likers').extract() # no value
            }
