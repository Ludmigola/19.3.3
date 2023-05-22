import requests
import json

def print_res(resp):
  """ Функция для вывода статуса и тела ответа """
  print(resp.status_code)
  if 'application/json' in resp.headers['Content-Type']:
    print(resp.json())
  else:
    print(resp.text)

status = 'available' # зададим переменную статуса для запроса
# отправим GET-запрос 
res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}',
                   headers={'accept':'application/json'})
print_res(res)


petId = 125 # создадим зарезервированный id для создания и изменения питомца

# создадим словарь с данными о питомце
new_pet = {"id": petId,
  "category": {
    "id": petId,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": petId,
      "name": "string"
    }
  ],
  "status": "available"
}

# отправим POST-запрос с данными о питомце
res = requests.post(f'https://petstore.swagger.io/v2/pet',
                   headers={'accept':'application/json', 'Content-Type':'application/json'},
                   data=json.dumps(new_pet)) # упакуем словарь в json формат

print_res(res)

updated_pet = new_pet # теперь создадим копию данных о питомце
updated_pet["name"] = "Bobbie" # и изменим имя "name"

# отправим PUT-запрос с измененными данными о питомце
res = requests.put(f'https://petstore.swagger.io/v2/pet',
                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                   data=json.dumps(updated_pet)) # упакуем словарь в json формат

print_res(res)

# отправим DELETE-запрос для удаления питомца с id == petId
res = requests.delete(f'https://petstore.swagger.io/v2/pet/{petId}',
                     headers={'accept': 'application/json'})
print_res(res)



