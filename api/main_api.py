import requests
import json
import pprint

response = requests.get("https://randomuser.me/api")
if response.ok:
    data = response.json()
    user = data["results"][0]
    print(f"Имя: {user['name']['first']}")
    print(f"Страна: {user['location']['country']}")
    print("-" * 30)
    print("Printing data")
    pprint.pprint(data)
    print("Printing user")
    pprint.pprint(user)
else:
    print("Ошибка получения данных")

