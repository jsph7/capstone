# -*- coding: utf-8 -*-

# Scrapy settings for article project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'article'

SPIDER_MODULES = ['article.spiders']
NEWSPIDER_MODULE = 'article.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
#USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0'
#USER_AGENT = '/Users/Woosik/capstone/scrapy/article/useragents.txt'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'article.middlewares.ArticleSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'article.middlewares.ArticleDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'article.pipelines.ArticlePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


#socket proxy setting
# DOWNLOADER_MIDDLEWARES = {
#     'article.middlewares.ProxyMiddleware': 1,
# }

# DOWNLOADER_MIDDLEWARES = {
#     'article.middlewares.ProxyMiddleware': 1,
#     'article.middlewares.DelayAfterConnectionRefusedMiddleware': 510,
# }

# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#     'article.middlewares.ProxyMiddleware': 100,
# }


# random_useragent setting
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
#     'random_useragent.RandomUserAgentMiddleware': 400
# }


# fake-useragent settings
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
}



## scrapoxy setting
# CONCURRENT_REQUESTS_PER_DOMAIN = 1
# RETRY_TIMES = 0
#
# # PROXY
# PROXY = 'http://127.0.0.1:8888/?noconnect'
#
# # SCRAPOXY
# API_SCRAPOXY = 'http://127.0.0.1:8889/api'
# API_SCRAPOXY_PASSWORD = 'chilbang'
#
# DOWNLOADER_MIDDLEWARES = {
#     'scrapoxy.downloadmiddlewares.proxy.ProxyMiddleware': 100,
#     'scrapoxy.downloadmiddlewares.wait.WaitMiddleware': 101,
#     'scrapoxy.downloadmiddlewares.scale.ScaleMiddleware': 102,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
# }
