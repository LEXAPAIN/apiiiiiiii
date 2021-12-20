import feedparser
import json

rss_feed = feedparser.parse('https://lenta.ru/rss')
result = []
for news_post in rss_feed['entries']:
    cv = {'pubDate': news_post['published'], 'title': news_post['title']}
    result.append(cv)

jsn = json.dumps(result, ensure_ascii=False)
with open('news.json', 'w', encoding='utf-8') as news_file:
    news_file.write(jsn)
