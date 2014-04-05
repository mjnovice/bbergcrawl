from scrapy import log
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from bbergcrawl.storeinmongo import storeinmongo
from bbergcrawl.cleanarticle import cleanarticle
from bbergcrawl.xpaths import *
from datetime import timedelta,date

"""
The spider responsible for crawling bloomberg.com
"""
class BloombergSpider(Spider):
    name = 'bloomberg'
    allowed_domains = ['bloomberg.com']
    start_urls = []

    """
    Initialises the start_urls based upon the input dates.
    """
    def __init__(self, *args, **kwargs):
	try:
	    tup = kwargs.get('dates').split(',')
	    datetup = self.todate(tup)
	    for d in (datetup[0],datetup[1]+timedelta(days=1)):
		self.start_urls.append(START_URL_PREFIX+str(d))
	except:
	    print "There seems to be some error, with the input dates."
	print self.start_urls

    """
    converts a date like yyyy-mm-dd into date(yyyy,mm,dd)
    """
    def todate(self,datetup):
	startd = datetup[0].split('-')
	endd = datetup[1].split('-')
	sd = date(int(startd[0]),int(startd[1]),int(startd[2]))
	ed = date(int(endd[0]),int(endd[1]),int(endd[2]))
	return (sd,ed)

    """
    The main parser for getting responses from the list of
    start_urls.
    """
    def parse(self, response):
	hxs = HtmlXPathSelector(response)
	articlelinks = hxs.select(ARTICLE_LINK_XPATH).extract()
	filename = response.url.split("/")[-1]
	for articlelink in articlelinks:
	    url = BASE_URL + articlelink
	    print url
	    yield Request(url,self.parse_article)
	    self.log("Article %s Successfuly Sent for Parsing" % url.split('/')[-1])
        self.log('Archive from date %s crawled!' % response.url[-1])

    """
    The method responsible for parsing the article .
    """
    def parse_article(self, response):
	hxs2 = HtmlXPathSelector(response)
	article_title = response.url.split('/')[-1] 
	article_html = hxs2.select(ARTICLE_BODY_XPATH).extract()
	self.cleanandstore(article_html, article_title)
	self.log("Article %s Successfuly Sent for Parsing" % response.url.split('/')[-1])
	self.log("-------------------------------------------------------------------------")

    """
    The method for cleaning and storing the articles, by calling
    appropriate methods from classes storeinmongo and cleanarticle
    """
    def cleanandstore(self, article_html, article_title):
	cleaner = cleanarticle(article_html, article_title)
	p = storeinmongo("bloomberg", "articles")
	p.store(cleaner.cleanjson())