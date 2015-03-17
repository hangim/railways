# -*- coding: utf-8 -*-

# Scrapy settings for railways project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'railways'

SPIDER_MODULES = ['railways.spiders']
NEWSPIDER_MODULE = 'railways.spiders'

ITEM_PIPELINES = ['railways.pipelines.RailwaysPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'railways (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2327.5 Safari/537.36'

CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True

LOG_LEVEL = 'INFO'
