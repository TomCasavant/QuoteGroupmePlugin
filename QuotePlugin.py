from yapsy.IPlugin import IPlugin
from urllib.request import urlopen
import json
import html2text

class QuotePlugin(IPlugin):
    def process(self, msg, client):
        if ("!quote" in msg['text']):
            response = urlopen("http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1")
            js = json.load(response)
            author = js[0]['title']
            quote = html2text.html2text(js[0]['content']).replace("\n","")
            response = f"\"{quote}\" - {author}"
            client.send_message(response)
