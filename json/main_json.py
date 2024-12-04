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

# python_data = {
#     "name": "Leha",
#     "age": 5,
#     "gruz": 200,
#     "is_student": True,
#     "skills": [],
# }

# json_string = json.dumps(python_data, indent=4)
# print(json_string)

# Загрузка данных из JSON файла
# ------------------------------------------------------------

# Путь до файла указываем от папки my-projects, так как мы находимся в ней
# и путь ищется от неё до файла data.json

# В данном случае мы применяем контекстный менеджер для открытия файла
# на чтение ("r") (("read")) и сохраняем указатель на файл в виде file
# Использование контекстного менеджера удобно, так как при завершении работы
# нам не нужно вручную закрывать файл
with open("./json/data.json", "r") as file:
    data = json.load(file)

print(data)
print(data["skills"])
print(data["name"])