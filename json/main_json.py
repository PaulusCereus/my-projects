import json

# Преобразуем строку JSON в Python-объект
# ------------------------------------------------------------

json_string = '{"name": "Alice", "age":"25", "is_student":false}'

data = json.loads(json_string)

print(data["name"])
print(data["age"])
print(data["is_student"])