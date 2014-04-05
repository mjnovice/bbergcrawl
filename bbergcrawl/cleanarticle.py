import html2text

"""
A class which handles the conversion of HTML article 
to clean text.
"""
class cleanarticle:
    articlehtml = ""
    title = ""

    def __init__(self, articlehtml, articletitle):
	self.articlehtml = articlehtml
	self.title = articletitle

    """
    cleans the article and converts it into a JSON format.
    """
    def cleanjson(self):
	c = html2text.HTML2Text()
	c.ignore_links = True
	clean_article = c.handle(str(self.articlehtml))
	json_article = self.jsonify(clean_article)
	return json_article

    """
    converts an input article into JSON.
    """
    def jsonify(self, clean_article):
	return {"title":self.title,"article":clean_article}