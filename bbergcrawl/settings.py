# Scrapy settings for bbergcrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bbergcrawl'

SPIDER_MODULES = ['bbergcrawl.spiders']
NEWSPIDER_MODULE = 'bbergcrawl.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bbergcrawl (+http://www.yourdomain.com)'
