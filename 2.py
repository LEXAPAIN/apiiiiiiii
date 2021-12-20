import requests
repositories = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars')
print(f" Общее кол-во репозиториев на Python- {repositories.json()['total_count']} ")
print(f" Самый популярный репозиторий {repositories.json()['items'][0]}")
print("Прочие репозитории репозитории:")
for rep in repositories.json()['items'][1:]:
    print(rep['name'], rep['url'])
