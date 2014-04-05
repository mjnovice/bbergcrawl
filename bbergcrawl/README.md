A crawler built using scrapy library of python.
The application is simple to use, one needs to type 
the following on the terminal to start crawling the articles 
between the dates and storing them in the MongoDB database "bloomberg",
under the collections "articles".

    "scrapy crawl bloomberg -a dates=<start-date>,<end-date>"

<start-date> and <end-date> are something of the form, 
2014-02-23, ie yyyy-mm-dd.

Python dependencies:
1. Scrapy
2. html2text
3. pymongo