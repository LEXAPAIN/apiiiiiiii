import json
jsonFile = open("news.json")
with open("news.json", 'r', encoding='utf-8') as fh:
    data = json.load(fh)
print(data)
