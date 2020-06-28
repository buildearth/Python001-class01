# -*- coding: utf-8 -*-

# Scrapy settings for spiders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spiders'

SPIDER_MODULES = ['spiders.spiders']
NEWSPIDER_MODULE = 'spiders.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'spiders (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
  'Cookie': 'uuid_n_v=v1; uuid=9BF004F0B5C311EAAD7CEBC74F78E0F95C3D56CAB3FE445F99D6EBA7900DD526; _lxsdk_cuid=172e42fbd2ac8-0e05f5e49d02d9-3f770c5a-100200-172e42fbd2ac8; _lxsdk=9BF004F0B5C311EAAD7CEBC74F78E0F95C3D56CAB3FE445F99D6EBA7900DD526; mojo-uuid=3541ca2920d824e62e5b2726f16d272f; _csrf=c34c908cefb54a819623eeccf8c573846c6eecd21914095e0988da7922407730; lt=iFP_tk4hEvWpLqe68TP_T3HUCYYAAAAA5woAAABR9yGapJYwO0XpVTCbTvsxiT8_GUcNj3-LxOwUhCMS_T0WruD7dQgLEsNacGiYhA; lt.sig=e7tPy7wQo2Um5GlrqY5ORYe5dbo; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593325259,1593325402,1593325417,1593326373; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=209043117.1592966246630.1593325452378.1593326373367.16; mojo-session-id={"id":"6e181891c9f9f9f6b66dfce6813a16a2","time":1593332272691}; mojo-trace-id=4; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593332356; _lxsdk_s=172fa00a5f2-cbf-d62-ac8%7C692297092%7C9'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'spiders.middlewares.SpidersSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'spiders.middlewares.SpidersDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'spiders.pipelines.SpidersPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
