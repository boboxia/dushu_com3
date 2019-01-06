# -*- coding: utf-8 -*-

# Scrapy settings for dushu_com3 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dushu_com3'

SPIDER_MODULES = ['dushu_com3.spiders']
NEWSPIDER_MODULE = 'dushu_com3.spiders'

# ȥ���������
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# redis������������
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# redis�Ƿ񱾵ػ��Ŀ���
#������α�ֲ�ʽ��ѡ�񱾵ػ�
SCHEDULER_PERSIST = True

# �ֲ�ʽ������Ҫ����Ҫ���ʵ�redis������
#REDIS_HOST = '10.11.56.63'  # ����ip,����д'localhost'
REDIS_HOST = '192.168.0.103'#����scrapy-redis��master�ˣ�����scrapy-redis��slave�� ���õ�������REDIS_URL = 'redis://192.168.1.112:6379'
REDIS_PORT = 6379


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dushu_com3 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

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
#    'dushu_com3.middlewares.DushuCom3SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'dushu_com3.middlewares.DushuCom3DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'dushu_com3.pipelines.DushuCom3Pipeline': 300,
#}
ITEM_PIPELINES = {
   'dushu_com3.pipelines.DushuCom3Pipeline': 300,

    # ����redis��pipeline����
   'scrapy_redis.pipelines.RedisPipeline':400,
}

MONGO_URL = 'mongodb://localhost:27017'
MONGO_DB = "BOOK_DUSHU_COM"
# ��ʱ1s(������)
DOWMLOAD_DELAY = 1


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
