import requests

URL = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url=URL)

print(f"Ответ response - {response}\n")
print(f"Статус-код ответа - {response.status_code}\n")
print(f"Текст ответа - {response.text}\n")
resp_json = response.json()
print(f"JSON ответа - {resp_json}\n")

print(f"""
Номер шутки: {resp_json['id']}
Тип шутки: {resp_json['type']}
Сетап: {resp_json['setup']}
Панчалайн: {resp_json['punchline']}
""")