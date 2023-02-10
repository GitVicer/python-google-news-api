from pygooglenews import GoogleNews
from flask import Flask

app = Flask(__name__)

gn = GoogleNews(lang = 'en', country = 'India')

@app.route("/g_news/<string:keyword>")
def search_by_keyword(keyword):
    news_data = gn.search(f'intitle:{keyword}')
    return(news_data)

@app.route("/g_news/location/<string:location>")
def search_by_location(location):
    news_data = gn.geo_headlines(location)
    return(news_data)  

@app.route("/g_news/topic/<string:topic>")
def search_by_topic(topic):
    news_data = gn.topic_headlines(topic)
    return(news_data)

@app.route("/g_news/top_feeds")
def top_feeds():
    news_data = gn.top_news()
    return(news_data)
    