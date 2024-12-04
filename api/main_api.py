# import requests
# import json
# import pprint

# response = requests.get("https://randomuser.me/api")
# if response.ok:
#     data = response.json()
#     user = data["results"][0]
#     print(f"Имя: {user['name']['first']}")
#     print(f"Страна: {user['location']['country']}")
#     print("-" * 30)
#     print("Printing data")
#     pprint.pprint(data)
#     print("Printing user")
#     pprint.pprint(user)
# else:
#     print("Ошибка получения данных")

# ----------------------------------------------------

# import requests

# response = requests.get("https://api.quotable.io/random")

# if response.status_code == 200:
#     data = response.json()
#     print(f"Случайная цитата: '{data['content']}' - {data['author']}")
# else:
#     print("Не удалось получить цитату")


# ----------------------------------------------------

import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Hello, API!",
    "body": "This is a test post",
    "userId": 1
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print("Данные успешно отправлены")
    print(f"Ответ сервера: {response.json()}")
else:
    print(f"Ошибка: {response.status_code}")