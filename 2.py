import requests

repos = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars')

print(f"{repos.json()['total_count']} - Общее количество репозиториев на Python")
print(f" Самый популярный репозиторий {repos.json()['items'][0]}")
print("Остальные популярные репозитории")
for i in repos.json()['items'][1:]:
    print(i['name'], i['url'])
