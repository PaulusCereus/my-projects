import requests

def get_all_by_name():
    name = input("Введите имя для проверки ")
    params = {"name": name}

    response_gender = requests.get(url=URL_GENDER, params=params)
    response_age = requests.get(url=URL_AGE, params=params)
    response_nationality = requests.get(url=URL_NATIONALITY, params=params)

    resp_json_gender = response_gender.json()
    resp_json_age = response_age.json()
    resp_json_nationality = response_nationality.json()

# Пример
# Данные по полу
# {'count': 215520, 'name': 'Nicola', 'gender': 'male', 'probability': 0.81}
# Данные по возрасту
# {'count': 56726, 'name': 'Nicola', 'age': 55}
# Данные по национальности
# {'count': 15390, 'name': 'Nicola', 'country': [
#     {'country_id': 'RO', 'probability': 0.13134792236427048},
#     {'country_id': 'IT', 'probability': 0.11797839644845824},
#     {'country_id': 'UY', 'probability': 0.05143364431909301},
#     {'country_id': 'EC', 'probability': 0.046905085909882765},
#     {'country_id': 'AR', 'probability': 0.03606483507686333}]}

    print(f"Вы ввели имя - {name}")
    print(f"{name} является {resp_json_gender['gender']} с вероятностью {resp_json_gender['probability']}")
    print(f"{name} примерно {resp_json_age['age']}")
    print(f"{name} может быть из\n")
    for i in resp_json_nationality['country']:
        print(f"{i["country_id"]} с вероятностью {i["probability"]}")


URL_GENDER = "https://api.genderize.io"
URL_AGE = "https://api.agify.io"
URL_NATIONALITY = "https://api.nationalize.io"

get_all_by_name()