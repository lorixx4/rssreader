import feedparser

from flask import Flask

app = Flask(__name__)

BBC_FEDD = "http://feeds.bbci.co.uk/news/rss.xml"
RSS_FEEDS = {'bbc' : 'http://feeds.bbci.co.uk/news/rss.xm',
             'cnn' : 'http://rss.cnn.com/rss/edition.rss',
             'fox' : 'http://feeds.foxnews.com/foxnews/latest',
             'iol' : 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="cnn"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed["entries"][0]
    return """<html>
        <body>
            <h1>BBC HEADLINES</h1>
            <b>{0}</b>
            <b>{1}</b>
            <p>{2}</p>
        </body>
    </html>""".format(first_article.get("title"),first_article.get("published"),
    first_article.get("summary"))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
