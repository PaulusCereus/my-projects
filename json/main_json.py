import json

# Преобразуем строку JSON в Python-объект
# ------------------------------------------------------------

# json_string = '{"name": "Alice", "age":"25", "is_student":false}'

# data = json.loads(json_string)

# print(data["name"])
# print(data["age"])
# print(data["is_student"])

# Преобразуем Python-объект в строку JSON
# ------------------------------------------------------------

python_data = {
    "name": "Leha",
    "age": 5,
    "gruz": 200,
    "is_student": True,
    "skills": [],
}

json_string = json.dumps(python_data, indent=4)
print(json_string)