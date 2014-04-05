"""
contains the xpaths patterns used by the crawler.
"""
START_URL_PREFIX = 'http://www.bloomberg.com/archive/news/'
BASE_URL = 'http://www.bloomberg.com'
ARTICLE_LINK_XPATH = '//ul[contains(@class, "stories")]/li/a/@href'
ARTICLE_BODY_XPATH = '//div[contains(@itemprop, "articleBody")]'